#Coding Challenge 15
# Wap to print the sum of cube from 1 to (N) number.

N=int(input("Enter any no. upto which you want sum the cube"))
i=1
sum=0
while i<=N:
    cube = i**3
    sum += cube
    i=i+1
print(f"Sum of cube from 1 to {N} = {sum}")