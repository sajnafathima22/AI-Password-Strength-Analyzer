import random
import string
def generate_password():
    upper=string.ascii_uppercase
    lower=string.ascii_lowercase
    digits=string.digits
    special="@#$%^&*!?"
    all_characters =upper+lower+digits+special
    password=""
    for i in range(12):
        password+= random.choice(all_characters)
    return password