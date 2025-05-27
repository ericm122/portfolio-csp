import random
import time
magic_list = ["It is certain", "It is decidedly so", "Without a doubt", "Yes definitely", "You may rely on it", "Reply hazy, try again", "Ask again later", "Better not tell you now", "Cannot predict now", "Concentrate and ask again", "Don’t count on it", "My reply is no", "My sources say no", "Outlook not so good", "Very doubtful"]

print("Welcome to the magic 8 ball.")

while True:
    try:


        x = input("Please Input a question for the magic 8 ball: (has to be a yes or no question) ")
        z = x.endswith("?")



        if z == True: #checks to see if the sentence ends with a question mark
            print ("shake...")
            time.sleep(2)
            print ("shake...")
            time.sleep(2)
            print ("shake...")
            time.sleep(2)
            print(random.choice(magic_list))
        y = input("Would you like to try again? (yes or no)  : ")


        if y == "no" or y == "n":     #if respsonse is no / n , then it will quit the program, else it reruns again
            print ("Have a good day!")
            break
        elif z == False:
            print("ERROR! Please enter a question!!")
    except:
        print("ERROR! Please enter a question!!")



