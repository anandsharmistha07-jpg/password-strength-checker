import re
import random
import string

common_passwords = ["123456", "password", "12345678", "qwerty", "abc123", "admin"]

def check_password_strength(password):
    strength = 0
    feedback = []

    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters long")

    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        feedback.append("Add at least one uppercase letter")

    if re.search(r"[a-z]", password):
        strength += 1
    else:
        feedback.append("Add at least one lowercase letter")

    if re.search(r"[0-9]", password):
        strength += 1
    else:
        feedback.append("Include at least one number")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1
    else:
        feedback.append("Include at least one special character")

    if password.lower() in common_passwords:
        feedback.append("This is a very common password!")
        return "Weak", feedback

    if strength <= 2:
        return "Weak", feedback
    elif strength <= 4:
        return "Medium", feedback
    else:
        return "Strong", feedback


def estimate_crack_time(strength):
    if strength == "Weak":
        return "Few seconds"
    elif strength == "Medium":
        return "Minutes to hours"
    else:
        return "Years"


def generate_strong_password():
    length = 12
    all_chars = string.ascii_letters + string.digits + "!@#$%^&*()"

    password = [
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.digits),
        random.choice("!@#$%^&*()")
    ]

    password += random.choices(all_chars, k=length - 4)
    random.shuffle(password)

    return "".join(password)


if __name__ == "__main__":
    password = input("Enter your password: ")

    strength, feedback = check_password_strength(password)
    print("\nPassword Strength:", strength)

    print("Estimated Crack Time:", estimate_crack_time(strength))

    if feedback:
        print("\nSuggestions:")
        for f in feedback:
            print("-", f)

    if strength == "Weak":
        print("\nSuggested Strong Password:", generate_strong_password())nerate_strong_password())
    
