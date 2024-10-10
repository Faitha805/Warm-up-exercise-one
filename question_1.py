#1
# The volume of a sphere with radius r is (4/3)* pie * r**2. 
# What is the volume of the sphere with radius 5. 
# Make sure the program enters the radius from the keyboard and provide the answer in 2 decimal places


radius = int(input("Enter the radius of the sphere: "))
#import math library
import math
volume_of_the_sphere = (4/3)*math.pi*(radius**3)
print(f"The volume of the sphere with a radius {radius} is {volume_of_the_sphere:.2f}")
