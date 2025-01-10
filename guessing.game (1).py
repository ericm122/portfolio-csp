import random

print ("Welcome to the Guessing Game")
print("Choose difficulty easy, medium, or hard")


easy = random.randint(0,10)
medium = random.randint(0,50)
hard = random.randint(0,100)


def difficulty():
    diff = (input("Please choose your difficulty (easy, medium, or hard): "))
    if diff == "easy":
        question =  int(input("Please enter a number 0-10 "))
        if question == easy:
            print ("Congrats, you are correct")
        else:
            print ("You are incorrect, try again" )
            if question > easy:
                print ("The guess was too high, would you like to play again?")
            else:
                print ("The guess was too low, would you like to play again?")

    if diff == "medium":
        question =  int(input("Please enter a number 0-50 "))
        if question == medium:
            print ("Congrats, you are correct")
        else:
            print ("You are incorrect, try again" )
            if question > medium:
                print ("The guess was too high, would you like to play again?")
            else:
                print ("The guess was too low, would you like to play again?")

    if diff == "hard":
        question =  int(input("Please enter a number 0-100 "))
        if question == hard:
            print ("Congrats, you are correct" )
        else:
            print ("You are incorrect, try again" )
            if question > hard:
                print ("The guess was too high, would you like to play again?")
            else:
                print ("The guess was too low, would you like to play again?")


def again():
    tryagain = input("Would you like to play again? (yes or no) ")
    if tryagain == "yes":
        difficulty()
    else:
        print("Goodbye")


difficulty()
again()

