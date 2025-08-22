gadgets = ["Mobile", "Laptop", 10.0, "Marker", 3, 10, "Speakers", "Camera", 310.25]
strings = []
numbers = []

for item in gadgets:
    if type(item) == str:
        strings.append(item)
    else:
        numbers.append(item)

print("Strings:", strings)
print("Numbers:", numbers)

strings.sort()
print("Ascending:", strings)
strings.sort(reverse=True)
print("Descending:", strings)

strings.sort(key=len)
print("Sorted by length:", strings)

numbers.sort()
print("Ascending:", numbers)
numbers.sort(reverse=True)
print("Descending:", numbers)
