'''
The break statement terminates the loop immediately when it's encountered.
'''
#We can use the break statement with the for loop to terminate the loop when a certain condition is met.

for i in range(5):
    if i == 2:
        break
    print(i , "this is break example")

# continue
'''
The continue statement skips the current iteration of the loop and the control flow of the program goes to the next iteration
'''

for i in range(5):
    if i == 3:
        continue
    print(i, "this is continue example")