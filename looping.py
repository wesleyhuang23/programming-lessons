#FOR IN LOOP
names = ["Adam","Alex","Mariah","Martine","Columbus"]

for name in names:
    print name

#for entries
webster = {
	"Aardvark" : "A star of a popular children's cartoon show.",
    "Baa" : "The sound a goat makes.",
    "Carpet": "Goes on the floor.",
    "Dab": "A small amount."
}

# Add your code below!
for key in webster:
    print webster[key]

#with conditional
#-dont forget :
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

for num in a:
    if num % 2 == 0:
        print num

#counting number of things
def fizz_count(x):
    count = 0
    for string in x:
        if string == 'fizz':
            count = count + 1
    return count

#printing strings
for letter in "Codecademy":
    print letter
    
# Empty lines to make the output pretty
print
print

word = "Programming is fun!"

for letter in word:
    # Only print out the letter i
    if letter == "i":
        print letter

#for in loop of multiple entires
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}

for key in prices:
    print key
    print "price: %s" % prices[key]
    print "stock: %s" % stock[key]

total = 0

for key in prices:
    print prices[key] * stock[key]
    total = total + prices[key] * stock[key]
    print total



#adding stuff in a list
shopping_list = ["banana", "orange", "apple"]

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15
}
    
prices = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
}

# Write your code below!
def compute_bill(food):
    total = 0
    for key in food:
        if stock[key] > 0:
            total = total + prices[key]
        stock[key] = stock[key] - 1
    return total