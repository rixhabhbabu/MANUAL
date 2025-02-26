def decimal_others(value, choice):
    try:
        value = int(value)
        if choice == 1:
            return str(value)
        elif choice == 2:
            return bin(value)[2:]
        elif choice == 3:
            return oct(value)[2:]
        elif choice == 4:
            return hex(value)[2:]
        else:
            return "Invalid Option"
    except ValueError:
        return "Invalid Decimal Input"

def binary_others(value, choice):
    try:
        decimal_value = int(value, 2)
        if choice == 1:
            return value
        elif choice == 2:
            return str(decimal_value)
        elif choice == 3:
            return oct(decimal_value)[2:]
        elif choice == 4:
            return hex(decimal_value)[2:]
        else:
            return "Invalid Option"
    except ValueError:
        return "Invalid Binary Input"

def octal_others(value, choice):
    try:
        decimal_value = int(value, 8)
        if choice == 1:
            return value
        elif choice == 2:
            return str(decimal_value)
        elif choice == 3:
            return bin(decimal_value)[2:]
        elif choice == 4:
            return hex(decimal_value)[2:]
        else:
            return "Invalid Option"
    except ValueError:
        return "Invalid Octal Input"

def hex_others(value, choice):
    try:
        decimal_value = int(value, 16)
        if choice == 1:
            return value
        elif choice == 2:
            return str(decimal_value)
        elif choice == 3:
            return oct(decimal_value)[2:]
        elif choice == 4:
            return bin(decimal_value)[2:]
        else:
            return "Invalid Option"
    except ValueError:
        return "Invalid Hexadecimal Input"

print("Convert from: 1: Decimal, 2: Binary, 3: Octal, 4: Hexadecimal")
input_choice = input("Enter the choice: ")

if input_choice.isdigit():
    input_choice = int(input_choice)
    if input_choice == 1:
        decimal_num = input("Enter decimal number: ")
        print("Convert to: 1: Decimal, 2: Binary, 3: Octal, 4: Hexadecimal")
        choice = input("Enter target conversion: ")
        if choice.isdigit():
            print("Converted value: ", decimal_others(decimal_num, int(choice)))
        else:
            print("Invalid Choice")
    elif input_choice == 2:
        binary_num = input("Enter binary number: ")
        print("Convert to: 1: Binary, 2: Decimal, 3: Octal, 4: Hexadecimal")
        choice = input("Enter target conversion: ")
        if choice.isdigit():
            print("Converted value: ", binary_others(binary_num, int(choice)))
        else:
            print("Invalid Choice")
    elif input_choice == 3:
        octal_num = input("Enter octal number: ")
        print("Convert to: 1: Octal, 2: Decimal, 3: Binary, 4: Hexadecimal")
        choice = input("Enter target conversion: ")
        if choice.isdigit():
            print("Converted value: ", octal_others(octal_num, int(choice)))
        else:
            print("Invalid Choice")
    elif input_choice == 4:
        hex_num = input("Enter hexadecimal number: ")
        print("Convert to: 1: Hexadecimal, 2: Decimal, 3: Octal, 4: Binary")
        choice = input("Enter target conversion: ")
        if choice.isdigit():
            print("Converted value: ", hex_others(hex_num, int(choice)))
        else:
            print("Invalid Choice")
    else:
        print("Invalid Choice")
else:
    print("Invalid Choice")
