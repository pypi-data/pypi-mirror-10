
from AXUI.logger import LOGGER
from AXUI.driver import DriverException

import UIA
import ctypes
import _ctypes

import win32
import screenshot
import Translater

def _unpack(flag, name, *args):
    return flag, name, args

class Method(object):
    '''Wrapper class for UIA pattern method
    '''
    def __init__(self, function_object, name, args_expected=None):
        if args_expected is None:
            args_expected = []
    
        self.function_object = function_object
        self.name = name
        self.args = []
        self.outs = []
        for arg in args_expected:
            arg_direction = arg[0]
            arg_type = arg[1]
            arg_name = arg[2]
            if arg_direction == "in":
                self.args.append([arg_type, arg_name])
            elif arg_direction == "out":
                self.outs.append([arg_type, arg_name])
            else:
                #skip unsupported arg_direction
                raise DriverException("Unsupported arg_direction: %s" % arg_direction)

    def __repr__(self):
        docstring = "Name:\t"+self.name+"\n"
        argument_string = "Arguments:\n"
        for argument in self.args:
            argument_type = argument[0]
            argument_name = argument[1]

            if argument_type == "POINTER(IUIAutomationElement)":
                argument_type = "UIElement"
            elif argument_type in UIA.UIA_enums:
                argument_type = UIA.UIA_enums[argument_type]

            argument_string +="  Name:\t"+argument_name+"\n"
            argument_string +="  Type:\t"+repr(argument_type)+"\n\n"

        return_string = "Returns:\n"
        for out in self.outs:
            return_name = out[1]
            return_type = out[0]
            return_string +="  Name:\t"+return_name+"\n"
            return_string +="  Type:\t"+return_type+"\n\n"

        docstring += argument_string
        docstring += return_string

        return docstring

    def __call__(self, *in_args):
        '''
        For output value, use original value
        For input arguments:
            1. If required argument is an enum, check if input argument fit requirement
            2. If required argument is "POINTER(IUIAutomationElement)", we accept UIElement object,
               get required pointer object from UIElement, and send it to function
            3. Other, no change
        '''
        args = list(in_args)
        if len(self.args) != len(args):
            LOGGER().warn("Input arguments number not match expected")
            return None
        for index, expected_arg in enumerate(self.args):
            expected_arg_type = expected_arg[0]
            if expected_arg_type == "POINTER(IUIAutomationElement)":
                #get the UIAElment
                args[index] = args[index].UIAElement
            elif expected_arg_type in UIA.UIA_enums:
                #enum should be an int value, if argument is a string, should translate to int
                if args[index] in UIA.UIA_enums[expected_arg_type]:
                    args[index] = UIA.UIA_enums[expected_arg_type][args[index]]

                if args[index] not in UIA.UIA_enums[expected_arg_type].values():
                    LOGGER().warn("Input argument not in expected value: %s" , args[index])
                    return None

        return self.function_object(*args)

class Pattern(object):
    '''Wrapper class for UIA pattern interface

    '''
    def __init__(self, UIAElement, pattern_identifier):
        self.UIAElement = UIAElement
        self.pattern_object = UIA.get_pattern_by_id(UIAElement, pattern_identifier)
        if self.pattern_object is None:
            raise DriverException("Cannot get pattern, stop init pattern object")
        self.methods = {}
        self.properties = {}
        interface_description = UIA.UIA_control_pattern_interfaces[pattern_identifier]
        for member_description in interface_description:
            flag, name, args = _unpack(*member_description)
            #do a check, see if member exist in pattern object
            #if not, skip this member
            try:
                getattr(self.pattern_object, name)
            except AttributeError:
                LOGGER().warn("%s not exist in Pattern:%s", name, pattern_identifier)
                continue

            if flag == "method":
                self.methods[name] = args
            elif flag == "property":
                self.properties[name] = args
            else:
                raise DriverException("Unrecognised flag %s" % flag)

    def __repr__(self):
        docstring = ""
        docstring += "Properties:\n"
        for property_ in self.properties.items():
            name = property_[0]
            argument = property_[1][0]
            value_type = argument[1]
            value = getattr(self.pattern_object, name)
            docstring += "#"*32+"\n"
            docstring += "  Name:\t"+name+"\n"
            docstring += "  Value Type:\t"+value_type+"\n"
            docstring += "  Value:\t"+repr(value)+"\n"

        docstring += "\nMethods:\n"
        for method_ in self.methods.items():
            name = method_[0]
            arguments = method_[1]
            docstring += "#"*32+"\n"
            docstring += "  Name:\t"+name+"\n"
            argument_string = "  Arguments:\n"
            return_string = "  Return:\n"
            for argument in arguments:
                argument_direction = argument[0]
                argument_type = argument[1]
                argument_name = argument[2]

                if argument_direction == "in":
                    if argument_type == "POINTER(IUIAutomationElement)":
                        argument_type = "UIElement"
                    elif argument_type in UIA.UIA_enums:
                        argument_type = UIA.UIA_enums[argument_type]

                    argument_string +="    Name:\t"+argument_name+"\n"
                    argument_string +="    Type:\t"+repr(argument_type)+"\n\n"
                elif argument_direction == "out":
                    return_string +="    Name:\t"+argument_name+"\n"
                    return_string +="    Type:\t"+argument_type+"\n\n"

            docstring += argument_string
            docstring += return_string

        return docstring

    def __getattr__(self, name):
        member_object = getattr(self.pattern_object, name)
        if name in self.methods:
            return Method(member_object, name, self.methods[name])
        elif name in self.properties:
            return member_object
        else:
            raise AttributeError("Attribute not exist: %s" % name)

