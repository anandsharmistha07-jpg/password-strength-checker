   
import re
import random
import string

def check_password_strength(password):
    strength = 0

    if len(password) >= 8:
        strength += 1
    if re.search(r"[A-Z]", password):
        strength += 1
    if re.search(r"[a-z]", password):
        strength += 1
    if re.search(r"[0-9]", password):
        strength += 1
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1

    if strength <= 2:
        return "Weak"
    elif strength <= 4:
        return "Medium"
    else:
        return "Strong"


def generate_strong_password():
    length = 12
    all_chars = string.ascii_letters + string.digits + "!@#$%^&*()"

    # Ensure at least one of each type
    password = [
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.digits),
        random.choice("!@#$%^&*()")
    ]

    # Fill remaining characters
    password += random.choices(all_chars, k=length - 4)

    # Shuffle for randomness
    random.shuffle(password)

    return "".join(password)


# MAIN PROGRAM
password = input("Enter your password: ")

result = check_password_strength(password)
print("Password Strength:", result)

if "Weak" in result:
    print("Suggested Strong Password:", generate_strong_password())
    