def moved_string(string):
    return string[1:] + string[0]    # In this case we need the first char to move
                                    # to the end of the string on each iteration
def compare_strings(string_a, string_b):
    is_possible = False
    original_string = string_a
    for _ in range(len(string_a)):
        string = moved_string(string_a)
        if string_b.lower() == string.lower():
            is_possible = True
            break
        string_a = string
    string_a = original_string      # needed original_string variable to store string_a value
    return is_possible              # for possible future useage
                                       
def main():
    string_a = input("Input a: ").strip()
    string_b = input("Input b: ").strip()   # To remove extra spaces top/bottom
    
    while not string_a.isalpha() or not string_b.isalpha():     # Used isalpha() as suggested
        print("Error: Please enter only alphabetic characters.")
        string_a = input("Input a: ").strip()
        string_b = input("Input b: ").strip()

    if len(string_a) == len(string_b):
        result = "YES" if compare_strings(string_a, string_b) else "NO"
        print(f'Output: {result}')
    else:
        print('Output: NO')

if __name__ == "__main__":
    main()
