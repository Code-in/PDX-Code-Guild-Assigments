

def ask_for_three_card():
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

def score_hand(hand):
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

        if (ace_count == 1) and (value + 10 <= 21):
            value += 10
        elif (ace_count == 2) and (value + 10 <= 21):
            value += 10
            
    return value


def get_advice(hand):
    score = score_hand(hand)

    if score < 17:
        print(f"{score} Hit")
    elif 17 < score < 21:
        print(f"{score} Stay")
    elif score == 21:
        print(f"{score} BlackJack!")
    else:
        print(f"{score} Already Busted")

    
def main():
    hand = ask_for_three_card()
    get_advice(hand)

main()