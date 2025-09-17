# TODO: this is the import for the random module, we use it to generate random numbers.
import random


# TODO: This is the ascii art for rock, paper and scissors.
rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""


scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""


# TODO: We store the ascii art variables in a list so that we can easily use it elsewhere in our code
game_moves = [rock, paper, scissors]


# TODO: This is where our output to the user starts from
# Our first output is some form of game intro message
name = input("Enter your name: ")
welcome_message = (f"Welcome {name}\n"
                   "Feel like you can beat us at Rock Paper Scissors?\n")
print(welcome_message)
input("Click Next let's see: ")


# TODO: Here we just ask print out a menu to our user
# The menu is just a bunch of options that specify the moves the user can make
# i.e., rock, paper, scissors.
# However, by allocating each move to a number we make it easier for the user to specify his move.
move_names = ["Rock", "Paper", "Scissors"]
print("Your moves are: ")
for i in range(len(move_names)):
    print(f"{i+1}: {move_names[i]}")


# TODO: We get the user's input when the user enters a number from our options
# Then we use that number to pick the appropriate move from our list of moves.
# Do you see the intuition here. With the list of moves we created,
# We can directly pick out a matching move using list indexing.
user_choice = int(input("Pick a number from the options: "))
user_move = game_moves[user_choice-1]


# TODO: We get the computer's input by using random selection
# We get the computer's move using the same pattern for the user move
computer_choice = random.randint(1,3)
computer_move = game_moves[computer_choice-1]


# TODO: Isn't interesting that after the user and computer make their moves
# We print out the name of their move and an ASCII art
# That looks like the actual shape of people's hands when they play rock paper scissors
print(f"You dealt {move_names[user_choice-1]} {user_move}")
print(f"The computer dealt {move_names[computer_choice-1]} {computer_move}")


# TODO: This is the second hardest part of the program
# Programming the logic that tells the computer who has won
# Based on the choices of the computer and user
user_wins = False
computer_wins = False
if user_choice == computer_choice:
    print("It is a tie")
elif user_choice == 1 and computer_choice == 3:
    user_wins = True
    print("User wins")
elif user_choice == 2 and computer_choice == 1:
    user_wins = True
    print("User wins")
elif user_choice == 3 and computer_choice == 2:
    user_wins = True
    print("User wins")
else:
    computer_wins = True
    print("Computer wins")


# TODO: This is just a brief section explaining the possible outcomes in rock paper scissors
# 1. They both tie when they play the same move
# 2. The user wins
# 3. The computer wins

# todo: So how does this relate to the conditionals above.
# 1. The first if statement covers the outcome 1 above (When it is a tie)
# 2. The 3 elifs cover all the possible options that the computer and the user can play
# such that the user wins. The 3 elifs cover outcome 2.
# 3. The last statement is simply a process of elimination. If outcome 1 is not met,
# And outcome 2 is not met. Then the only outcome possible is outcome 3.
