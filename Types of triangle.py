# Program to find the type of triangle based on side lengths

# Input side lengths
a = float(input("Enter side a: "))
b = float(input("Enter side b: "))
c = float(input("Enter side c: "))

# Check if the triangle is valid using triangle inequality theorem
if a + b <= c or a + c <= b or b + c <= a:
    print("Not a valid triangle")

# Check for Equilateral triangle
elif a == b == c:
    print("Equilateral Triangle")

# Check for Isosceles triangle
elif a == b or b == c or a == c:
    print("Isosceles Triangle")

# Otherwise, it is a Scalene triangle
else:
    print("Scalene Triangle")
