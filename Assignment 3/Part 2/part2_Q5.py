numbers = [32, 54, 66, 11, 77, 10, 90]
for i in numbers:
    if i < 20:
        numbers.remove(i)
print(numbers)

numbers.sort()
print("Ascending:", numbers)
numbers.sort(reverse=True)
print("Descending:", numbers)

average = sum(numbers) / len(numbers)
print("Average:", average)
