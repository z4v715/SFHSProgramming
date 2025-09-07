""" 
==================================================================== |
███████╗███████╗██╗  ██╗███████╗    ██████╗ ██████╗  ██████╗  ██████╗ 
██╔════╝██╔════╝██║  ██║██╔════╝    ██╔══██╗██╔══██╗██╔═══██╗██╔════╝ 
███████╗█████╗  ███████║███████╗    ██████╔╝██████╔╝██║   ██║██║  ███╗
╚════██║██╔══╝  ██╔══██║╚════██║    ██╔═══╝ ██╔══██╗██║   ██║██║   ██║
███████║██║     ██║  ██║███████║    ██║     ██║  ██║╚██████╔╝╚██████╔╝
╚══════╝╚═╝     ╚═╝  ╚═╝╚══════╝    ╚═╝     ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ 
----------------------- Rock Paper Scissors ------------------------
==================================================================== |
""" 

import random

# Used to convert between a choice made and its index
CHOICES = ["rock", "paper", "scissors"]

# Random choice of AI and player choice
ai_choice = random.randint(0, 2)
player_choice = input("Rock, paper, scissors, shoot!\n")

print(f"AI chooses: {CHOICES[ai_choice]}")

# If the player choice is not valid, raise an exception
if player_choice.lower() in CHOICES:
    player_choice = CHOICES.index(player_choice.lower())
else:
    raise Exception("Invalid choice.")

# See who won and who lost
if player_choice == ai_choice:
    print("Tie!")
else:
    if player_choice == 0 and ai_choice == 1:
        print("You lost.")
    elif player_choice == 0 and ai_choice == 2:
        print("You win!")
    elif player_choice == 1 and ai_choice == 0:
        print("You win!")
    elif player_choice == 1 and ai_choice == 2:
        print("You lost.")
    elif player_choice == 2 and ai_choice == 0:
        print("You lost.")
    else:
        print("You win!")