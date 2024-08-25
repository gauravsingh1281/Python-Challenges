#Coding Challenge 14
# Wap to print the sum of square from 1 to (N) number.

N=int(input("Enter any no. upto which you want sum the square"))
i=1
sum=0
while i<=N:
    square = i**2
    sum += square
    i+=1
print(f"Sum of square from 1 to {N} = {sum}")