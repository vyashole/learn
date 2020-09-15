# With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print("I like " + x)
print("this happens once")
# indentation works just like if.
# Unindented line marks the end the scope of the loop

# With the break statement we can stop the loop before it has looped through all the items:
for x in fruits:
    print(x)
    if x == "banana":
        print("i stop at banana")
        break

# To loop through a set of code a specified number of times, we can use the range() function,
# The range() function returns a sequence of numbers, starting from 0 by default,
# and increments with 1 by default, and ends at a specified number.
for x in range(6):
    print(x)
# range(6) means 0 to 5
# range(2, 6) will mean 2 to 5
# the final number is not inclusive
# range(2, 30, 3) means 2 to 30 in increments of 3 (30 not included)
# try different ranges in above loop
