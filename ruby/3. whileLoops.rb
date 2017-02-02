#While Loops
i = 0
while i < 5
  puts i
  # Add your code here!
  i += 1
end

#until - until a value reaches your condition
counter = 1
until counter == 10
  puts counter
  # Add code to update 'counter' here!
  counter += 1
end

#for in Loop
for num in 1...10
  puts num
end

#or

for num in 1..15
  puts num
end

#example
for num in 1 .. 20
    puts num
end

#ITERATOR
#loop use brake if
i = 20
loop do
  i -= 1
  print "#{i}"
  break if i <= 0
end

#next
#-skip if a condition is met
i = 20
loop do
  i -= 1
  next if i % 2 != 0
  print "#{i}"
  break if i <= 0
end

#Arrays

array = [1,2,3,4,5]

array.each do |x|
  x += 10
  print "#{x}"
end

#example
odds = [1,3,5,7,9]

# Add your code below!
odds.each do |num|
    print num * 2
end

#ITERATOR
10.times { print "bacon" }

#until practice
i = 1
until i == 51 do
    print i
    i += 1
end

#for in practice
for i in 1..50
    print i
end

#loop in a loop
i = 0
loop do
    i += 1
    print "Ruby!"
    break if i == 30
end