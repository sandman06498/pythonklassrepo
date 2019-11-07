#this is a program to calculate the area of a circle
print("Enter 'x' for exit.")
radius = input("enter the radius of the circle then hit return: ")
if radius == 'x':
    exit()
else:
    circle_radius = int(radius)
    area_circle = 3.14*circle_radius**2
    print("area of circle =",area_circle)