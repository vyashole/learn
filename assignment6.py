# _
# _|
# _|_
# _|_|
# _|_|_
num = int(input("Enter a number:"))
for i in range(1, num+1):
    for j in range(0, i):
        if j % 2 == 0:
            print("_", end="")
        else:
            print("|", end="")
    print()
