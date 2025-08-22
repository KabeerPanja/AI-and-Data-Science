num = float(input("Enter a number: "))

def check_num(num):
    if num > 0:
        return "positive"
    elif num < 0:
        return "negative"
    else:
        return "zero"

check = check_num(num)
print(f"This number is {check}")
