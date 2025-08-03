import random
import art

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    # Blackjack (21 with two cards)
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    # Handle ace (11) conversion to 1 if the sum is greater than 21
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(u_score, c_score):
    if u_score == c_score:
        return "Draw :-)"
    elif c_score == 0:
        return "Opponent has a blackjack, you lose."
    elif u_score == 0:
        return "You have a blackjack, you win!"
    elif u_score > 21:
        return "you loses"
    elif c_score > 21:
        return "Computer lose"
    elif u_score > c_score:
        return "Yay! You win!"
    else:
        return "You lose :-("

def play_game():
# Initializing game
    print(art.blackjack_logo)
    user_cards = []
    computer_cards = []
    computer_score = -1
    user_score = -1

# Deal two cards each for user and computer
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    should_continue = True

# User's turn
    while should_continue:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"User's cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            should_continue = False
        else:
            game_ended = input("Type 'y' to get another card, type 'n' to pass: ")
            if game_ended == "y":
                user_cards.append(deal_card())
            else:
                should_continue = False

# Computer's turn: Computer keeps drawing if score is below 17 and doesn't have blackjack
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    # Final result
    print(f"User's hand cards: {user_cards}, current score: {user_score}")
    print(f"Computer's hand cards: {computer_cards}, current score: {computer_score}")

    print(compare(user_score, computer_score))

while input("Do you want to play a game of blackjack? Type 'y' for yes, 'n' for no.") == "y":
    print("\n" * 20)
    play_game()