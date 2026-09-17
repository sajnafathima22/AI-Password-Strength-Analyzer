from checker import check_password

password = input("Enter Password: ")

result = check_password(password)

print("Password Strength:", result)