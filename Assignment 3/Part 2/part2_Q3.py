fruits = ["apple", "raspberry", "pineapple", "cherry"]
if "apple" in fruits:
    print("Found at index:", fruits.index("apple"))

fruits[1:3] = ["orange"]
print(fruits)

fruits.insert(2, "apricot")
print(fruits)

fruits.extend(["car", "bike", "aeroplane"])
print(fruits)
