import random
from art import logo
# from replit import clear


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def play_a_game():
    play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower().strip()
    if play == "y":
        # clear()
        return True
    else:
        print("Goodbye :(")
        return False


def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def game_result(user_score, computer_score):
    if user_score > 21 and computer_score > 21:
        return "You lose."
    elif computer_score == 0:
        return "Computer has BLACKJACK. You lose."
    elif user_score == 0:
        return "BLACKJACK! You win."
    elif user_score == computer_score:
        return "It's draw."
    elif user_score > 21:
        return "You lose."
    elif computer_score > 21:
        return "You win."
    elif user_score > computer_score:
        return "You win."
    else:
        return "You lose."


while play_a_game():
    print(logo)
    user_cards = []
    computer_cards = []
    for i in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    game_over = False
    while not game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"    Your cards: {user_cards}, current score: {user_score}")
        print(f"    Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            get_card = input("Type 'y' to get another card, type 'n' to pass: ").lower().strip()
            if get_card == "y":
                user_cards.append(deal_card())
            else:
                game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)
    
    print(f"    Your final hand: {user_cards}, final score: {user_score}")
    print(f"    Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(game_result(user_score, computer_score))
