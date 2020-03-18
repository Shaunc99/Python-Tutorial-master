print("Hi!")

while True:
    num1 = input("Enter a number: ")
    num2 = input("Enter another number: ")
    option = input("What do you want to do? 'Type add, subtract, multiply, or divide' ")

    if option == "divide":
        print(float(num1) / float(num2))
    if option == "multiply":
        print(float(num1) * float(num2))
    if option == "add":
        print(float(num1) + float(num2))
    if option == "subtract":
        print(float(num1) - float(num2))
    program_option = input("Press enter to start another operation or 'q' to quit the calculator.")
    if program_option == "q":
        break

