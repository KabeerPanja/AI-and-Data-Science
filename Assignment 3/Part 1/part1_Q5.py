age = int(input("Enter your age: "))

def compare_age(age):
    if age < 18:
        return "Minor"
    elif age < 60:
        return "Adult"
    else:
        return "Senior citizen"

print(compare_age(age))
