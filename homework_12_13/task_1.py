def moved_string(string):
    return string[-1] + string[:-1]    # Each iteration need to start from last char
                                       # + Remaining string untill last char
def main():
    string = input("Input: ").strip()

    while not string.isalpha():
        print("Error: Please enter only alphabetic characters.")
        string = input("Input: ").strip()
    
    print('Output: ')
    original_string = string
    for _ in range(len(string)):
        new_string = moved_string(string)
        print(string)
        string = new_string
    string = original_string

if __name__ == "__main__":
    main()
