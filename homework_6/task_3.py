import random
import sys

print()
computer_num = random.randint(0, 100)

attempts = 5# this is for counting wrong input attempts

tries_left = 10             # this counts if userinput is = or not to compnum
print("Tries left: ", tries_left)

while True:
    
    if tries_left == 0:
        print()
        print("Computer wins!")
        sys.exit(0)
    
    while True:
        user_number = int(input("     Enter your number [1, 99]: "))
        if user_number <= 0 or user_number >= 100:
            attempts -= 1
            if attempts == 0:
                print("You have entered a lot wrong numbers")
                sys.exit(0)
        else:
            break
    
    if user_number > computer_num:
        tries_left -= 1
        print("Too high!  You got ", tries_left, ' tries left',  end='')
    elif user_number == computer_num:
        print("You win!")
        break
    else:
        tries_left -= 1
        print("Too low!  You got ", tries_left, ' tries left',  end='')
print()
