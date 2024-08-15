# Coding Challenge 12
#Wap to Print the Sum of First (N) Natural Numbers
N= int(input("Enter a natural no. upto which you want to find the sum"))
sum=0
for i in range(1,N+1):
    sum+=i
print(f"The Sum of First {N} Natural Numbers = {sum}")