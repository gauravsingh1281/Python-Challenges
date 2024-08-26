# Coding Challenge 18
# Wap to check whether a given number is Armstrong or not.

num = input("Enter any no. to check if it is Armstrong or not.")
originalNum = int(num)
power = len(num)
newNum = 0
for digit in num:
    powerOfDigit = int(digit) ** power
    newNum += powerOfDigit
if originalNum == newNum:
    print(f"{num} is Armstrong No.")
else:
    print(f"{num} is not a Armstrong No.")
