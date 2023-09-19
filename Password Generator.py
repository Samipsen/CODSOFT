import random
import string

# Function to generate a random password
def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Prompt the user for the desired password length
try:
    password_length = int(input("Enter the desired password length: "))
    if password_length <= 0:
        print("Password length must be greater than 0.")
    else:
        generated_password = generate_password(password_length)
        print(f"Generated Password: {generated_password}")
except ValueError:
    print("Please enter a valid number for password length.")
