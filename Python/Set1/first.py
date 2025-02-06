def Celcius_to_Fehranite(Celcius):
    return Celcius * (9/5) + 32
def Fehranite_to_Celcius(fehranite):
    return (fehranite - 32) * (5/9)

choice = int(input("""Enter Your Choice:[1 and 2]
1. Celcius -> Fehranite
2. Fehranite -> Celcius
>>> """))
if (choice == 1):
    Celcius = int(input("Enter Celcius: "))
    print(f"{Celcius} degree Celius is Equal to {Celcius_to_Fehranite(Celcius)} degree Fehranite")
elif(choice == 2):
    Fehranite = int(input("Enter Fehranite: "))
    print(f"{Fehranite} degree Fehranite is Equal to {Fehranite_to_Celcius(Fehranite)} degree Celcius")
else:
    print("Invalid Choice! Please write Correct Spelling")        




