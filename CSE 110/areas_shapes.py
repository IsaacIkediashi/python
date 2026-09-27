import math

# Containers for storing information
square_length = float(input("What is the length of the square? "))
square_calculation = square_length ** 2

print(f"The area of the square is {square_calculation}")
#----------------------------------------------------------------
# area for rectangle
rectangle_length = float(input("What is the length of the rectangle? "))

rectangle_width = float(input("What is the width of the rectangle? "))
rectangle_calculation = rectangle_length * rectangle_width
#----------------------------------------------------------------
print(f"The area of the rectangle is {rectangle_calculation}")
#----------------------------------------------------------------
# area for circle calculation
circle_radius = float(input("What is the radius of the circle? "))

circle_calculation = math.pi * (circle_radius ** 2)
print(f"The area of the circle is {circle_calculation:.4f}")