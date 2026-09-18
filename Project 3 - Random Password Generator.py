# Project 3 - Random Password Generator 

import random
import string

print("🔐 Welcome to DecodeLabs Password Generator!")

try:
    length = int(input("Enter desired password length: "))
    if length < 4:
        print("Password length must be at least 4.")
    else:
        # Character pool: letters, digits, special chars
        chars = string.ascii_letters + string.digits + string.punctuation
        
        # Ensure at least one of each type
        password = [
            random.choice(string.ascii_lowercase),
            random.choice(string.ascii_uppercase),
            random.choice(string.digits),
            random.choice(string.punctuation)
        ]
        
        # Fill the rest randomly
        password += random.choices(chars, k=length - 4)
        random.shuffle(password)
        
        print("Generated Password:", "".join(password))
except ValueError:
    print("Invalid input. Please enter a number.")
