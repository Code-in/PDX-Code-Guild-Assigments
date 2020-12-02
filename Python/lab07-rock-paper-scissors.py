import random

choices = 'rpslv'
names = {"r":"Rock", "p":"Paper", "s":"Scissors", "v":"Volcan", "l":"Lizard"}
wins = {'rr':0, 'rs':1, 'rp':2, 'rv':2, 'rl':1, 
        'ss':0, 'sr':2, 'sp':1, 'sv':2, 'sl':1, 
        'pp':0, 'ps':2, 'pr':1, 'pv':1, 'pl':2, 
        'vv':0, 'vr':1, 'vp':2, 'vs':1, 'vl':2, 
        'll':0, 'lr':2, 'lp':1, 'ls':2, 'lv':1}


def ask_user_for_rock_paper_scissors():
    response = False
    while response == False:
        selection = input("Enter 'R' for Rock, 'P' for Paper, 'S' for Scissors, 'V' for Volcan and 'L' for Lizard: ")
        if selection.lower() in choices:
            return selection.lower()

def ask_computer_for_choice():
    return random.choice(choices)

def who_won(computer, player):
    return wins[computer + player]

def print_winner(winner, computer_choice, player_choice):
    if winner == 0:
        print(f"Computer: {names[computer_choice]} and Player 1: {names[player_choice]} tied!")
    elif winner == 1:
       print(f"Computer: {names[computer_choice]} wins over Player 1: {names[player_choice]}")
    elif winner == 2:
        print(f"Computer: {names[computer_choice]} loses to Player 1: {names[player_choice]}")
    else:
        print("I missed an option")

def main():
    running = True
    while running == True:
        value = input("Enter Y or N if want play a game of 'Rock, Paper, Scissors, Vulcan, Lizard': ")
        if value == "N" or value == "n":
            break
        player_choice = ask_user_for_rock_paper_scissors()
        computer_choice = ask_computer_for_choice()
        winner = who_won(computer_choice, player_choice)
        print_winner(winner, computer_choice, player_choice)
    
main()