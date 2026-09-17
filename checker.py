def check_password(password):

    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False

    special = "@#$%^&*!?"

    for ch in password:

        if ch.isupper():
            has_upper = True

        elif ch.islower():
            has_lower = True

        elif ch.isdigit():
            has_digit = True

        elif ch in special:
            has_special = True

    if len(password) >= 8 and has_upper and has_lower and has_digit and has_special:
        return "Strong"

    elif len(password) >= 6:
        return "Medium"

    else:
        return "Weak"