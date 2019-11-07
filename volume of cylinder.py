#this is a program to calculate the volume of a cylinder
print("Enter 'x' for exit.")
radius = input("enter the radius of the cylinder then hit return: ")
if radius == 'x':
    exit()
else:
    cylinder_radius = int(radius)
height = input("enter the height of the cylinder then hit return:")
if height == 'x':
    exit()
else:
    cylinder_height=int(height)
    volume_cylinder = 3.14*cylinder_radius**2*height
    print("volume of cylinder =",volume_cylinder)