# An "if statement" is written by using the if keyword, followed by the condition.
a = 33
b = 200
if b > a:
    print("b is greater than a")
print("This will print regardless of the condition")
# Notice the indentation. Whatever is indented under the if statement is affected by the condition.
# unindented line means the if statement is over and the statement will be executed regardless.
# try changing the a and b values to see this in effect

# if... else
x = 200
y = 33
if y > x:
    print("y is greater than x")
else:
    print("y is not greater than x")

# Anything that is NOT covered by the if condition will be executed in the else block


# if... elif... else
i = 200
j = 33
if i > j:
    print("i is greater than j")
elif i == j:
    print("i and j are equal")
else:
    print("i is greater than j")
# elif block will execute if all the if and other elif blocks above it are false.
# Anything that is not covered by the elif ladder falls down to the else block
