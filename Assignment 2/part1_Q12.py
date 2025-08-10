temp = float(input("Enter temperature: "))

if temp <= 0:
    print("Freezing")
elif temp < 26 and temp > 0:
    print("Moderate")
else:
    print("Hot")
