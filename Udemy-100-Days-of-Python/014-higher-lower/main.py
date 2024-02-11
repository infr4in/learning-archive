from art import logo, vs
from game_data import data
from random import choice
# from replit import clear


def get_random_account():
    return choice(data)


def compare(guess, a, b):
    if a > b:
        return guess == "a"
    else:
        return guess == "b"


def higher_lower():
    print(logo)
    user_score = 0
    b = get_random_account()

    while True:
        a = b
        b = get_random_account()
        
        while a == b:
            b = get_random_account()
    
        print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}")
        print(vs)
        print(f"Anainst B: {b['name']}, a {b['description']}, from {b['country']}")
        
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        a_fc = a['follower_count']
        b_fc = b['follower_count']
        is_correct = compare(guess, a_fc, b_fc)

        # clear()
        print(logo)
        if is_correct:
            user_score += 1
            print(f"You're right! Current score: {user_score}.")
        else:
            print(f"Sorry, that's wrong. Final score: {user_score}")
            break


higher_lower()
