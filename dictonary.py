'''
A Python dictionary is a collection of items, similar to lists and tuples. However, unlike lists and tuples, each item in a dictionary is a key-value pair
We create a dictionary by placing key: value pairs inside curly brackets {}, separated by commas.
Dictionary keys must be immutable, such as tuples, strings, integers, etc. We cannot use mutable (changeable) objects such as lists as keys
We can also create a dictionary using a Python built-in function dict(). To learn more, visit Python dict().
'''
# creating a dictionary
country_capitals = {
  "Germany": "Berlin", 
  "Canada": "Ottawa", 
  "England": "London"
}

# printing the dictionary
print(country_capitals)

# Valid and Invalid Dictionaries

# valid dictionary
# integer as a key
my_dict = {1: "one", 2: "two", 3: "three"}

# valid dictionary
# tuple as a key
my_dict = {(1, 2): "one two", 3: "three"}

# invalid dictionary
# Error: using a list as a key is not allowed
my_dict = {1: "Hello", [1, 2]: "Hello Hi"}

# valid dictionary
# string as a key, list as a value
my_dict = {"USA": ["Chicago", "California", "New York"]}

country_capitals = {
  "Germany": "Berlin", 
  "Canada": "Ottawa", 
  "England": "London"
}

# access the value of keys
print(country_capitals["Germany"])    # Output: Berlin
print(country_capitals["England"])    # Output: London

country_capitals = {
  "Germany": "Berlin", 
  "Canada": "Ottawa", 
}

# add an item with "Italy" as key and "Rome" as its value
country_capitals["Italy"] = "Rome"

print(country_capitals)

country_capitals = {
  "Germany": "Berlin", 
  "Canada": "Ottawa", 
}

# delete item having "Germany" key
del country_capitals["Germany"]

print(country_capitals)

country_capitals = {
  "Germany": "Berlin", 
  "Italy": "Naples", 
  "England": "London"
}

# change the value of "Italy" key to "Rome"
country_capitals["Italy"] = "Rome"

print(country_capitals)

country_capitals = {"England": "London", "Italy": "Rome"}

# get dictionary's length
print(len(country_capitals))   # Output: 2

numbers = {10: "ten", 20: "twenty", 30: "thirty"}

# get dictionary's length
print(len(numbers))            # Output: 3

countries = {}

# get dictionary's length
print(len(countries))          # Output: 0

'''
Python Dictionary Methods
pop()	Removes the item with the specified key.
update()	Adds or changes dictionary items.
clear()	Remove all the items from the dictionary.
keys()	Returns all the dictionary's keys.
values()	Returns all the dictionary's values.
get()	Returns the value of the specified key.
popitem()	Returns the last inserted key and value as a tuple.
copy()	Returns a copy of the dictionary.
'''