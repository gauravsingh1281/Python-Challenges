# Coding Challenge 23
# Wap to count total number of odd and even numbers in the list.

num = []
listSize = int(input("Enter no. of element you want to add in the list"))

for j in range(listSize):
    listElement = int(input("Enter Number"))
    num.append(listElement)
oddCount = 0
evenCount = 0
for i in range(len(num)):
    if num[i] % 2 == 0:
        evenCount += 1
    else:
        oddCount += 1

print(
    f"No. of Even element = {evenCount} and No. of Odd element = {oddCount} in list = {num}"
)
