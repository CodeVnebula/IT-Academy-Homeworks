characters_amounts = {}

def main():
    string = input("Input: ")
    for char in string:
        if char in characters_amounts:
            characters_amounts[char] += 1
        else:
            characters_amounts[char] = 1
    
    for char, count in characters_amounts.items():
        print(f"{char} - {count}")

if __name__ == "__main__":
    main()
