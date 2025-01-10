import random
import time

correct_answers = 0

print("Welcome to the multiplication quiz.")
num_questions = int(input("How many questions do you want to do?: "))

start_time = time.time()  # Start the timer

for i in range(num_questions):
    number1 = random.randint(1, 10)
    number2 = random.randint(1, 10)
    answer = number1 * number2

    print("Question " + str(i + 1) + ": What is " + str(number1) + " * " + str(number2) + "?")
    choice = input("Your answer: ")
    if int(choice) == answer:
        print("Correct!")
        correct_answers += 1
    else:
        print("Incorrect!")

end_time = time.time()  # End the timer
elapsed_time = end_time - start_time

print("Your score is " + str(correct_answers))
print("Elapsed time: " + str(elapsed_time) + " seconds")
