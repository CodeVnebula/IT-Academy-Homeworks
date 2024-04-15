def main():
    name = input("Enter your name: ")
    surname = input("Enter your surname: ")
    age = int(input("Enter your age: "))

    if age <= 0:
        print("You have not been born yet!")    
        return

    print(f"Hello {name} {surname}.")
    print(f"Age: {age}")

if __name__ == "__main__":
    main()
