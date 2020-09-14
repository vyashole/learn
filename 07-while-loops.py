# While

# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#     print(print("I like " + x))
# print("this happens once")
# length = len(fruits)
# i = 0
# while i < length:
#     print("I like " + fruits[i])
#     i = i + 1
# print("this happens once")

# i = 1
# while True:
#     print(i)
#     i = i*64

n = int(input("Enter any number:"))
# 2 ---> n and check divisibility
# if it is divisible then mark it as not prime and stop
# otherwise contine
i = 2
is_prime = True
while i < n/2:
    if n % i == 0:
        is_prime = False
        break
    i = i + 1
if is_prime:
    print(f"{n} is a prime number")
else:
    print(f"{n} is not a prime number")
