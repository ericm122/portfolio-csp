print ( "Welcome Preschoolers to Simple Calculatoor")


def simplecalculator():
    while True:

        print("Enter an operation: ")
        print("""1.Addition
    2.Subtration
    3.Division
    4.Multiplication
    5.Quit""")

        def add(num1,num2):
            result= num1 + num2
            print ("The result is: " + str(result))
        def subtract(num1,num2):
            result= num1 - num2
            print ("The result is: " + str(result))
        def divide(num1,num2):
            result= num1 / num2
            print ("The result is: " + str(result))
        def multiply(num1,num2):
            result= num1*num2
            print ("The result is: " + str(result))

        operation = int(input("(1-5)Operation: "))

        if operation == 1: #True
            int1 = int(input("Enter your first number: "))
            int2 = int(input("Enter your second number: "))
            add(int1, int2)

        elif operation ==2:
            int1 = int(input("Enter your first number: "))
            int2 = int(input("Enter your second number: "))
            subtract(int1, int2)

        elif operation ==3:
            int1 = int(input("Enter your first number: "))
            int2 = int(input("Enter your second number: "))
            divide(int1, int2)

        elif operation ==4:
            int1 = int(input("Enter your first number: "))
            int2 = int(input("Enter your second number: "))
            multiply(int1, int2)

        elif operation ==5:
            break

simplecalculator()
