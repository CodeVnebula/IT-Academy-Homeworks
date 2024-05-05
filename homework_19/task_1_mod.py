from random import randint

numbers_amount = {"Even" : 0, "Odd" : 0}

def main():
    print(f"Dictionary before: {numbers_amount}")
    
    for _ in range(100):
        random_number = randint(1, 1000)
        if random_number % 2 == 0:
            numbers_amount["Even"] += 1
        else:
            numbers_amount["Odd"] += 1
    print(f"Even numbers generated: {numbers_amount['Even']}, Odd numbers generated: {numbers_amount['Odd']}")
    
    print(f"Dictionary after: {numbers_amount}") 

    
if __name__ == "__main__":
    main()
