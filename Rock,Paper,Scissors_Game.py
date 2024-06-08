import random
while True:
    choice = ["rock", "paper", "scissors"]
    pc = random.choice(choice)
    player = input("Rock, paper, scissors: ")

    if (player == "rock" and pc == "scissors") or (player == "paper" and pc == "rock") or (player == "scissors" and pc == "paper"):
        print("Player wins")
    elif (pc == "rock" and player == "scissors") or (pc == "paper" and player == "rock") or (pc == "scissors" and player == "paper"):
        print("PC wins")
    elif player == pc:
        print("It is a draw!!")
    elif player == "":
        break
    else:
        print("You have entered a wrong action.")
    print(50 * "*")
    print(f"PC choice was {pc}")
    print(f"Player choice was {player}")