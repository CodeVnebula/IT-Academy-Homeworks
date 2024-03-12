PASSWORD = "passcode123"

print()

user_name = input("What's your name? ")

for attempt in range(3):
    entered_password = input("Please enter your password: ")
    if entered_password == PASSWORD:
        print("Welcome back,", user_name)
        break
    else:
        if attempt == 2:
            print("You have been trying to enter the wrong password for a few times.")
            print("You are blocked for a while.")
        else:
            print("Invalid password. Please try again.")

print()
