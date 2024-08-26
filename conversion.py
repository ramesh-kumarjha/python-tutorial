'''
In programming, type conversion is the process of converting data of one type to another. For example: converting int data to str.
here are two types of type conversion in Python.
Implicit Conversion - automatic type conversion
Explicit Conversion - manual type conversion
'''
'''
Python Implicit Type Conversion
In certain situations, Python automatically converts one data type to another. This is known as implicit type conversion
'''
integer_number = 123
float_number = 1.23

new_number = integer_number + float_number

# display new value and resulting data type
print("Value:",new_number)
print("Data Type:",type(new_number))

'''
Explicit Type Conversion
In Explicit Type Conversion, users convert the data type of an object to required data type.

We use the built-in functions like int(), float(), str(), etc to perform explicit type conversion
This type of conversion is also called typecasting because the user casts (changes) the data type of the objects
'''
num_string = '12'
num_integer = 23

print("Data type of num_string before Type Casting:",type(num_string))

# explicit type conversion
num_string = int(num_string)

print("Data type of num_string after Type Casting:",type(num_string))

num_sum = num_integer + num_string

print("Sum:",num_sum)
print("Data type of num_sum:",type(num_sum))
