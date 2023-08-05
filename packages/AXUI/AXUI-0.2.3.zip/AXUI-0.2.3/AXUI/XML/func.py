
from AXUI.logger import LOGGER

class _Step(object):
    '''represent one step element in the function element
    '''
    def __init__(self, xml_element, app_map):
        self.xml_element = xml_element
        self.type = xml_element.attrib["type"]
        self.command = xml_element.attrib["cmd"]
        try:
            self.app_map_name = xml_element.attrib["app_map"]
        except KeyError:
            self.app_map_name = ""
        
        if self.app_map_name:
            self.app_map = app_map.get_include_app_map_by_name(self.app_map_name)
        else:
            self.app_map = app_map
        
    def run(self):
        if self.type == "GUI":
            LOGGER().debug("run gui command: %s" , self.command)
            self.app_map.gui_execute(self.command)
        elif self.type == "CLI":
            LOGGER().debug("run cli command: %s" , self.command)
            self.app_map.cli_execute(self.command)
        else:
            raise ValueError("step type must be GUI or CLI, get: %s" % self.type)

class Func(object):
    '''represent a function element in the XML
    
    attributes:
        run:        run this function
    
    '''
    def __init__(self, xml_element, app_map):
        self.xml_element = xml_element
        self.app_map = app_map
        self.name = xml_element.attrib["name"]
        self.description = xml_element.attrib["description"]
        self.steps = []
        #parse all included steps
        self._parse_steps()
    
    def __repr__(self):
        return "Func instance for %s" % self.name
    
    def _parse_steps(self):
        for step_xml_element in self.xml_element.findall("AXUI:step", namespaces={"AXUI":"AXUI"}):
            self.steps.append(_Step(step_xml_element, self.app_map))
            
    def run(self):
        for step in self.steps:
            step.run()
            
        
