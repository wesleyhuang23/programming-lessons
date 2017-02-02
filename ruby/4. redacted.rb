#Redacted
puts "please type a response"
text = gets.chomp

puts "the word you want to redact"
redacted = gets.chomp

#split method - splits a string and returns an array
words = text.split(" ")
#each is kind of like each, map create new array in JS
words.each do |word|
    if word == redacted
        print "REDACTED"
    else
        print word + " "
    end
end