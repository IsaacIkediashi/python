import math
def compute_area_square(side):
  return compute_area_rectangle(side, side)
def compute_area_rectangle(length,width):
  return length * width
def compute_area_circle(radius):
  return math.pi * radius * radius

user_shape = ""

while True:
    user_shape = input("What kind of shape do you have? ")


    if user_shape == "square":
        length = float(input("What is the length of the side? "))
        result = compute_area_square(length)
        print(f"The area is {result}")
    elif user_shape == "rectangle":
        length = float(input("What is the length? "))
        width = float(input("What is the width? "))
        result = compute_area_rectangle(length, width)
        print(f"The area is {result}")
    elif user_shape == "circle":
        radius = float(input("What is the radius? "))
        result = compute_area_circle(radius)
        print(f"The area is {result}")
    elif user_shape == "quit":
       break 
    else:
        print("Invalid shape! Please enter square, rectangle, or circle.")

