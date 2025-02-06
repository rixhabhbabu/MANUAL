def Factorial(num):
    if num == 1:
        return 1
    else :
        return num*Factorial(num-1)
    
Number = int(input("Enter the Number: "))
print(f"The Factorial of {Number} is: {Factorial(Number)}")    
    