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