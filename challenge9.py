#Coding Challenge 9
#Search for the first occurrence of the number (X) in this tuple using loop.

tup = (1,4,9,16,25,36,49,64,81,100)
X=49
i=0
while i<len(tup):
    if(tup[i]==X):
        print(f"Found {X} at index no. {i}")
        break
    else:
        print("Finding",X)
    i+=1
print("Searching end.")