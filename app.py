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
print(add(a, b))
print(subtract(a,b))
print(multiply(a,b))
if b != 0:
    print(divide(a,b))
else:
    print("Error: Division by zero")

