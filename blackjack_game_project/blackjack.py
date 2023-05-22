import random
from art import logo

cards = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "J": 10, "Q": 10, "K": 10, "A": 11}

game_end = False
player_score = 0
dealer_score = 0

print(logo)
while not game_end:
    player_hand = random.choices(list(cards.keys()), k=2)
    dealer_hand = random.choices(list(cards.keys()), k=2)
    print(f"Your cards: [{player_hand[0]}, {player_hand[1]}]\nComputer`s first card: {dealer_hand[0]}")
    draw_card = input("Type 'y' to get another card, type 'n' to pass: ")
    if draw_card == "y":
        player_hand.append(random.choice(list(cards.keys())))
        print(f"Your final hand: [{player_hand[0]}, {player_hand[1]}, {player_hand[2]}]")
        player_score = cards[player_hand[0]] + cards[player_hand[1]] + cards[player_hand[2]]
    else:
        print(f"Your final hand: [{player_hand[0]}, {player_hand[1]}]")
        player_score = cards[player_hand[0]] + cards[player_hand[1]]
    print(f"Computer`s final hand: [{dealer_hand[0]}, {dealer_hand[1]}]")
    dealer_score = cards[dealer_hand[0]] + cards[dealer_hand[1]]

    if dealer_score < player_score <= 21:
        print("You won")
    elif dealer_score > player_score or player_score > 21:
        print("Computer won")
    else:
        print("Draw")
    continue_playing = input("Do you want to play another game of Blackjack? Type 'y' or 'n': ")
    if continue_playing == "y":
        game_end = False
    else:
        game_end = True
