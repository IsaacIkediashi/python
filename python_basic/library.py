#------ External code pre-written for us to use in our code, some are built in and some are downloadable
import math #------ starts the connection to the library by importing it, in this case the math library
math.ceil(4.67)


#------ access to the math module using the name of the module - math, ceil() is the item we want from the library
math.ceil(3.67)

math1 = math.ceil(8.56)
print(math1) #------ outputs 9, rounds value up to the next whole number "ceiling"

math2 = math.floor(8.56)
print(math2) #------ outputs 8, rounds value down to the next whole number "floor"

math3 = math.exp(8.56)
print(math3) #------ outputs 5218.681172451978, raise e to the power of value

math4 = math.sin(8.56)
print(math4) #------ outputs 0.7609512213187744, computes the trigonometry sine function of value in radians