num1 = float(input("Enter first number: "))
op = input("Enter operator (+, -, x, /): ")
num2 = float(input("Enter second number: "))

if op == "+":
    print("Result:", num1 + num2)
elif op == "-":
    print("Result:", num1 - num2)
elif op == "x":
    print("Result:", num1 * num2)
elif op == "/":
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Can't Divide By Zero")
else:
    print("Invalid operator")
