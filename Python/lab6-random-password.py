import string
import random

chars = string.ascii_letters + string.digits + "!@#$%z6&*()_+~"

def create_random_password(length):
    pwd = ""
    for x in range(length):
        pwd += random.choice(chars)
    return pwd

def create_random_lowercase_chars(length):
    pwd = ""
    for x in range(length):
        pwd += random.choice(string.ascii_lowercase)
    return pwd

def create_random_uppercase_chars(length):
    pwd = ""
    for x in range(length):
        pwd += random.choice(string.ascii_uppercase)
    return pwd

def create_random_number_chars(length):
    pwd = ""
    for x in range(length):
        pwd += random.choice(string.digits)
    return pwd

def create_random_special_chars(length):
    pwd = ""
    for x in range(length):
        pwd += random.choice("!@#$%z6&*()_+~")
    return pwd

def how_many_characters():
    value = "prep"
    while value.isdigit() != True:
        value = input("How many characters do you want your random password to be? ")
    return int(value)

def create_custom_password():
    lower = ""
    while lower.isdigit() != True:
        lower = input("How many lowercase characters do you want in your password? ")
    upper = ""
    while upper.isdigit() != True:
        upper = input("How many uppercase characters do you want in your password? ")
    numbers = ""
    while numbers.isdigit() != True:
        numbers = input("How many numbers characters do you want in your password? ")
    special = ""
    while special.isdigit() != True:
        special = input("How many special characters do you want in your password? ")

    return(int(lower), int(upper), int(numbers), int(special))


def main():
    running = True
    while running == True:
        value = input("Enter Y or N if you generate a random password: ")
        if value == "N" or value == "n":
            break
        pwd = ""
        value = input("Enter Y if you want a randomly password or N for a custom password: ")
        if value == "N" or value == "n":
            (lower, upper, numbers, special) = create_custom_password()
            pwd = create_random_lowercase_chars(lower)
            pwd += create_random_uppercase_chars(upper)
            pwd += create_random_number_chars(numbers)
            pwd += create_random_special_chars(special)
            password_list = list(pwd)
            random.shuffle(password_list)
            pwd = ''.join(password_list)
        else:
            length = how_many_characters()
            pwd = create_random_password(length)

        print(f"New random password: {pwd}")

main()