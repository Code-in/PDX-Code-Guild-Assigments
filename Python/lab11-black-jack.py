
# This function asks the user for 3 cards as the input for the hand to score
def ask_for_three_card():
    ''' This method ask the user for 3 parks which are in the acceptable card list. If not it keeps asking until they match the acceptable cards. '''
    print("Blackjack Advice 2020(tm) ;-)")
    acceptiable_cards = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'j', 'q', 'k', 'a']
    users_card = []
    while True:
        card = input("Enter first card: ")
        if card in acceptiable_cards:
            users_card.append(card)
            break

    while True:    
        card = input("Enter second card: ")
        if card in acceptiable_cards:
            users_card.append(card)
            break
    
    while True:
        card = input("Enter third card: ")
        if card in acceptiable_cards:
            users_card.append(card)
            break
    return users_card

# this function scores the user hand
def score_hand(hand):
    ''' This method score the user's hand and makes some basic decisions based on hand score and numnber of aces in hand. '''
    value = 0
    ace_count = 0

    for card in hand:
        if card in ['10', 'J', 'Q', 'K', 'j', 'q', 'k']:
            value += 10
        elif card in ['A', 'a']:
            value += 1
            ace_count += 1
        else:
            value += int(card)

    if ((0 < ace_count <= 3) and (value + 10 <= 21)):
        value += 10
            
    return value

# Give the user a base 'Hit', 'Stay', 'Black Jack' or 'Busted' feedback based on their hand
def get_advice(hand):
    ''' This methods performs some basic advice based on the user hand '''
    score = score_hand(hand)

    if score < 17:
        print(f"{score} Hit")
    elif 17 < score < 21:
        print(f"{score} Stay")
    elif score == 21:
        print(f"{score} BlackJack!")
    else:
        print(f"{score} Already Busted")

# main process function to run this 1 shot app
def main():
    ''' Main method to run all the code to see if we have a solution '''
    hand = ask_for_three_card()
    get_advice(hand)

main()