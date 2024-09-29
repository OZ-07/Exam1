import math
#Prompt the user to enter the radius of the circle as an integer
#Use the math module to calculate the area and circumference
#Display the area and circumference of the circle to the user using F-String

radius_int=int(input("Enter your integer, and press enter:"))
circle_circumference=2*radius_int*math.pi
circle_area= math.pi*radius_int**2

print(f'the area of your circle is {circle_area}, and the circumference is {circle_circumference}')