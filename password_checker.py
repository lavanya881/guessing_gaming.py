# Password Strength Checker

def check_password_strength(password):
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False

    # Check length
    length = len(password)

    # Check each character
    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        else:
            has_special = True

    # Evaluate strength
    if length >= 8 and has_upper and has_lower and has_digit and has_special:
        return "Strong Password 💪"
    elif length >= 6 and has_digit and (has_upper or has_lower):
        return "Medium Password ⚠️"
    else:
        return "Weak Password ❌"


# Main program
print("🔐 Password Strength Checker")

password = input("Enter your password: ")
result = check_password_strength(password)

print("Result:", result)