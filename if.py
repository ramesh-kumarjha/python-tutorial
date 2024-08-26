#number= int(input('please enter the value : '))
#if number % 2 ==0:
 #   print(number, 'is evene number')
#else:
 #   print(number, 'is odd number')

#number = list(range(1, 101))
#print (number)
#for i in number:
 #   if i % 2 == 0:
  #      print(i , 'number is even number')
   # else:
    #    print(i, 'number is odd number')
x = 1
total = 0

# start of the if statement
if x != 0:
    total += x 
    print(total)  
# end of the if statement

print("This is always executed.")

number = -5

if number > 0:
    print('Positive number')

elif number < 0:
    print('Negative number')

else:
    print('Zero')

print('This statement is always executed')

number = 5

# outer if statement
if number >= 0:
    # inner if statement
    if number == 0:
      print('Number is 0')
    
    # inner else statement
    else:
        print('Number is positive')

# outer else statement
else:
    print('Number is negative')