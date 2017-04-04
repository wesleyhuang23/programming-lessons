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




#MORE lists in ENTRIES or DICTRIONARIES
lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}
alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}
tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}

students = [lloyd, alice, tyler]

for student in students:
    print student['name']
    print student['homework']
    print student['quizzes']
    print student['tests']

#-printing students dictionary

#average function
#-use built in functions
def average(numbers):
    total = sum(numbers)
    total = float(total)
    total = total / len(numbers)
    return total

#weighted items
#-takes in the average and then multiplies the weight and sums them
def get_average(student):
    homework = average(student["homework"])
    quizzes = average(student["quizzes"])
    tests = average(student["tests"])
    return 0.6 * tests + 0.3 * quizzes + 0.1 * homework

#getting the letter grade
def get_letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

get_letter_grade(lloyd)

#getting the average of the class
#-loops through to get their average by invoking the get average function and then pushes it into the results list
def get_class_average(students):
    results = []
    for student in students:
        results.append(get_average(student))
    return sum(results) / len(results)

#print the results
print get_class_average(students)
print get_letter_grade(get_class_average(students))