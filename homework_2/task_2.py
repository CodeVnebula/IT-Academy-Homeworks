a = int(input("Enter A: "))
b = int(input("Enter B: "))

if b != 0:
    if a % b == 0:
        print("A is a multiple of B")
    else:
        print("A is not a multiple of B")
else:
    print("Can't divide by 0! Enter B again.")


    