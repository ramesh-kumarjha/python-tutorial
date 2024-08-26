# Python Local Variables
def greet():

    # local variable
    message = 'Hello'
    
    print('Local', message)

greet()

# try to access message variable 
# outside greet() function
#print(message)

# Python Global Variables
# declare global variable
message = 'Hello'

def greet():
    # declare local variable
    print('Local', message)

greet()
print('Global', message)

'''
In Python, nonlocal variables are used in nested functions whose local scope is not defined. This means that the variable can be neither in the local nor the global scope.

We use the nonlocal keyword 
'''