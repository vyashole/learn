# A function is a block of code which only runs when it is invoked.
# You can pass data, known as parameters or arguments, into a function.
# A function can return data as a result.
# You define a function with def
def my_function(name):
    print(f"Hello from {name}")
    my_function(name)


# This function will run only when invoked
print('before invoking the function')
my_function("adwait")
print('after invoking the function')
