import random

# :-D  =^P :\

def random_eyes():
    eyes = [":",";","="]
    return random.choice(eyes)

def random_nose():
    nose = ["-","^",""]
    return random.choice(nose)

def random_mouth():
    mouth = ["D","P","|","\\","/"]
    return random.choice(mouth)

def generate_emoticon():
    eyes = random_eyes()
    nose = random_nose()
    mouth = random_mouth()
    face = eyes+nose+mouth
    return face



def main():
    running = True
    while running == True:
        value = input("Enter Y or N if want an emoticon: ")
        if value == "N" or value == "n":
            break
        emoticon  = generate_emoticon()
        print(f"Your random emoticon: {emoticon}")

main()