class UIElement(object):
    '''This class defines interfaces for common UI element

    Every driver (Windows, Appium, Selenium) should implement this interfaces,
    provides independent interfaces for uplevel modules, so we transplant AXUI cross different platform

    Attributes:
        find_element:           find the first descendant element which matches parsed_identifier
        find_elements:          find all elements which match parsed_identifier
        verify:                 verify current element is valid

        get_keyboard:           class for keyboard related methods
        get_mouse:              class for mouse related methods
        get_touch:              class for touch related methods

        get_property:           get property value for current element
        get_pattern:            get pattern interface for current element
    '''
    def __init__(self, UIAElement):
        #UIAElement is a pointer to IUIAutomation
        self.UIAElement = UIAElement

    def __repr__(self):
        docstring = ""
        #generate UIA automation element properties
        docstring += "UIA automation element properties:\n"
        for identifier in UIA.UIA_automation_element_property_identifers_mapping:
            value = self.get_property(identifier)
            if value is not None:
                docstring += "  %s:\t%s\n" % (identifier, repr(value))

        docstring += "\n"
        #generate UIA control pattern availability properties
        docstring += "UIA control pattern availability properties:\n"
        for identifier in UIA.UIA_control_pattern_availability_property_identifiers_mapping:
            value = self.get_property(identifier)
            if value is not None:
                docstring += "  %s:\t%s\n" % (identifier, repr(value))

        return docstring

    def _find_by_index(self, translated_identifier, scope=UIA.UIA_wrapper.TreeScope_Descendants):
        if isinstance(translated_identifier, tuple) and len(translated_identifier) == 2:
            identifier = translated_identifier[0]
            index = translated_identifier[1]
        elif isinstance(translated_identifier, int):
            identifier = UIA.IUIAutomation_object.CreateTrueCondition()
            index = translated_identifier
        else:
            LOGGER().warn("Index identifier is wrong, get %s" , repr(translated_identifier))
            return None

        target_UIAElements = self.UIAElement.FindAll(scope, identifier)
        if index+1 > target_UIAElements.Length:
            LOGGER().warn("Find %d matched elements, index:%d out of range", target_UIAElements.Length, index)
            return None
        return UIElement(target_UIAElements.GetElement(index))

    def _find_by_UIA(self, translated_identifier, scope=UIA.UIA_wrapper.TreeScope_Descendants):
        target_UIAElement = self.UIAElement.FindFirst(scope, translated_identifier)
        if target_UIAElement == ctypes.POINTER(UIA.UIA_wrapper.IUIAutomationElement)():
            LOGGER().info("Find no element matching identifier")
            return None

        return UIElement(target_UIAElement)

    def find_element(self, parsed_identifier):
        '''find the UI element
        '''
        translated_identifier = Translater.ID_Translater(parsed_identifier).get_translated()
        if translated_identifier[0] == "Coordinate":
            return CoordinateElement(translated_identifier[1], self)
        elif translated_identifier[0] == "Index":
            return self._find_by_index(translated_identifier[1])
        elif translated_identifier[0] == "UIA":
            return self._find_by_UIA(translated_identifier[1])

    def find_elements(self, parsed_identifier):
        '''find all UI elements
        '''
        if parsed_identifier is None:
            translated_identifier = UIA.IUIAutomation_object.CreateTrueCondition()
        else:
            translated_identifier = Translater.ID_Translater(parsed_identifier).get_translated()

            if translated_identifier[0] == "Coordinate" or translated_identifier[0] == "Index":
                LOGGER().warn("find_elements method not support find by Coordinate or find by Index")
                return []
            else:
                translated_identifier = translated_identifier[1]

        scope = UIA.UIA_wrapper.TreeScope_Descendants
        UIAElementArray = self.UIAElement.FindAll(scope, translated_identifier)
        UIElements = []
        for i in range(UIAElementArray.Length):
            UIElements.append(UIElement(UIAElementArray.GetElement(i)))

        return UIElements

    def verify(self):
        '''verify UI element is still exist
        '''
        flag = True
        if self.UIAElement == ctypes.POINTER(UIA.UIA_wrapper.IUIAutomationElement)():
            flag = False

        try:
            UIAElement = self.UIAElement.FindFirst(UIA.UIA_wrapper.TreeScope_Element, UIA.IUIAutomation_object.CreateTrueCondition())
        except _ctypes.COMError:
            flag = False
            UIAElement = ctypes.POINTER(UIA.UIA_wrapper.IUIAutomationElement)()

        if UIAElement == ctypes.POINTER(UIA.UIA_wrapper.IUIAutomationElement)():
            flag = False

        if not flag:
            LOGGER().warn("Current UIAElement is no longer exist")
            return None

        return UIElement(UIAElement)

    def get_keyboard(self):
        return win32.Keyboard(self)

    def get_mouse(self):
        return win32.Mouse(self)

    def get_touch(self):
        return win32.Touch(self)

    def get_property(self, name):
        return UIA.get_property_by_id(self.UIAElement, name)

    def get_pattern(self, name):
        try:
            pattern = Pattern(self.UIAElement, name)
        except DriverException:
            pattern = None

        return pattern

    def __getattr__(self, name):
        '''
        we also support direct use name to get object
        '''
        if name == "Keyboard":
            return self.get_keyboard()
        elif name == "Mouse":
            return self.get_mouse()
        elif name == "Touch":
            return self.get_touch()
        else:
            attr = self.get_property(name)
            if attr is not None:
                return attr
            attr = self.get_pattern(name)
            if attr is not None:
                return attr
            raise AttributeError("Attribute not exist: %s" % name)

    ####################################################
    #below methods are for keyboard and mouse operation
    #####################################################

    @property
    def coordinate(self):
        #BoundingRectangle property value is (left, top, long, high)
        #CurrentBoundingRectangle value is (left, top, right, bottom)
        #use CurrentBoundingRectangle to be conpatible with Inspect.exe
        value = self.UIAElement.CurrentBoundingRectangle
        return value.left, value.top, value.right, value.bottom

    def set_focus(self):
        '''set foucs this element

        Will bring this element to the front, used by Keyboard, Mouse, Touch

        Arguments:
        Returns:
        '''
        try:
            self.UIAElement.SetFocus()
        except _ctypes.COMError:
            LOGGER().warn("SetFocus fail on current element, maybe due to this element not support SetFocus")
            #self.parent.SetFocus()

    def get_clickable_point(self):
        '''Retrieves a point on the element that can be clicked.

        Arguments:
        Returns:
            (x, y) coordinate if can get clickable point
            None if cannot get clickable point
        '''
        point, flag = self.UIAElement.GetClickablePoint()
        if flag:
            return point.x, point.y
        else:
            #use coordinate
            x = (self.coordinate[0]+self.coordinate[2])/2
            y = (self.coordinate[1]+self.coordinate[3])/2
            return x, y

