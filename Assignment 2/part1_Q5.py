age = int(input("Enter your age: "))

if age < 18:
    print("Minor")
elif age > 18 and age < 60:
    print("Adult")
else:
    print("Senior citizen")
