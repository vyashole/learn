x = int(input('Enter a number:'))
y = int(input('Enter another number:'))
while True:
    print ('0 - Toh mai kya karu?')
    print ('1 - Add the two numbers')
    print ('2 - Subtract the two numbers')
    print ('3 - Multiply the two numbers')
    print ('4 - Divide the two numbers')
    print ('5 - Exit')
    choice = int(input("Enter your choice:"))
    if choice == 1:
        print (f'The addition of two numbers is {x+y}')
    elif choice == 2:
        if x > y:
            result = x-y
        else:
            result = y-x
        print (f'The difference of two numbers is {result}')
    elif choice == 3:
        print (f'The multiplication of two numbers is {x*y}')
    elif choice == 4:
        if y != 0:
            print(f'The division of two numbers is {x/y}')
        else:
            print("I don't know the answer")
    elif choice == 0:
        pass
    elif choice == 5:
        print ('Okay, bye!')
        break
    else:
        print ('The choice is invalid')