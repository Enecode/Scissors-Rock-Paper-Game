import random


def get_choices():
    player_choice = input("Enter a choice(rock, paper, scissors): ")
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    choice = {"Player": player_choice, "computer": computer_choice}
    return choice


def check_win(player, computer):
    print(f"You chose {player} Computer chose {computer}")
    if player == computer:
        return "It's a tie"
    elif player == "rock":
        if computer == "scissors":
            return "Rock smashes scissors! You win"
        else:
            return "Paper covers rock! You lose."

    elif player == "paper":
        if computer == "rock":
            return "paper covers rock! you win!"
        else:
            return "scissors cuts paper! You lose."

    elif player == "scissors":
        if computer == "paper":
            return "scissors cut paper! You win!"
        else:
            return "Rock smashes scissors! You lose."


get_choices()
