def get_suggestion(password):

    suggestions = []

    if len(password) < 8:
        suggestions.append("Increase password length")

    if not any(ch.isupper() for ch in password):
        suggestions.append("Add uppercase letters")

    if not any(ch.islower() for ch in password):
        suggestions.append("Add lowercase letters")

    if not any(ch.isdigit() for ch in password):
        suggestions.append("Add numbers")

    special = "@#$%^&*!?"

    if not any(ch in special for ch in password):
        suggestions.append("Add special characters")

    if len(suggestions) == 0:
        return "Excellent Password 🔐"

    return "\n".join(suggestions)