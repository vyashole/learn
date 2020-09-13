# *
# **
# ***
# ****
# *****
# for i in range (5,0,-1):
#	for j in range(0,i):
#		print ('*', end = "")
#	print()

# 1
# 22
# 333
# 4444
# 55555
# for i in range (1,6):
#	for j in range (0,i):
#		print (i,end = "")
#	print()

# same as above, but only up to 9
num = int(input("Enter a number:"))
for i in range(1, num+1):
    if (i > 9):
        break
    for j in range(0, i):
        print(i, end="")
    print()
