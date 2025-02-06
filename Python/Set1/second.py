def Area_of_rectangle(length,breadth):
    return length*breadth

def Perimeter_of_rectangle(length,breadth):
    return 2*(length+breadth)

choice = int(input("""Enter the Choice
1.Area
2.Perimeter
>>> """))

if(choice!= 1 and choice!= 2):
    print("Invalid Choice!")
else:
 try:
    length = int(input("Enter the Length: "))
    breadth = int(input("Enter Breadth: "))
 except ValueError:
     print("Invalid Value Please Enter the Integer Number! ")
 else:
     if(choice == 1):
         print(f"Area of Rectangle is: {Area_of_rectangle(length,breadth)}")
     elif(choice == 2):
         print(f"Perimeter of Rectagle is: {Perimeter_of_rectangle(length,breadth)}")               


