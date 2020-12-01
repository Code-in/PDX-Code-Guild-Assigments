import random

def eight_ball_prediction():
    preset_predictions = [ "It is certain", "It is decidedly so", "Without a doubt", "Yes definitely", 
    "You may rely on it", "As I see it, yes", "Most likely", "Outlook good", "Yes", "Signs point to yes", "Reply hazy try again",
    "Ask again later", "Better not tell you now", "Cannot predict now", "Concentrate and ask again", "Don't count on it",
    "My reply is no", "My sources say no", "Outlook not so good", "Very doubtful"]

    return random.choice(preset_predictions)


def main():
    running = True
    while running == True:
        value = input("Enter Y or N if you want to recieve a prediciton from the 'Magic Eight Ball'")
        if value == "N" or value == "n":
            break
        user_question = input("Ask the Magic 8-ball for a prediction: ")
        prediction = eight_ball_prediction()

        print(f"The Magic 8-Ball says: {prediction}")
        print("----~----")
        print("")

main()