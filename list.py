# We create a list by placing elements inside square brackets [], separated by commas.
 # a list of three elements
ages = [19, 26, 29]
print(ages)

# Output: [19, 26, 29]

# List Items of Different Types

# We can use the built-in list() function to convert other iterables (strings, dictionaries, tuples, etc.) to a list.

x = "axz"

# convert to list
result = list(x)

print(result)  # ['a', 'x', 'z']
'''
List Characteristics
Ordered - They maintain the order of elements.
Mutable - Items can be changed after creation.
Allow duplicates - They can contain duplicate values.
'''

languages = ['Python', 'Swift', 'C++']

# Access the first element
print(languages[0])   # Python

# Access the third element
print(languages[2])   # C++

# Python also supports negative indexing. The index of the last element is -1, the second-last element is -2, and so on

# Access list value at index 2
print(languages[-1])

'''slicing in list In Python, it is possible to access a section of items from the list using the slicing operator :

'''

my_list = ['p', 'r', 'o', 'g', 'r', 'a', 'm']

# items from index 2 to index 4
print(my_list[2:5])

# items from index 5 to end
print(my_list[5:])

# items beginning to end
print(my_list[:])

# Add Elements to a Python List
fruits = ['apple', 'banana', 'orange']
print('Original List:', fruits)

# using append method 
fruits.append('cherry')

print('Updated List:', fruits)

#Add Elements at the Specified Index

fruits = ['apple', 'banana', 'orange']
print("Original List:", fruits) 

# insert 'cherry' at index 2
fruits.insert(2, 'cherry')

print("Updated List:", fruits)

# Change List Items

colors = ['Red', 'Black', 'Green']
print('Original List:', colors)

# changing the third item to 'Blue'
colors[2] = 'Blue'

print('Updated List:', colors)

#Remove an Item From a List
numbers = [2,4,7,9]

# remove 4 from the list
numbers.remove(4)

print(numbers) 

# Output: [2, 7, 9]

# Remove One or More Elements of a List
names = ['John', 'Eva', 'Laura', 'Nick', 'Jack']

# deleting the second item
del names[1]
print(names)

# deleting items from index 1 to index 3 
del names[1: 4]
print(names) # Error! List doesn't exist.
'''
Python List Methods
append()	Adds an item to the end of the list
extend()	Adds items of lists and other iterables to the end of the list
insert()	Inserts an item at the specified index
remove()	Removes item present at the given index
pop()	Returns and removes item present at the given index
clear()	Removes all items from the list
index()	Returns the index of the first matched item
count()	Returns the count of the specified item in the list
sort()	Sorts the list in ascending/descending order
reverse()	Reverses the item of the list
copy()	Returns the shallow copy of the list
'''

# List Comprehension in Python
# create a list with square values
numbers = [n**2 for n in range(1, 6)]
print(numbers)    
