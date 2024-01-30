import random

while True:
    # pick player choice
    your_choice = input("rock, paper, or scissors?: ").lower()

    # check if the input is valid
    if your_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        continue

 # convert the user input to a standard form
    if your_choice == "r":
        your_choice = "rock"
    elif your_choice == "p":
        your_choice = "paper"
    elif your_choice == "s":
        your_choice = "scissors"

    # computer choice
    possible_actions = ["rock" | "R" | "r", "paper" | "P" | "p", "scissors" | "s" | "S"]
    computers_action = random.choice(possible_actions)

    # show choices
    print(f"\nYou chose {your_choice}, AI chose {computers_action}")

    # pick and display winner
    if your_choice == computers_action:
        print(f"Both players selected {your_choice}. It's a tie!")
    elif your_choice == "rock" | "R" | "r":
        if computers_action == "scissors" | "s" | "S":
            print("You win!")
        else:
            print("You lose.")
    elif your_choice == "paper" | "P" | "p":
        if computers_action == "rock" | "R" | "r":
            print("You win!")
        else:
            print("You lose.")
    elif your_choice == "scissors" | "s" | "S":
        if computers_action == "paper" | "P" | "p":
            print("You win!")
        else:
            print("You lose.")

    # play again
    play_again = input("Try again? (y/n): ")
    if play_again.lower() != "y":
        break