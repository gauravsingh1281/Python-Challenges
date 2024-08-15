#Coding Challenge 10
#Wap to find the factorial of a number (N) given by the user.

N= int(input("Enter any no. to know its factorial"))
i=1
fact=1
while i<=N:
    fact = fact*i
    i=i+1

print(f"Factorial of {N} = {fact}")