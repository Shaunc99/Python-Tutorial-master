
# code written by: Shayan Qureshi on March 07, 2020
# the program will print table between 1 and 20 and will terminate when the user will enter the 'q'
import datetime
import json
while True:
    try:
        user_num = input("Enter a number between 1 and 20 or press 'q' to quit:")

        # quit program if the user enter 'q'
        if user_num == "q":
            print ("thanks for using the program!")
            break
        # else move forward and print table
        user_num= int(user_num)

        # keep asking user for the valid number
        while not (user_num > 0 and user_num < 21):
            user_num = int(input("Wrong number, please enter a number, it should be between 1 and 20:"))

        # print table with the user input number
        table = str(datetime.datetime.now().date()) + "\n"
        for i in range(1, 11):
            multiple = (user_num * i)
            # table = table + str(user_num) + " x " + str(i) + " = " + str(multiple) + "\n"
            table = table + str(user_num) + "," + str(i) + "," + str(multiple) + "\n"
        print(table)
        json.dumps(table)
        file = open("table","w")
        file.write(table)
        file.close()

    except ValueError:
        print("please enter a number")
