import random
import art


start = input("Do you want to play a game of Blackjack? Type 'y' or 'n' ")

if start == "n":
    print("Goodbye!")
    game = False
game = True

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

hand = []
score = 0

dealer_hand = []
dealer_score = 0
for i in range(2):
    hand.append(random.choice(cards))
    score += hand[i]
    dealer_hand.append(random.choice(cards))
    dealer_score += dealer_hand[i]


while game:



    print(art.logo)

    print(f"Your cards: {hand}, current score: {score}\n")
    print(f"Computer's first card: {dealer_hand[0]}\n")
    another_question = input("Type 'y' to get another card, type 'n' to pass:\n")

    if another_question == "y" and score < 22:
        hand.append(random.choice(cards))
        score += hand[-1]
    if another_question == 'n' or score > 21:
        while dealer_score < 17:
            dealer_hand.append(random.choice(cards))
            dealer_score += dealer_hand[-1]
        print(f"Your final hand: {hand}, final score: {score}\n")
        print(f"Computer's final hand: {dealer_hand}, final score: {dealer_score}\n")
        if dealer_score < score < 22:
            print("You win!")
            exit()
        elif score < dealer_score < 22 and score < 22:
            print("You lose!")
            exit()
        elif score > 21:
            print("Bust! You lose")
            exit()
        elif dealer_score > 21:
            print("You win!")
            exit()
        else:
            print("Draw")
            exit()




