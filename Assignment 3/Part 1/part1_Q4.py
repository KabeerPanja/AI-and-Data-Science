num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

def largest(a, b, c):
    if a > b and a > c:
        print(f"{a} is the largest number")
    elif b > a and b > c:
        print(f"{b} is the largest number")
    elif c > b and c > a:
        print(f"{c} is the largest number")
    elif a > b and a == c:
        print(f"{a} and {c} are the largest numbers")
    elif a > c and a == b:
        print(f"{a} and {b} are the largest numbers")
    elif b > a and b == c:
        print(f"{b} and {c} are the largest numbers")
    else:
        print("All the numbers are equal")

largest(num1, num2, num3)
