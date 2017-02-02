#thith means war
print "please type something"
user_input = gets.chomp
user_input.downcase!

if user_input.include? "s"
    puts user_input.gsub!(/s/, "th")
else
    print "There were no s'yes"
end

#gsub! - takes 2 arguments, what you want to replace and replace with what?
#include? - if statment checking if true or not.