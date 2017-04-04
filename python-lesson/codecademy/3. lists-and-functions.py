#LISTS AND FUNCTIONS
#-overwriting the second element with new number
n = [1, 3, 5]
# Do your multiplication here
n[1] = n[1] * 5
print n

#appending
n = [1, 3, 5]
# Append the number 4 here
n.append(4)
print n

#removing elements from a list
n = [1, 3, 5]
# Remove the first item in the list here
n.pop(0)
print n

#-there is also del and remove
#-pop choose indicy and remove
#-remove will remove which order so 
remove(1) #will remove the first element not the indicy
#-del will remove the specific element so you need to give it indicy like 
del(n[1])

#Functions
m = 5
n = 13
# Add add_function here!
def add_function(x, y):
    return x + y


print add_function(m, n)

#string functions
n = "Hello"
# Your function here!
def string_function(s):
    return s + 'world'

#THE FOR LOOPS WITH RANGE
n = [3, 5, 7]

def double_list(x):
    for i in range(0, len(x)):
        x[i] = x[i] * 2
    return x
# Don't forget to return your new list!

print double_list(n)

#RANGE
range(stop)
range(start, stop)
range(start, stop, step)

def my_function(x):
    for i in range(0, len(x)):
        x[i] = x[i] * 2
    return x

print my_function([0, 1, 2]) # Add your range between the parentheses!

#summing numbers using for range loop
n = [3, 5, 7]

def total(numbers):
    results = 0
    for num in range(0, len(numbers)):
        results = results + numbers[num]
    return results

#CONCATNATING STRINGS
n = ["Michael", "Lieberman"]
# Add your function here
def join_strings(word):
    result = ""
    for i in range(0, len(word)):
        result = result + word[i]
    return result


print join_strings(n)

#JOINTING LISTS
#- will make it into one list
m = [1, 2, 3]
n = [4, 5, 6]

# Add your code here!
def join_lists(x, y):
    return x + y

print join_lists(m, n)
# You want this to print [1, 2, 3, 4, 5, 6]

#PRINTING lists within lists making it into one list
n = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]
# Add your function here
def flatten(lists):
    results = []
    for i in range(0, len(lists)):
        for j in range(0, len(lists[i])):
            results.append(lists[i][j])
    return results


print flatten(n)