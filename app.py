print("Hello World")
#This is a calculator program
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    return a / b

a= int(input("Enter a number: "))
b= int(input("Enter a number: "))
print("The sum of the two numbers is: ",    add(a, b))
print("The difference of the two numbers is: ", subtract(a,b))
print("The product of the two numbers is: ", multiply(a,b))
if b != 0:
    print("The division of the two numbers is: ", divide(a,b))
else:
    print("Error: Division by zero")

