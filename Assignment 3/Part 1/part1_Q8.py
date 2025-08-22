def circle(radius):
    pi = 3.14
    area = pi * radius ** 2
    circumference = 2 * pi * radius
    return area, circumference

radius = float(input("Enter the radius: "))
area, circumference = circle(radius)
print("Area:", area)
print("Circumference:", circumference)