class Root(UIElement):
    '''
    root is the entry point to interact with UI
    like desktop of windows UIA, web browser of web driver API

    This class defines interfaces for root element

    Every driver (Windows, Appium, Selenium) should implement this interfaces,
    provides independent interfaces for uplevel modules, so we transplant AXUI cross different platform

    Attributes:
        start:                  start root element
        stop:                   stop root element
        screenshot:             take a screen shot for root element

        find_element:           find the first descendant element which matches parsed_identifier
        find_elements:          find all elements which match parsed_identifier
        verify:                 verify current element is valid

        get_keyboard:           class for keyboard related methods
        get_mouse:              class for mouse related methods
        get_touch:              class for touch related methods

        get_property:           get property value for current element
        get_pattern:            get pattern interface for current element
    '''
    def __init__(self):
        self.UIAElement = None

    def start(self, **kwargs):
        self.UIAElement = UIA.IUIAutomation_object.GetRootElement()

    def stop(self, **kwargs):
        self.UIAElement = None

    def screenshot(self, filename):
        return screenshot.screenshot(filename)

    def find_element(self, parsed_identifier):
        '''find the UI element
        root find should only find in the first level to avoid search in all UI
        '''
        translated_identifier = Translater.ID_Translater(parsed_identifier).get_translated()
        if translated_identifier[0] == "Coordinate":
            return CoordinateElement(translated_identifier[1], self)
        elif translated_identifier[0] == "Index":
            return self._find_by_index(translated_identifier[1], scope=UIA.UIA_wrapper.TreeScope_Children)
        elif translated_identifier[0] == "UIA":
            return self._find_by_UIA(translated_identifier[1], scope=UIA.UIA_wrapper.TreeScope_Children)

    def find_elements(self, parsed_identifier):
        '''find all matched element
        root find should only find in the first level to avoid search in all UI
        '''
        if parsed_identifier is None:
            translated_identifier = UIA.IUIAutomation_object.CreateTrueCondition()
        else:
            translated_identifier = Translater.ID_Translater(parsed_identifier).get_translated()
            if translated_identifier[0] == "Coordinate" or translated_identifier[0] == "Index":
                LOGGER().warn("find_elements method not support find by Coordinate or find by Index")
                return []
            else:
                translated_identifier = translated_identifier[1]

        scope = UIA.UIA_wrapper.TreeScope_Children
        UIAElementArray = self.UIAElement.FindAll(scope, translated_identifier)
        UIElements = []
        for i in range(UIAElementArray.Length):
            UIElements.append(UIElement(UIAElementArray.GetElement(i)))
        return UIElements

    def verify(self):
        '''verify UI element is still exist
        for root element just check if UIAElement is initialized
        '''
        if self.UIAElement is None:
            return None
        else:
            return self

