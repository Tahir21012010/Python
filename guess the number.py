import random
playig = True
number = str(random.randint(10,20))
print("I will generte a number from 10 to 20, and you have guess the number one digit at a time.")
while playig:
    guess = input("give me your best guess! \n")
    if guess == number:
        print("You win the game")
        print("the number was",number)
        break
    else:
        print("You guess isn't quite right, try again \n")