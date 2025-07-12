import random
options = ["rock", "paper", "scissors"]
computer_choice = random.choice(options)
print(computer_choice)
user_choice = input("choose rock, paper, or scissors: ")
print("you chose:", user_choice)
print("computer chose:", computer_choice)
if user_choice == computer_choice:
    print("It's a tie!")
elif user_choice == "rock" and computer_choice == "scissors":
    print("Rock smashes scissors! You win!")

elif user_choice == "paper" and computer_choice == "rock":
    print("Paper covers rock! You win!")

elif user_choice == "scissors" and computer_choice == "paper":
    print("Scissors cut paper! You win!")

else:
    print("You lose! ")
