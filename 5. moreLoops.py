#MORE LOOPS
#while loop
if count < 10:
    print "Hello, I am an if statement and count is", count
    
while count < 10:
    print "Hello, I am a while and count is", count
    count += 1



#while with condition
loop_condition = True

while loop_condition:
    print "I am a loop"
    loop_condition = False


#counting to a specific number
num = 1

while num < 11:  # Fill in the condition
    print num * num
    num += 1

#using ==
choice = raw_input('Enjoying the course? (y/n)')


while choice == "n":  # Fill in the condition (before the colon)
    choice = raw_input("Sorry, I didn't catch that. Enter again: ")
    if choice == 'y':
        print "that's what I like to hear!"




#While Else example
import random

print "Lucky Numbers! 3 numbers will be generated."
print "If one of them is a '5', you lose!"

count = 0
while count < 3:
    num = random.randint(1, 6)
    print num
    if num == 5:
        print "Sorry, you lose!"
        break
    count += 1
else:
    print "You win!"




#While else:
from random import randint

# Generates a number from 1 through 10 inclusive
random_number = randint(1, 10)

guesses_left = 3

while guesses_left > 0:
    guess = int(raw_input("Your guess: "))
    if guess == random_number:
        print "You win!"
        break
    guesses_left -= 1 # decrements guesses left by one until the while clause no longer is true then the else will fire
else:
    print "You lose."



#While with range
print "Counting..."

for i in range(20):
    print i

#print every letter in a string
#-do a stright up for loop on a string
thing = "spam!"

for c in thing:
    print c

word = "eggs!"

# Your code here!
for letter in word:
    print letter



#changing characters use a comma at the end of your print to print as original string
phrase = "A bird in the hand..."

# Add your for loop
for char in phrase:
    if char == 'A' or char == 'a':
        print 'X',
    else:
        print char,

#enumerate
#-sets the value variable to number
choices = ['pizza', 'pasta', 'salad', 'nachos']

print 'Your choices are:'
for index, item in enumerate(choices):
        print index + 1, item


#zip
#-compares two lists and stops at the shortest list
list_a = [3, 9, 17, 15, 19]
list_b = [2, 4, 8, 10, 30, 40, 50, 60, 70, 80, 90]

for a, b in zip(list_a, list_b):
    # Add your code here!
    if a > b:
        print a
    elif b > a:
        print b

#FOR ELSE loop
fruits = ['banana', 'apple', 'orange', 'tomato', 'pear', 'grape']

print 'You have...'
for f in fruits:
    if f == 'tomato':
        print 'A tomato is not a fruit!' # (It actually is.)
        break
    print 'A', f
else:
    print 'A fine selection of fruits!'

#example 2
fruits = ['banana', 'apple', 'orange', 'tomato', 'pear', 'grape']

print 'You have...'
for f in fruits:
    print 'A', f
else:
    print 'A fine selection of fruits!'

#my example
cart = ['cheese', 'bread', 'soy sauce', 'bacon']

for food in cart:
    if food == 'bacon':
        print "Good choice"
        break
else:
    print "you forgot the bacon"