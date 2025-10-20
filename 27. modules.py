# MODULES
# Module is a file containing python code, it can define functions, classes, variables

import greet
greet.greet("Vivek Goud") # When using a function from a module, syntax: module_name.function_name

# You can also import specific functions from a module
from greet import wish 
greet.wish("Vivek Goud")

# ---------------------------------------------------------

# VARIABLES IN MODULES
a = greet.details["city"]
print(a)

# ---------------------------------------------------------

# RENAMING A MODULE WHILE IMPORTING
import greet as gr
a = gr.details["age"]
print(a)

# ---------------------------------------------------------

# BUILT-IN MODULES

# MATH MODULE
import math 
print(math.pi)

# PLATFORM MODULE
import platform
x=platform.system()
print(x)

# dir() FUNCTION
# dir() function is used to list all functions or variables of that module
c = dir(math)
print(c)