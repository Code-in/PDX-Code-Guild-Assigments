import random

HUMAN = 2
COMPUTER = 1

def random_num():
    return random.randint(1,10)

def who_guesses():
    print("Computer guess your number Enter 1")
    value = input("Guess computer's number Enter 2: ")
    if value.isdigit() and COMPUTER <= int(value) <= HUMAN:
        return int(value)

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
    return success

def get_random_number(who):
    if who == COMPUTER:
        number = int(input("Enter a number including or between 1 and 10: "))
    elif who == HUMAN:
        number = random_num()
    return number


def main():
    running = True
    while running == True:
        value = input("Enter Y or N if you want play a Number Guessing game: ")
        if "n" == value.lower():
            break
        who = who_guesses() # this should return a 1 or 2
        number = get_random_number(who)
        last_guess = None
        for i in range(10):
            if who == COMPUTER:
                guess = random.randint(1,10)
            elif who == HUMAN:
                guess = whats_your_guess()
            # Setting a success and last guess
            success = compare_guess_to_answer(number, guess, i, last_guess)
            if success:
                break
            last_guess = guess

main()