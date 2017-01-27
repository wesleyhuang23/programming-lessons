#FUNCTIONS

#FUNCTION IMPORTS
from math import sqrt #import individual method

from module import * #import whole library using *
from math import *

#code that shows everything in the imports
import math            # Imports the math module
everything = dir(math) # Sets everything to a list of things from math
print everything       # Prints 'em all!

"""['__doc__', '__name__', '__package__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'copysign', 'cos', 'cosh', 'degrees', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'hypot', 'isinf', 'isnan', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'modf', 'pi', 'pow', 'radians', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'trunc']"""

#BEYOND STRING
def biggest_number(*args):
    print max(args)
    return max(args)
    
def smallest_number(*args):
    print min(args)
    return min(args)

def distance_from_zero(arg):
    print abs(arg)
    return abs(arg)


biggest_number(-10, -5, 5, 10)
smallest_number(-10, -5, 5, 10)
distance_from_zero(-10)

#max() => max number of what is passed in
maximum = max(1,2,3)
print maximum

#min() => minimum number passed in
minimum = min(5,24,235)
print minimum

#abs() => makes whatever number positive
absolute = abs(-129423)
print absolute

#type() => print what the data type of what is passed in
print type(33)
print type(3.2)
print type("eat")

"""
<type 'int'>
<type 'float'>
<type 'str'>
"""

#function review
def shut_down(s):
    if(s == "yes"):
        return "Shutting down"
    elif(s == "no"):
        return "Shutdown aborted"
    else:
        return "Sorry"

#modules
from math import *
print math.sqrt(13689)

#built in functions
def distance_from_zero(n):
    if type(n) == int or type(n) == float:
        return abs(n)
    else:
        return "Nope"