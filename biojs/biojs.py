from jsobject import JSObject
import ipywidgets as widgets
from IPython.display import display, Javascript
import os, json

#Push biojs scripts to front end
with open(os.path.join(os.path.split(__file__)[0], 'js/biojs-require.js'), 'r') as f:
    display(Javascript(data=f.read()))

window = JSObject()
#Javascript console for testing purposes
console = window.console
console.log('Hello from Python')

#BaseClass to derive further classes as per the requirements of biojs components
class BaseClass(object):
    def __init__(self, classtype):
        self.type = classtype

# function to create classes dynamically so that objects could be created
def classFactory(name, argnames, BaseClass=BaseClass):
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            if key not in argnames:
                raise TypeError("Argument %s not valid for %s" %(key, self.__class__.__name__))
            setattr(self, key, value)
        BaseClass.__init__(self, name[:-len("class")])
    newClass = type(name, (BaseClass,), {"__init__":__init__})
    return newClass


#Code to create new classes for biojs components

# Fetch names of the installed biojs components
with open(os.path.join(os.path.split(__file__)[0], 'biojs-packages.json'), 'r') as f:
    biojs_packages = json.load(f)

for package in biojs_packages:
    print(package['package-name'])
    className = package['package-name']
    globals()[className] = classFactory(className)
