
import os

config_section="XML"
default_configs={ "app_map_location": os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "example"),
                  "schema_location": os.path.join(os.path.dirname(os.path.abspath(__file__)), "schemas"),
                  "timeout": 5,
                  "screenshot_location": os.path.dirname(os.path.abspath(__file__)),
                  "screenshot_on_failure": "False",
                }

AppMapLocation=default_configs["app_map_location"]
SchemaLocation=default_configs["schema_location"]
TimeOut=default_configs["timeout"]
ScreenshotLocation=default_configs["screenshot_location"]
ScreenshotOnFailure=default_configs["screenshot_on_failure"]

def config(configs=None):
    '''call back function used by config module
    set the global variables according to configuration
    '''
    if configs is None:
        configs = default_configs
    
    global AppMapLocation
    global SchemaLocation
    global TimeOut
    global ScreenshotLocation
    global ScreenshotOnFailure
    AppMapLocation=configs["app_map_location"]
    SchemaLocation=configs["schema_location"]
    TimeOut=configs["timeout"]
    ScreenshotLocation=configs["screenshot_location"]
    ScreenshotOnFailure=configs["screenshot_on_failure"]

#used by config module
__all__=["config_section", "default_configs", "config"]
    
def query_app_map_file(app_map_file):
    '''search app_map_file in AppMapLocation, return abs path if found 
    Arguments:
        app_map_file: app_map file name
    Returns:
        abs_app_map_file: abs path of the app_map file
    '''
    if os.path.isabs(app_map_file) and os.path.isfile(app_map_file):
        return app_map_file
    else:
        basename = os.path.basename(app_map_file)
        for root, dirs, files in os.walk(AppMapLocation):
            for file_ in files:
                if file_ == basename:
                    return os.path.join(root, basename)
        raise ValueError("%s not found in %s" % (app_map_file, AppMapLocation))
    
def query_schema_file(schema_file):
    '''search schema_file in SchemaLocation, return abs path if found 
    Arguments:
        schema_file: schema file name
    Returns:
        abs_schema_file: abs path of the schema file
    '''
    if os.path.isabs(schema_file) and os.path.isfile(schema_file):
        return schema_file
    else:
        basename = os.path.basename(schema_file)
        for root, dirs, files in os.walk(SchemaLocation):
            for file_ in files:
                if file_ == basename:
                    return os.path.join(root, basename)
        raise ValueError("%s not found in %s" % (schema_file, SchemaLocation))
    
def query_timeout():
    '''query timeout from config
    Return: timeout set in config
    '''
    return TimeOut
    
def query_screenshot_location():
    '''query screenshot_location from config
    Return: screenshot_location
    '''
    if not os.path.isdir(ScreenshotLocation):
        os.makedirs(ScreenshotLocation)
        
    return ScreenshotLocation
    
def query_screenshot_on_failure():
    '''query screenshot_on_failure from config
    '''
    results = {"True":True, "False":False}
    
    if ScreenshotOnFailure in results:
        return results[ScreenshotOnFailure]
    else:
        #use default
        return results[default_configs["screenshot_on_failure"]]
