from random import randint

def generate_computer_action():
    action_number = randint(1, 3)
    if action_number == 1:
        return "R"
    elif action_number == 2:
        return "S"
    else:
        return "P"

def main():
    print()
    print("      Welcome To")
    print("ROCK - PAPER - SCISSORS\n")
    your_move = input("Enter 'R'- for Rock, 'S'- for Scissors, 'P'- for Paper: ").upper()
    tries_for_input = 3
    while your_move not in ['R','S','P']:
        tries_for_input -= 1
        if tries_for_input == 0:
            print("Quiting the game!\n\n")
            return
        print(f"You have {tries_for_input} tries to enter correct move!")
        your_move = input("Please enter only 'R'- for Rock, 'S'- for Scissors, 'P'- for Paper: ")
        


    computer_move = generate_computer_action()

    print(f"Your move: {your_move} |||  Computer move: {computer_move} \n")
    if your_move == "R" and computer_move == "S":
        print("You win!\n\n")

    elif your_move == "S" and computer_move == "P":
        print("You win!\n\n")

    elif your_move == "P" and computer_move == "R":
        print("You win!\n\n")
    
    elif your_move == "P" and computer_move == "P" \
    or your_move == "S" and computer_move == "S" \
    or your_move == "R" and computer_move == "R":
        print("It's a draw!\n\n")
    else:
        print("Computer win!\n\n")

if __name__ == "__main__":
    main()
