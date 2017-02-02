#DATA STRUCTURES
demo_array = [100, 200, 300, 400, 500]
#print third
print demo_array[2]

#store strings
string_array = ["eat", "cheese"]

#array of arrays
multi_d_array = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
multi_d_array.each { |x| puts "#{x}\n" }

#HASH is like an object use => instead of : in JS
my_hash = { "name" => "Eric",
  "age" => 26,
  "hungry?" => true
}

puts my_hash["name"]
puts my_hash["age"]
puts my_hash["hungry?"]

#hase.new to create new hash
pets = Hash.new()

#assign key value pair
pets = Hash.new()
pets["dog"] = "max"



#iteration of arrays and hashes
friends = ["Milhouse", "Ralph", "Nelson", "Otto"]

family = { "Homer" => "dad",
  "Marge" => "mom",
  "Lisa" => "sister",
  "Maggie" => "sister",
  "Abe" => "grandpa",
  "Santa's Little Helper" => "dog"
}

friends.each { |x| puts "#{x}" }
family.each { |x, y| puts "#{x}: #{y}" }

#array iteration
languages = ["HTML", "CSS", "JavaScript", "Python", "Ruby"]
languages.each { |str| puts str }

#Subarrays
s = [["ham", "swiss"], ["turkey", "cheddar"], ["roast beef", "gruyere"]]

s.each do | sub_array |
  sub_array.each do | y |
    puts y
  end
end

#iterating through hashes
secret_identities = {
  "The Batman" => "Bruce Wayne",
  "Superman" => "Clark Kent",
  "Wonder Woman" => "Diana Prince",
  "Freakazoid" => "Dexter Douglas"
}

secret_identities.each do |hero, name|
    puts "#{hero}: #{name}"
end
  
#print lunch
lunch_order = {
  "Ryan" => "wonton soup",
  "Eric" => "hamburger",
  "Jimmy" => "sandwich",
  "Sasha" => "salad",
  "Cole" => "taco"
}

lunch_order.each { |name, food| puts food }
#ruby knows the order so give key value order
