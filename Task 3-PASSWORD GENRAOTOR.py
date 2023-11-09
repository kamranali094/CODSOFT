import random
import string

def generate_password(length,lowercase,uppercase,digits,special_chars):
    characters = ''

    if lowercase==1:
        characters += string.ascii_lowercase
    if uppercase ==1:
        characters += string.ascii_uppercase
    if digits==1:
        characters += string.digits
    if special_chars==1:
        characters += string.punctuation

    if not characters:
        print("Please select at least one character type.")
        return None

    generated_password = ''.join(random.choice(characters) for _ in range(length))
    return generated_password

def main():
    print("Welcome to Password generator !")

    length = int(input("Enter the length of the your password:"))
    lowercase = input("Include Lowercase ?? (1/2): ").lower()
    uppercase = input("Include uppercase ?? (1/2): ").lower()
    digits = input("Include digits ?? (1/2): ").lower()
    special_chars = input("Include special characters ?? (1/2): ").lower() == '1'

    password = generate_password(length, lowercase, uppercase, digits,special_chars)

    if password:
        print(f"Generated Password: {password}")

y1=main()
