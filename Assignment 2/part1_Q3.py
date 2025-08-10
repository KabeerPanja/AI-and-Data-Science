a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

if a == b and b == c:
    print("All three numbers are equal.")
elif a == b:
    print(f"{a} and {b} are equal, and they are the largest.")
elif a == c:
    print(f"{a} and {c} are equal, and they are the largest.")
elif b == c:
    print(f"{b} and {c} are equal, and they are the largest.")
elif a > b and a > c:
    print(f"{a} is the largest.")
elif b > a and b > c:
    print(f"{b} is the largest.")
else:
    print(f"{c} is the largest.")
