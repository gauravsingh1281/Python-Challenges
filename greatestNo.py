num1 = int(input("Enter number 1"))
num2 = int(input("Enter number 2"))
num3 = int(input("Enter number 3"))

if(num1>num2 and num1>num3):
    print(f"1st number is greatest = {num1}")
elif(num2>num3):
    print(f"2nd number is greatest = {num2}")
else:
    print(f"3rd number is greatest = {num3}")
