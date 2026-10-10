import colorama 
from colorama import Style , Fore , Back
typeObject = input(Fore. + "Enter the shape (Triangle , Square ,Circle):").upper()

if typeObject == "SQUARE":
    width = int(input("enter the width:"))
    length = int(input("enter the length:"))
    area = width*length
    print("the area is", area)
elif typeObject == "TRIANGLE":
    base = int(input("enter the base:"))
    height = int(input("enter the height:"))
    area = base*height*0.5
    print("the area is", area)
elif typeObject == "CIRCLE":
    radius = int(input("enter the radius:"))
    area = 3.142*radius**2
    print("the area is", area)
else:
    print("invalid")
