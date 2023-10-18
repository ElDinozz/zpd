import random

turns = ["rock", "paper", "scissors"]

human_turn = input("Enter rock, paper or scissors: ")
computer_turn = random.choice(turns)

if human_turn == computer_turn:
    print("I'ts a draw!")
elif human_turn == "rock" and computer_turn == "scissor":
    print("Human wins")
elif human_turn == "paper" and computer_turn == "rock":
    print("Human wins")
elif human_turn == "scissors" and computer_turn == "paper":
    print("Human wins")
else:
    print("computer wins")
