import string
import random

# Create the character pool for the random generation of passwords
chars = string.ascii_letters + string.digits + string.punctuation

# Create the random password per the length requested
def create_random_password(length):
    pwd = ""
    for x in range(length):
        pwd += random.choice(chars)
    return pwd

# Create the random lowercase character per the length requested
def create_random_lowercase_chars(length):
    pwd = ""
    for x in range(length):
        pwd += random.choice(string.ascii_lowercase)
    return pwd

# Create the random uppercase character per the length requested
def create_random_uppercase_chars(length):
    pwd = ""
    for x in range(length):
        pwd += random.choice(string.ascii_uppercase)
    return pwd

# Create the random digits per the length requested
def create_random_number_chars(length):
    pwd = ""
    for x in range(length):
        pwd += random.choice(string.digits)
    return pwd

# Create the random special character per the length requested
def create_random_special_chars(length):
    pwd = ""
    for x in range(length):
        pwd += random.choice(string.punctuation)
    return pwd

# Ask the user how many digits they want in the randomly generate password
def how_many_characters():
    value = "prep"
    while value.isdigit() != True:
        value = input("How many characters do you want your random password to be? ")
    return int(value)

# Ask the user how many lowercase, uppercase, digits and special characters they want in custom generate password
def create_custom_password():
    lower = ""
    while not lower.isdigit():
        lower = input("How many lowercase characters do you want in your password? ")
    upper = ""
    while not upper.isdigit():
        upper = input("How many uppercase characters do you want in your password? ")
    numbers = ""
    while not numbers.isdigit():
        numbers = input("How many numbers characters do you want in your password? ")
    special = ""
    while not special.isdigit():
        special = input("How many special characters do you want in your password? ")

    print(f"lower: {int(lower)} upper: {int(upper)} digits: {int(numbers)} special: {int(special)}")
    return(int(lower), int(upper), int(numbers), int(special))

# Main function with the REPL which allows us to ask question of the user get to the data needed to create a password
def main():
    running = True
    while running == True:
        value = input("Enter Y or N if you generate a random password: ")
        if value in ['n', 'N', 'No', 'NO', 'no']:
            break
        elif value.isascii and value in ['y', 'Y', 'Yes', 'YES', 'yes']:
            pwd = ""
            value = input("Enter R if you want a randomly generated password or C for a custom password: ")
            if value in ['c', 'C', 'Custom', 'CUSTOM', 'custom']:
                (lower, upper, numbers, special) = create_custom_password()
                pwd = create_random_lowercase_chars(lower)
                pwd += create_random_uppercase_chars(upper)
                pwd += create_random_number_chars(numbers)
                pwd += create_random_special_chars(special)
                password_list = list(pwd)
                random.shuffle(password_list)
                pwd = ''.join(password_list)
            elif value in ['r', 'R', 'Random', 'RANDOM', 'random']:
                length = how_many_characters()
                pwd = create_random_password(length)

            print(f"New random password: {pwd}")

main()