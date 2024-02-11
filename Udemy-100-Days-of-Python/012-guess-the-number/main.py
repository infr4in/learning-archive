from random import randint
from art import logo

EASY = 10
HARD = 5


def set_dif():
    dif = input("Chose a difficulty. Type 'easy' or 'hard': ").lower().strip()
    if dif == "easy":
        return EASY
    elif dif == "hard":
        return HARD


def guess_check(guess, answer, lives):
    if guess > answer:
        print("Too high.")
        return lives - 1
    elif guess < answer:
        print("Too low.")
        return lives - 1
    else:
        print(f"You got it! The answer was {answer}.")
        

def game():  
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    # Chose a random number between 1 and 100.
    answer = randint(1, 100)
    # For tracking
    print(answer)
    # Set difficulty.
    lives = set_dif()
    # Repeat the guessing functionality if they get it wrong.
    guess = 0
    while guess != answer:
        print(f"You have {lives} attempts remaining to guess the number.") 
        guess = int(input("Make a guess: "))
        lives = guess_check(guess, answer, lives)
        if lives == 0:
            print("You've run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again.")


game()
