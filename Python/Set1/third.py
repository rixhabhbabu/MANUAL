import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits 
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Specify the desired length of the password
password_length = int(input("Enter the Length of the Password: "))
password = generate_password(password_length)
print("Generated password:", password)
