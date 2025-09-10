import math

radius = float(input("Enter the radius of the circle: "))
area = math.pi * pow(radius, 2)
final = round(area, 2)
print("The area of the circle is:", final)
