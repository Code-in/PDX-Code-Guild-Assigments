import random

def random_num():
    return random.randint(1,10)

def whats_your_guess():
    while True:
        value = input("Enter your numerical guess from 1 to 10: ")
        if value.isdigit and 1 <= int(value) <= 10:
            return int(value)

def to_high_to_low(number, guess):
    if guess < number:
        print("Guess too low!")
    else:
        print("Guess too high!")

def warmer_or_colder(number, guess, last_guess):
    new_guess = abs(number - guess)
    old_guess = abs(number - last_guess)
    if new_guess < old_guess:
        print("Your getting warmer!")
    else:
        print("Your getting colder!")

def compare_guess_to_answer(number, guess, tries, last_guess):
    success = False
    if guess == number:
        print(f"Correct! you guessed {tries + 1} times")
        success = True
    else:
        to_high_to_low(number, guess)
        if last_guess != None:
            warmer_or_colder(number, guess, last_guess)
        print("Try again!")
    # make sure to return the success and guess for setting the new last_guess
    return success, guess

def main():
    running = True
    while running == True:
        value = input("Enter Y or N if you want play a Number Guessing game!")
        if "n" == value.lower():
            break
        number = random_num()
        last_guess = None
        for i in range(10):
            guess = whats_your_guess()
            # Setting a success and last guess
            success, last_guess = compare_guess_to_answer(number, guess, i, last_guess)
            if success:
                break

main()