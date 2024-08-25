# Coding Challenge 17
# Wap to find the sum of digits of a given number (N).

# 1st way
"""
N= input("Enter any no. to find the sum of its digit")
sum=0
i=0
while i<len(N):
    digit=N[i]
    sum = sum +int(digit)
    i=i+1
print(f"Sum of digits = {sum}")
"""
# 2nd way
"""
N= input("Enter any no. to find the sum of its digit")
sum = 0
for digit in N:
    sum = sum + int(digit)
print(f"Sum of digits = {sum}")
"""

# 3rd way
N = int(input("Enter any no. to find the sum of its digit"))
sum = 0
while N > 0:
    sum = sum + N % 10
    N = N // 10
print(f"Sum of digits = {sum}")
