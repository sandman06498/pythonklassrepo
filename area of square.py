#this is a program to calculate the area of a square
print("Enter 'x' for exit.")
side = input("enter side length of square then hit return: ")
if side == 'x':
    exit()
else:
    side_length = int(side)
    area_square = side_length*side_length
    print("Area of Square =",area_square)4