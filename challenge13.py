# Coding Challenge 13
# Wap to create a simple calculator for basic operation like additon, subtraction, multiplication and division.

number1 = int(input("Enter number 1"))
number2 = int(input("Enter number 2"))
operator = input("Choose operation to perform like +, -, /, *")

def add(num1,num2):
    sum = num1+num2
    print(f"Sum of {num1} and {num2} = {sum}")
def sub(num1,num2):
    diff = num1-num2
    print(f"Subtraction of {num1} and {num2} = {diff}")
def product(num1,num2):
    multi= num1*num2
    print(f"Product of {num1} and {num2} = {multi}")
def div(num1,num2):
    division = num1/num2
    print(f"Division of {num1} by {num2} = {division}")

if operator =="+":
    add(number1,number2)
elif operator == "-" :
    sub(number1,number2)
elif operator == "*" :
    product(number1,number2)
elif operator == "/" :
    div(number1,number2)
else:
    print("You have entered invalid value please try again")