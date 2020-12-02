import random

choices = 'rps'
names = {"r":"Rock", "p":"Paper", "s":"Scissors"}



def ask_user_for_rock_paper_scissors():
    response = False
    while response == False:
        selection = input("Enter 'R' for Rock, 'P' for Paper and 'S' for Scissors: ")
        if selection.lower() in choices:
            return selection.lower()


def ask_computer_for_choice():
    return random.choice(choices)

def who_won(computer, player):
    if computer == player:
        ouput = 1
    elif computer + player == 'rs': # Rock beats Scissors Computer Winds
        ouput =  2
    elif computer + player == 'ps': # paper loses to Scissors Player 1 wins
        ouput =  3
    elif computer + player == 'rp': # rock loses to paper Player 1 wins
        ouput =  3
    elif computer + player == 'sp': # scissors beats paper Computer wins
        ouput =  2
    elif computer + player == 'sr': # scissors loses Rock Player 1 wins
        ouput =  3
    elif computer + player == 'pr': # paper beats rock Computer wins
        ouput =  2
    else:
        output  = 4
    return ouput

def print_winner(winner, computer_choice, player_choice):
    if winner == 1:
        print(f"Computer: {names[computer_choice]} and Player 1: {names[player_choice]} tied!")
    elif winner == 2:
       print(f"Computer: {names[computer_choice]} wins over Player 1: {names[player_choice]}")
    elif winner == 3:
        print(f"Computer: {names[computer_choice]} loses to Player 1: {names[player_choice]}")
    else:
        print("I missed an option")

def main():
    running = True
    while running == True:
        value = input("Enter Y or N if want play a game of 'Rock, Paper, Scissors': ")
        if value == "N" or value == "n":
            break
        player_choice = ask_user_for_rock_paper_scissors()
        computer_choice = ask_computer_for_choice()
        winner = who_won(computer_choice, player_choice)
        print_winner(winner, computer_choice, player_choice)
    
main()