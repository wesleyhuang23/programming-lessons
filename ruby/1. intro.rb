#INTRO TO RUBY
my_num = 25 
my_boolean = true 
my_string = "Ruby"  

#puts and print
#-puts put things on a new line
print "cheese"
puts "eggs"

#Everything in ruby is an object

#length
"Wesley Huang".length

#reverse
"Wesley".reverse

#up and down case
puts "Wesley".upcase #prints all upper case
puts "Wesley".downcase #prints all lower case

#comments same as python

# for single line comments

=begin
multiline comments
=end

#MORE MATH
sum = 13 + 379
product = 923 * 15
quotient = 13209 / 17

#everything in Ruby is an object so you can call multiple methods
name = "Wesley".downcase.reverse.upcase
name.method1.method2.method3


#gets.chomp is prompt
#{} is reading the value of the variable
#! will change the actual value without having you to put it in a new variable
firstname = "Sam"
puts "#{firstname}"
puts "my name is #{first_name}"
.capitalize!

lastname = "Smith"
puts "#{lastname}"
puts "my last name is #{last_name}"
.capitalize!

city = "Los Angeles"
puts "#{city}"
puts "I live in #{city}"
.capitalize!

state = "California"
puts "#{state}"
puts "I live in the city of #{state}"
.upcase!

#if statement
#-straight up write remember to end at the bottom
if 2 > 1
    print "This is easy"
elsif 1 < 2
    print "This is not fun"
else
    print "Too bad"
end

#unless
hungry = false

unless hungry
  puts "I'm writing Ruby programs!"
else
  puts "Time to eat!"
end

#asssignment operator
is_true = 2 != 3
is_false = 2 == 3

#Booleans
# boolean_1 = 77 < 78 && 77 < 77
boolean_1 = false

# boolean_2 = true && 100 >= 100
boolean_2 = true

# boolean_3 = 2**3 == 8 && 3**2 == 9
boolean_3 = true

#double comparing
# boolean_1 = (3 < 4 || false) && (false || true)
boolean_1 = true

# boolean_2 = !true && (!true || 100 != 5**2)
boolean_2 = false

# boolean_3 = true || !(true || false)
boolean_3 = true

#unless
#-will not print unless problem is false, WILL NOT FIRE if true
problem = true
print "I am ready" unless problem