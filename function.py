def greet():
    print('Hello World!')

# call the function
greet()

print('Outside function')

def greet(name):
    print("Hello", name)

# pass argument
greet("John")

# function with two arguments
def add_numbers(num1, num2):
    sum = num1 + num2
    print("Sum: ", sum)

# function call with two values
add_numbers(5, 4)

# function definition
def find_square(num):
    result = num * num
    return result

# function call
square = find_square(3)

print('Square:', square)

def future_function():
    pass

# this will execute without any action or error
future_function()  

def greet(name, message="Hello"):
    print(message, name)

# calling function with both arguments
greet("Alice", "Good Morning")

# calling function with only one argument
greet("Bob")

# function to print keyword arguments
def greet(**words):
    for key, value in words.items():
        print(f"{key}: {value}")

# pass any number of keyword arguments
greet(name="John", greeting="Hello")

# program to find sum of multiple numbers 

def find_sum(*numbers):
    result = 0
    
    for num in numbers:
        result = result + num
    
    print("Sum = ", result)

# function call with 3 arguments
find_sum(1, 2, 3)

# function call with 2 arguments
find_sum(4, 9)
