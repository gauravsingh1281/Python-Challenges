# Coding Challenge 20
# Wap to check whether a number is prime or not.

num = int(input("Enter any no. to check it is prime or not "))
count = 0
i = 1
while i <= num:
    if num % i == 0:
        count += 1
    i += 1
if count == 2:
    print(f"{num} is a prime no.")
else:
    print(f"{num} is not a prime no.")
