# Coding Challenge 19
# Wap to reverse a given number

num = int(input("Enter any no."))
i = num
reverseNum = 0
while i > 0:
    reverseNum = (reverseNum * 10) + i % 10
    i = i // 10

print(f"Reverse of {num} = {reverseNum}")