class CoordinateElement(UIElement):
    '''
    coordinate element is for coordinate identifier
    functions are limited, only support keyboard, mouse and touch operation
    '''
    def __init__(self, coordinate, parent_element):
        #coordinate should be like:
        #"(left, top, right, bottom)", "[left, top, right, bottom]", "left, top, right, bottom"
        coordinate_list = coordinate.strip("(").strip(")").strip("[").strip("]").split(",")
        try:
            left, top, right, bottom = [int(value) for value in coordinate_list]
            if left > right or top > bottom:
                raise ValueError()
        except ValueError:
            raise ValueError("Coordinate should contain 4 digitals, get:%s" % repr(coordinate))

        self.coordinate = (left, top, right, bottom)
        self.parent_element = parent_element

    def __repr__(self):
        docstring = "Coordinate element for coordinate: %s" % repr(self.coordinate)
        return docstring

    def find_element(self, parsed_identifier):
        #TODO maybe we should let coordinate element have children
        raise DriverException("coordinate element should not have children")

    def find_elements(self, parsed_identifier):
        #TODO maybe we should let coordinate element have children
        raise DriverException("coordinate element should not have children")

    def verify(self):
        return self

    def set_focus(self):
        '''set foucs this element

        Will bring this element to the front, used by Keyboard, Mouse, Touch

        Arguments:
        Returns:
        '''
        #usually, a coordinate element will be set focus if its parent is set focus
        return self.parent_element.SetFocus()

    def get_clickable_point(self):
        '''Retrieves a point on the element that can be clicked.

        Arguments:
        Returns:
            (x, y) coordinate if can get clickable point
            None if cannot get clickable point
        '''
        x = (self.coordinate[0]+self.coordinate[2])/2
        y = (self.coordinate[1]+self.coordinate[3])/2
        return x, y

    def get_property(self, name):
        raise DriverException("coordinate element don't support property")

    def get_pattern(self, name):
        raise DriverException("coordinate element don't support pattern")

    def __getattr__(self, name):
        raise AttributeError("Attribute not exist for coordinate element: %s" % name)
