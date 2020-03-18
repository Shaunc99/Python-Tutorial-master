import cv2
from roku import Roku
roku= Roku("192.168.0.183")

while True:
    print("Enter A for left navigation")
    print("Enter D for right navigation")
    print("Enter W for up navigation")
    print("Enter S for down navigation")
    print("Enter H for home navigation")

    user_choice = input("Enter your choice key:")
    if user_choice == "A":
        roku.left()
    elif user_choice == "D":
        roku.right()

    elif user_choice == "W":
        roku.up()
    elif user_choice == "S":
        roku.down()
    elif user_choice == "H":
        roku.home()
    elif user_choice == "B":
        roku.back()
    elif user_choice == "":
        roku.select()
    elif user_choice == "I":
        roku.info()
    elif user_choice == "F":
        roku.forward()
    elif user_choice == "L":
        roku.literal('Tek savvy')
    elif user_choice == "C":
        roku.backspace()
    elif user_choice == "V":
        roku.search()
    elif user_choice == "break":
        break