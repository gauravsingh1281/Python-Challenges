list1 = ["m","a","a","m"]

copyList1 = list1.copy()
copyList1.reverse()

if(list1 == copyList1):
    print(f"Palindrom as {list1} == {copyList1}")
else:
     print(f"Not a Palindrom as {list1} !== {copyList1}")