# write a program to take 10 integers as input and add them up. Display the sum at the end.
counter = 0
for i in range(1, 11):
    x = int(input("Enter a number:"))
    counter = counter + x
print(counter)
