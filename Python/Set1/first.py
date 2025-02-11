def Celcius_to_Fehranite(Celcius):
    return Celcius * (9/5) + 32
def Fehranite_to_Celcius(fehranite):
    return (fehranite - 32) * (5/9)

choice = (input("""Enter Your Choice:
1. Celcius -> Fehranite
2. Fehranite -> Celcius
>>> """))
if (choice[0] == "c" or choice[0] == "C"):
    try:
     Celcius = float(input("Enter Celcius: "))
    except ValueError:
        print("Please Enter Floating Value")
    else:     
     print(f"{Celcius} degree Celius is Equal to {Celcius_to_Fehranite(Celcius)} degree Fehranite")
elif(choice[0] == "f" or choice[0] == "F"):
   try: 
    Fehranite = float(input("Enter Fehranite: "))
   except ValueError:
        print("Please Enter Floating Value")
   else:      
    print(f"{Fehranite} degree Fehranite is Equal to {Fehranite_to_Celcius(Fehranite)} degree Celcius")
else:
    print("Invalid Choice! Please write Correct Spelling")        




