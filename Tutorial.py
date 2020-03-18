user_age = input("Hi, Enter your age please:")

if int(user_age) < 13:
    print("Hi young kid")
elif int(user_age) >= 13 and int(user_age) <= 20:
    print ("Hi teen")
elif int(user_age) > 20 and int(user_age) <= 30:
    print("Hi young man")
elif int(user_age) > 30 and int(user_age) <= 45:
    print("Hi sir")
else:
    print("Hi old man")