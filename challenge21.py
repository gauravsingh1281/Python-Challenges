# Coding Challenge 21
# Wap to check whether a given number is palindrome number or not.

num = int(input("Enter any no. to check it is palindrome or not."))
reverseNum = 0
i = num
while i > 0:
    reverseNum = (reverseNum * 10) + i % 10
    i = i // 10

if num == reverseNum:
    print(f"{num} is palindrome")
else:
    print(f"{num} is not a palindrome")
