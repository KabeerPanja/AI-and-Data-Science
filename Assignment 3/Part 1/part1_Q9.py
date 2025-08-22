def pass_or_fail(score):
    if score > 60:
        return "Pass"
    else:
        return "Fail"

marks = float(input("Enter Marks: "))
print(pass_or_fail(marks))
