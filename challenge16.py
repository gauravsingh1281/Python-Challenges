#Coding Challenge 16
#Wap to print only even number between 1 to N.

N = int(input("Enter any no. upto which you want to print the even no."))
for i in range(1,N+1):
    if i%2==0:
        print(i)