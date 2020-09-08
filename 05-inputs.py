# User input can be taken from the console using the input()
user_name = input("Enter your name:")
print("Hello, " + user_name)

# note that input always comes in as string
# so id a use puts in 5 python gets "5"
# To convert your data types you can use casting
# int() - casts to an integer number from an integer literal,
# a float literal (by rounding down to the previous whole number),
# or a string literal (providing the string represents a whole number)
x = int(1)   # x will be 1
y = int(2.8)  # y will be 2
z = int("3")  # z will be 3
print(x, y, z)
# float() - casts to a float number from an integer literal,
# a float literal or a string literal
x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2")  # w will be 4.2

# str() - casts to a string from a wide variety of data types,
# including strings, integer literals and float literals
x = str("s1")  # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'


# casting is often used in combination with input
g = int(input("Get me a number:"))
