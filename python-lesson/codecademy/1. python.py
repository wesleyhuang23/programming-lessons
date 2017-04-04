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



#function review
def hotel_cost(nights):
    return nights * 140
    
def plane_ride_cost(city):
    if city == "Charlotte":
        return 183
    elif city == "Tampa":
        return 220
    elif city == "Pittsburgh":
        return 222
    elif city == "Los Angeles":
        return 475

def rental_car_cost(days):
    if days < 3:
        return days * 40
    elif days >= 3 and days < 7:
        return days * 40 - 20
    elif days >= 7:
        return days * 40 - 50

def trip_cost(city, days, spending_money):
    sum = rental_car_cost(days) + hotel_cost(days) + plane_ride_cost(city) + spending_money
    print trip_cost("Los Angeles", 5, 600)
    return sum






#LIST AND DICTIONARIES
#instead of arrays they are called lists with indicies like an array
zoo_animals = ["pangolin", "cassowary", "sloth", "pig"];

if len(zoo_animals) > 3:
	print "The first animal at the zoo is the " + zoo_animals[0]
	print "The second animal at the zoo is the " + zoo_animals[1]
	print "The third animal at the zoo is the " + zoo_animals[2]
	print "The fourth animal at the zoo is the " + zoo_animals[3]

#indicies
numbers = [5, 6, 7, 8]

print "Adding the numbers at indices 0 and 2..."
print numbers[0] + numbers[2]
print "Adding the numbers at indices 1 and 3..."
# Your code here!
print numbers[1] + numbers[3]

#reassign them just like javascript
zoo_animals = ["pangolin", "cassowary", "sloth", "tiger"]
# Last night our zoo's sloth brutally attacked 
#the poor tiger and ate it whole.

# The ferocious sloth has been replaced by a friendly hyena.
zoo_animals[2] = "hyena"

# What shall fill the void left by our dear departed tiger?
# Your code here!
zoo_animals[3] = "Taylor Swift"




#Append
#-like push in javascript adding one element to the end of the array or list
suitcase = [] 
suitcase.append("sunglasses")

# Your code here!
suitcase.append("chicken")
suitcase.append("pig")
suitcase.append("beer")

list_length = len(suitcase) # Set this to the length of suitcase

print "There are %d items in the suitcase." % (list_length)
print suitcase



#Slicing
#-begin with the indicy you want and them the one you want to end plus 1 and it will return the range between them
suitcase = ["sunglasses", "hat", "passport", "laptop", "suit", "shoes"]

first  = suitcase[0:2]  # The first and second items (index zero and one)
middle = suitcase[2:4]  # Third and fourth items (index two and three)
last   = suitcase[4:6]  # The last two items (index four and five)

#slicing strings
animals = "catdogfrog"
cat  = animals[:3]   # The first three characters of animals
dog  = animals[3:6]  # The fourth through sixth characters
frog = animals[6:10]  # From the seventh character to the end

#.index()
animals = ["aardvark", "badger", "duck", "emu", "fennec fox"]
duck_index = animals.index("duck")    # Use index() to find "duck"

# Your code here!
animals.insert(duck_index, "cobra")



#FOR IN LOOP
#-for is the new variable and the in the original array you want each element to be performed on
my_list = [1,9,3,8,5,7]

for number in my_list:
    # Your code here
    print 2 * number

#sort and append in loop
start_list = [5, 3, 1, 2, 4]
square_list = []

# Your code here!
for x in start_list:
    square_list.append(x ** 2)
    square_list.sort()

print square_list



#KEY VALUES PAIRS
#-also use currly brackets
# Assigning a dictionary with three key-value pairs to residents:
residents = {'Puffin' : 104, 'Sloth' : 105, 'Burmese Python' : 106}

print residents['Puffin'] # Prints Puffin's room number

# Your code here!
print residents['Sloth']
print residents['Burmese Python']




#OBJECTS or ENTRIES
menu = {} # Empty dictionary
menu['Chicken Alfredo'] = 14.50 # Adding new key-value pair
print menu['Chicken Alfredo']

# Your code here: Add some dish-price pairs to menu!
menu['pig'] = 100
menu['taylor swift'] = 1000
menu['hotpocket'] = 300

print "There are " + str(len(menu)) + " items on the menu."
print menu


# key - animal_name : value - location 
zoo_animals = { 
'Unicorn' : 'Cotton Candy House',
'Sloth' : 'Rainforest Exhibit',
'Bengal Tiger' : 'Jungle House',
'Atlantic Puffin' : 'Arctic Exhibit',
'Rockhopper Penguin' : 'Arctic Exhibit'}
# A dictionary (or list) declaration may break across multiple lines

# Removing the 'Unicorn' entry. (Unicorns are incredibly expensive.)
del zoo_animals['Unicorn']

# Your code here!
del zoo_animals['Sloth']
del zoo_animals['Bengal Tiger']
zoo_animals['Rockhopper Penguin'] = 'Ham'

print zoo_animals

#remove
backpack = ['xylophone', 'dagger', 'tent', 'bread loaf']
backpack.remove('dagger')

#reassigning lists and entries
inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'], # Assigned a new list to 'pouch' key
    'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
}

# Adding a key 'burlap bag' and assigning a list to it
inventory['burlap bag'] = ['apple', 'small ruby', 'three-toed sloth']

# Sorting the list found under the key 'pouch'
inventory['pouch'].sort() 

# Your code here
inventory['pocket'] = ['seashell', 'strange berry', 'lint']
inventory['backpack'].sort()
inventory['backpack'].remove('dagger')
inventory['gold'] = inventory['gold'] + 50