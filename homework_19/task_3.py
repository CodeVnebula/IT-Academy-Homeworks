friends_dict = {}
friends_list = []

def adding_friends_logic(friend1, friend2):
    if friend1 not in friends_dict:
        friends_dict[friend1] = friend2
    else:
        friends_dict[friend1] += ", " + friend2
    if friend2 not in friends_dict:
        friends_dict[friend2] = friend1
    else:
        friends_dict[friend2] += ", " + friend1

def check_input_format(user_input):
    
    if "-" not in user_input:
        return False
    else:
        names = user_input.split("-") 
    if len(names) != 2:
        return False
    if len(names[0]) < 1 or len(names[1]) < 1:
        return False
    return True
    
def main():
    while True:
        user_input = input("Input e.g 'name1-name2': ")
        if user_input.upper() == "FINISH":
            break
        if check_input_format(user_input):
            friends_list.append(user_input)
        else:
            print("Wrong format of input. Try again!")
        
    for i in range(len(friends_list)):
        friend1, friend2 = friends_list[i].split('-')
        friend1 = friend1.capitalize().strip()
        friend2 = friend2.capitalize().strip()
        adding_friends_logic(friend1=friend1, friend2=friend2)
        
    for key, value in friends_dict.items():
        print(f"{key} - {value}")
    
if __name__ == "__main__":
    main()
