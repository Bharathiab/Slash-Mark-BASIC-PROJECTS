import random
import string

def generate_password(length):
    """Generate a strong password with the given length."""
    if length < 3:
        raise ValueError("Password length should be at least 3 characters")

    # Define possible characters for the password
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    # Ensure the password has at least one of each type of character
    all_characters = lower + upper + digits + symbols
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits)
    ]

    if length > 3:
        password += random.choices(all_characters, k=length - 3)

    # Shuffle the password list to avoid predictable patterns
    random.shuffle(password)

    # Convert list to string and return the password
    return ''.join(password)

if __name__ == "__main__":
    num_passwords = int(input("How many passwords do you want to generate? "))
    print(f"Generating {num_passwords} passwords")

    passwords = []
    for i in range(num_passwords):
        length = int(input(f"Enter the length of Password #{i+1}: "))
        try:
            password = generate_password(length)
            passwords.append(password)
        except ValueError as e:
            print(e)
            continue

    for i, password in enumerate(passwords, 1):
        print(f"Password #{i}: {password}")
