data = ["Tahir", 44, "AI and Data Science", True]
strings = []
numbers = []
booleans = []

for item in data:
    if type(item) == str:
        strings.append(item)
    elif type(item) == int:
        numbers.append(item)
    elif type(item) == bool:
        booleans.append(item)

print(f"Strings: {strings}")
print(f"Numbers: {numbers}")
print(f"Booleans: {booleans}")
