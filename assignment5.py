#for i in range (5,0,-1):
#	for j in range(0,i):
#		print ('*', end = "")
#	print()


#for i in range (1,6):
#	for j in range (0,i):
#		print (i,end = "")
#	print()

num = int(input("Enter a number:"))
for i in range (1,num+1):
	if (i > 9):
		break
	for j in range (0,i):
		print (i, end = "")
	print()
