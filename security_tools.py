import random 
import string


# this make sure that the password is strong
def validate_password(password):

    has_letter = False
    has_number = False
    has_symbol = False
    
    for char in password:

        if char.isalpha():
            has_letter = True 

        elif char.isdigit():
            has_number = True

        else:
            has_symbol = True
    
    if len(password) >= 8 and has_letter and has_number and has_symbol:
        return True

    return False


# the make sure that the ip address is valid 
def validate_ip(ip):

    parts = ip.split(".")

    if len(parts) != 4:
        return False

    for part in parts:
        if not part.isdigit():
            return False
        
        number = int(part)

        if number < 0 or number >255:
            return False
    
    return True


# this generates a strong password
def generate_password():

    characters = string.ascii_letters + string.digits + "!%#?&*"

    length = random.randint(10, 16)

    password = ""

    for i in range(length):
        password = password + random.choice(characters)

    return password
