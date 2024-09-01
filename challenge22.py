# Coding Challenge 22
# Wap to find the sum of elements of the list.

num = []
listSize = int(input("How many elements you want to enter"))

for i in range(listSize):
    listValue = int(input("Enter Number"))
    num.append(listValue)
sum = 0
for j in range(len(num)):
    sum += num[j]

print(f"Sum = {sum}")
