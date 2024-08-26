'''
In Python, the global keyword allows us to modify the variable outside of the current scope
'''
# global variable (we cant change the golbal variable value)
c = 1 

def add():

     # increment c by 2
    c = c + 2
    d = c+2

    print(c)
    print(d)

add()