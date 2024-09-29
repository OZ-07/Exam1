"""rectangle"""
import math
"""Display the area of the rectangle to the user using F-Strings
Allow the user to input floating point numbers for width and height.
Call a generalized, custom function that takes 2 parameters."""

base_int = int(input("Enter base integer, and press enter:"))
leg_int= int(input("enter leg integer here, and press enter:"))
#leg is height?
area_of_rectangle= leg_int * base_int
print(f'the area of your rectangle is {area_of_rectangle}')