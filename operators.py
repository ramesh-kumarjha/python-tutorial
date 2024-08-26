# Operators are special symbols that perform operations on variables and values
'''
Types of Python Operators
Arithmetic Operators
Assignment Operators
Comparison Operators
Logical Operators
Bitwise Operators
Special Operators
'''
# Python Arithmetic Operators
#a=10+5
#print(a)
a = 7
b = 2

# addition
print ('Sum: ', a + b)  

# subtraction
print ('Subtraction: ', a - b)   

# multiplication
print ('Multiplication: ', a * b)  

# division
print ('Division: ', a / b) 

# floor division
print ('Floor Division: ', a // b)

# modulo
print ('Modulo: ', a % b)  

# a to the power b
print ('Power: ', a ** b)   

# Python Assignment Operators
# assign 5 to x 
x = 5
'''
=	Assignment Operator	a = 7
+=	Addition Assignment	a += 1 # a = a + 1
-=	Subtraction Assignment	a -= 3 # a = a - 3
*=	Multiplication Assignment	a *= 4 # a = a * 4
/=	Division Assignment	a /= 3 # a = a / 3
%=	Remainder Assignment	a %= 10 # a = a % 10
**=	Exponent Assignment	a **= 10 # a = a ** 10
'''
# assign 10 to a
a = 10

# assign 5 to b
b = 5 

# assign the sum of a and b to a
a += b      # a = a + b

print(a)

# Output: 15
'''
Python Comparison Operators
==	Is Equal To	3 == 5 gives us False
!=	Not Equal To	3 != 5 gives us True
>	Greater Than	3 > 5 gives us False
<	Less Than	3 < 5 gives us True
>=	Greater Than or Equal To	3 >= 5 give us False
<=	Less Than or Equal To	3 <= 5 gives us True
'''
a = 5

b = 2

# equal to operator
print('a == b =', a == b)

# not equal to operator
print('a != b =', a != b)

# greater than operator
print('a > b =', a > b)

# less than operator
print('a < b =', a < b)

# greater than or equal to operator
print('a >= b =', a >= b)

# less than or equal to operator
print('a <= b =', a <= b)

'''
Python Logical Operators
'''
a = 5
b = 6

print((a > 2) and (b >= 6))    # True
'''
and	a and b	Logical AND:
True only if both the operands are True
or	a or b	Logical OR:
True if at least one of the operands is True
not	not a	Logical NOT:
True if the operand is False and vice-versa.
'''
# logical AND
print(True and True)     # True
print(True and False)    # False

# logical OR
print(True or False)     # True

# logical NOT
print(not True)          # False

# Python Special operators
'''
is	True if the operands are identical (refer to the same object)	x is True
is not	True if the operands are not identical (do not refer to the same object)	x is not True
'''
x1 = 5
y1 = 5
x2 = 'Hello'
y2 = 'Hello'
x3 = [1,2,3]
y3 = [1,2,3]

print(x1 is not y1)  # prints False

print(x2 is y2)  # prints True

print(x3 is y3)  # prints False

# Membership operators
'''
In Python, in and not in are the membership operators. They are used to test whether a value or variable is found in a sequence (string, list, tuple, set and dictionary).
in	True if value/variable is found in the sequence	5 in x
not in	True if value/variable is not found in the sequence	5 not in x
'''
message = 'Hello world'
dict1 = {1:'a', 2:'b'}

# check if 'H' is present in message string
print('H' in message)  # prints True

# check if 'hello' is present in message string
print('hello' not in message)  # prints True

# check if '1' key is present in dict1
print(1 in dict1)  # prints True

# check if 'a' key is present in dict1
print('a' in dict1)  # prints False

