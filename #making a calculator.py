#making a calculator
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
menu = ["+","-","*","/"]
choice = input("Enter your choice: ")
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if choice == "+":
    print(add(a,b))
elif choice == "-":
    print(sub(a,b))
elif choice == "*":
    print(mul(a,b))
elif choice == "/":
    print(div(a,b))
else:
    print("Quit")

    