
import random

print("Welcome to the rock papper scissors game." )

#Players choice
win = 0
lose = 0

while True:
    print("Please select one of the following")
    choice = input("Rock, Paper, or Scissor?").lower()

    #Computer's choice
    # = gets the value of
    # == is equal to


    computer = random.randint(1, 3)



    if computer == 1:
        computer = "rock"
        print("Computer chose rock")
    elif computer == 2:
        computer = "paper"
        print("Computer chose paper")

    else:
        computer = "scissor"
        print("Computer chose scissor")

    #determine the outcome

    if choice == "rock" and computer == "rock":
        print ("This is a tie!" )
    elif choice == "rock" and computer =="paper":
        print ("You win!")
        win = win + 1
    elif choice == "rock" and computer == "scissor":
        print ("You lose!")
        lose = lose + 1

    elif choice == "paper" and computer == "rock":
        print ("You win!" )
        win = win + 1

    elif choice == "paper" and computer =="paper":
        print ("This is a tie!")
    elif choice == "paper" and computer == "scissor":
        print ("You lose!")
        lose = lose + 1

    elif choice == "scissor" and computer == "rock":
        print ("You lose!" )
        lose = lose + 1

    elif choice == "scissor" and computer == "paper":
        print ("This win!")
        win = win + 1

    elif choice == "scissor" and computer == "scissor":
        print ("This is a tie!")

    print ("Player:  "  +  str(win) + "///" +  "Computer :  " +  str(lose))

    playagain= input("Would you like to play again?")
    if playagain == "yes":
        print("Restarting . . . . ")
    elif playagain == "no":
        break
