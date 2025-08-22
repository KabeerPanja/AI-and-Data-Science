num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

def larger(a, b):
    if a > b:
        print(f"{a} is greater than {b}")
    elif b > a:
        print(f"{b} is greater than {a}")
    else:
        print("Both numbers are same")

larger(num1, num2)
