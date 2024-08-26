'''
A tuple is a collection similar to a Python list. The primary difference is that we cannot modify a tuple once it is created
We create a tuple by placing items inside parentheses ()
'''
numbers = (1, 2, -5)
print(numbers)

#Create a Tuple Using tuple() Constructor
tuple_constructor = tuple(('Jack', 'Maria', 'David'))
print(tuple_constructor)

# tuple of string types
names = ('James', 'Jack', 'Eva')
print (names)

# tuple of float types
float_values = (1.2, 3.4, 2.1)
print(float_values)

# tuple including string and integer
mixed_tuple = (2, 'Hello', 'Python')
print(mixed_tuple)

'''
Ordered - They maintain the order of elements.
Immutable - They cannot be changed after creation.
Allow duplicates - They can contain duplicate values.
'''
# Access Items Using Index
languages = ('Python', 'Swift', 'C++')

# access the first item
print(languages[0])   # Python

# access the third item
print(languages[2])   # C++

print(languages[-1])
