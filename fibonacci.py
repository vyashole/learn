# 1 1 2 3 5 8... - fibonacci series

x = 1
y = 0
i = 1
while i <= 100:
    z = x+y
    y = x
    print(x)
    x = z
    i = i + 1
    

    