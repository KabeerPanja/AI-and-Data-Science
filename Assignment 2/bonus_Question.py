a = 0
b = 1

print(a)
print(b)

for _ in range(8):
    c = a + b
    
    a = b
    b = c

    print(b)
