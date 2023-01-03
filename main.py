import random

count = 0
win = 0 
lose = 0

name = input("Enter Your Name: ")

while count <= 4:

    game = ["rock", "paper", "scissors"]
    player = input("Rock Paper or Scissors: ").lower()
    computer = game[random.randint(0, len(game) - 1)]

    while player not in game:
        player = input("Rock Paper or Scissors: ").lower() 

    if computer == player:
        print("Computer: ", computer)
        print("You: ", player)
        print("Tie!")
        win += 1
        lose += 1

    if player == "rock":
        if computer == "paper":
            print("Computer: ", computer)
            print("You: ", player)
            print("Computer won")
            lose += 1

        elif computer == "scissors":
            print("Computer: ", computer)
            print("You: ", player)
            print("You won")
            win += 1

    if player == "paper":
        if computer == "scissors":
            print("Computer: ", computer)
            print("You: ", player)
            print("Computer won")
            lose += 1

        elif computer == "rock":
                print("Computer: ", computer)
                print("You: ", player)
                print("You won")
                win += 1

    if player == "scissors":
        if computer == "rock":
            print("Computer: ", computer)
            print("You: ", player)
            print("Computer won")
            lose += 1

        elif computer == "paper":
                print("Computer: ", computer)
                print("You: ", player)
                print("You won")
                win += 1
    count += 1

if lose > win:
    print("Computer: ", lose)
    print("You: ", win)
    print("You lose")

if win > lose:
    print("Computer: ", lose)
    print("You: ", win)
    print("You win")