# Coding Challenge 8
# Print the mathematical table of a number (N) on user input.

N=int(input("Enter any no. to know its mathematical table"))
i=1
while(i<=10):
    print(f"{N} X {i} = {N*i}")
    i+=1
