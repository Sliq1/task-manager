# Ask user to input the length of the 3 sides of a triangle
x = float(input("Enter the first side: "))
y = float(input("Enter the second side: "))
z = float(input("Enter the third side:"))
# if all sides are equel print equilateral
if x== y and y ==z:
    print("Equilateral")
# if 2 sides are equel print Isosceles
elif x == y or y == z or x == z:
    print("Isosceles")
# if no sides are equal print scalene
else:
    print("Scalene")

    
