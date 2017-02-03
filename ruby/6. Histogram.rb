#Historgram
puts "Text Please"
text = gets.chomp

words = text.split(' ')

frequencies = Hash.new(0)

words.each { |word| frequencies[word] += 1 }
#Sorting the hash
frequencies.sort_by do |word, num|
    num
    frequencies = frequencies.sort_by { |k, v| v}
    frequencies.reverse!
end
#iterate though each key value of the hash
frequencies.each do |word, num|
    puts word + " " + num.to_s
end

#full example
puts "Text Please"
text = gets.chomp

words = text.split(' ')

frequencies = Hash.new(0)

words.each { |word| frequencies[word] += 1 }

frequencies.sort_by do |word, num|
    num
    frequencies = frequencies.sort_by { |k, v| v}
    frequencies.reverse!
end

frequencies.each do |word, num|
    puts word + " " + num.to_s
end
