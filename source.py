# add random library to choose random move from list
import random

# if you don't want your output text to be bold, you don't have to add/install simple_colors library
from simple_colors import *

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
---'   ____)______
          ________)
       ____________)
      (____)
---.__(___)
'''


hand_signs = [rock, scissors, paper]
random_choice = random.choice(hand_signs)

user_input = input("Choose: rock, paper or scissors. Type: ")



# is user's move is scissors:
if user_input.lower() == "scissors" and random_choice == scissors:
    print("\n\nYour move:" + yellow(scissors) + "\n""Computer move:" + yellow(random_choice) + "\n" + blue("Tie."))
elif user_input.lower() == "scissors" and random_choice == rock:
    print("\n\nYour move:" + yellow(scissors) + "\n""Computer move:" + yellow(random_choice) + "\n" + red("You lose."))
elif user_input.lower() == "scissors" and random_choice == paper:
    print("\n\nYour move:" + yellow(scissors) + "\n""Computer move:" + yellow(random_choice) + "\n" + green("You win!"))

# if user's move is paper:
elif user_input.lower() == "paper" and random_choice == paper:
    print("\n\nYour move:" + yellow(paper) + "\n""Computer move:" + yellow(random_choice) + "\n" + blue("Tie."))
elif user_input.lower() == "paper" and random_choice == scissors:
    print("\n\nYour move:" + yellow(paper) + "\n""Computer move:" + yellow(random_choice) + "\n" + red("You lose."))
elif user_input.lower() == "paper" and random_choice == rock:
    print("\n\nYour move:" + yellow(paper) + "\n""Computer move:" + yellow(random_choice) + "\n" + green("You win!"))

# if user's move is rock:
elif user_input.lower() == "rock" and random_choice == rock:
    print("\n\nYour move:" + yellow(rock) + "\n""Computer move:" + yellow(random_choice) + "\n" + blue("Tie."))
elif user_input.lower() == "rock" and random_choice == scissors:
    print("\n\nYour move:" + yellow(rock) + "\n""Computer move:" + yellow(random_choice) + "\n" + green("You win."))
elif user_input.lower() == "rock" and random_choice == paper:
    print("\n\nYour move:" + yellow(rock) + "\n""Computer move:" + yellow(random_choice) + "\n" + red("You lose!"))
else:
    print("Please type: rock, paper or scissors.")








