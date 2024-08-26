'''
print function accepts 5 parameters
'''
# print with end whitespace
print('Good Morning!', end= ' ')
print('It is rainy today')

print('New Year', 2023, 'See you soon!', sep= '. ')
print('Programiz is ' + 'awesome.')
#Output formatting
x = 5
y = 10

print('The value of x is {} and y is {}'.format(x,y))

#Python Input
'''
While programming, we might want to take the input from the user. In Python, we can use the input() function.
'''
# using input() to take user input
num = input('Enter a number: ')

print('You Entered:', num)

print('Data type of num:', type(num))

#  To convert user input into a number we can use int() or float() functions as:
num = int(input('Enter a number: '))
print (num)


