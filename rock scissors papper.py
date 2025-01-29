import random

options = ("rock", "paper" ,"scissors")
running = True

while running:
    computer = random.choice(options)
    player = None

    while player not in options:
     player = input("Enter your choice (rock , paper , scissors)").lower()
    print(f"Players Choice : {player}")
    print(f"Computer Choice : {computer}")

    if player == computer:
        print("It's a tie!")
    elif player =="paper" and computer =="rock":
        print("Player Win!")
    elif player == "scissors" and computer == "paper":
        print("Player Win!")
    elif player == "rock" and computer == "scissors":
        print("Player Win")
    else:
        print("Computer Win!")
    play_again=input("Play Again (y/n)").lower()
    if play_again != "y":
        running = False

print("Thanks for playing")



