rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random

chose = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. \n"))

rps = ["rock", "paper", "scissors"]
rps_pic = [rock, paper, scissors]
game = [rps, rps_pic]

user_chose = rps[chose]
computer_chose = random.randint(0, 2)
computer_chose_rps = rps[computer_chose]

if user_chose == "rock":
  if computer_chose_rps == "rock":
    print(f"You chose: \n {game[1][chose]} \nComputer chose: {game[1][computer_chose]} \nIt's draw.")
  elif computer_chose_rps == "paper":
    print(f"You chose: \n {game[1][chose]} \nComputer chose: {game[1][computer_chose]} \nYou lose.")
  else:
    print(f"You chose: \n {game[1][chose]} \nComputer chose: {game[1][computer_chose]} \nYou win.")
elif user_chose == "paper":
  if computer_chose_rps == "paper":
    print(f"You chose: \n {game[1][chose]} \nComputer chose: {game[1][computer_chose]} \nIt's draw.")
  elif computer_chose_rps == "scissors":
    print(f"You chose: \n {game[1][chose]} \nComputer chose: {game[1][computer_chose]} \nYou lose.")
  else:
    print(f"You chose: \n {game[1][chose]} \nComputer chose: {game[1][computer_chose]} \nYou win.")
else:
  if computer_chose_rps == "scissors":
    print(f"You chose: \n {game[1][chose]} \nComputer chose: {game[1][computer_chose]} \nIt's draw.")
  elif computer_chose_rps == "rock":
    print(f"You chose: \n {game[1][chose]} \nComputer chose: {game[1][computer_chose]} \nYou lose.")
  else:
    print(f"You chose: \n {game[1][chose]} \nComputer chose: {game[1][computer_chose]} \nYou win.")
    