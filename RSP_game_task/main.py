from random import randint

def get_computer_move():
    action_number = randint(1, 3)
    if action_number == 1:
        return "R"
    elif action_number == 2:
        return "S"
    else:
        return "P"
    
def get_user_move():
    user_move = input("Enter 'R'- for Rock, 'S'- for Scissors, 'P'- for Paper: ").upper()
    tries_for_input = 3
    while user_move not in ['R','S','P']:
        tries_for_input -= 1
        if tries_for_input == 0:
            print("Quiting the game!\n\n")
            exit(1)
        print(f"You have {tries_for_input} tries to enter correct move!")
        user_move = input("Please enter only 'R'- for Rock, 'S'- for Scissors, 'P'- for Paper: ").upper()
    return user_move

def get_winner() -> str:
    user_score = 0
    computer_score = 0
    
    while user_score < 3 and computer_score < 3:
        user_move = get_user_move()
        computer_move = get_computer_move()
        
        print(f"\nYour move: {user_move} |||  Computer move: {computer_move} \n")

        if user_move == "R" and computer_move == "S" or \
           user_move == "S" and computer_move == "P" or \
           user_move == "P" and computer_move == "R":
            user_score += 1
        elif user_move != computer_move:
            computer_score += 1
        print(f"Your Score: {user_score}\nComputer Score: {computer_score} \n")
    
    if user_score > computer_score:
        return "You win!"
    elif computer_score > user_score:
        return "Computer wins!"
    else:
        return "It's a draw!"


def main():

    print()
    print("      Welcome To")
    print("ROCK - PAPER - SCISSORS\n")

    winner = get_winner()
    print(winner)
    
if __name__ == "__main__":
    main()
