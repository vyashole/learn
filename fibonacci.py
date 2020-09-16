# 1 1 2 3 5 8... - fibonacci series
# 1 -> 1
# 2 -> 1
# n -> f(n-1) + f(n-2)

# x = 1
# y = 0
# i = 1
# while i <= 100:
#     z = x+y
#     y = x
#     print(x)
#     x = z
#     i = i + 1

def fibonacci(n):
    if(n == 1 or n == 2):
        return 1
    else:
        return (fibonacci(n-1) + fibonacci(n-2))


for i in range(1, 101):
    print(fibonacci(i))
