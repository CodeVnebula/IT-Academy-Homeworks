from random import randint

numbers_amount = {"Even" : 0, "Odd" : 0}

def main():
    even_numbers_amount = 0
    odd_numbers_amount = 0
    for _ in range(100):
        random_number = randint(1, 1000)
        if random_number % 2 == 0:
            even_numbers_amount += 1
        else:
            odd_numbers_amount += 1
    print(f"Even numbers generated: {even_numbers_amount}, Odd numbers generated: {odd_numbers_amount}")
    print(f"Dictionary before: {numbers_amount}")
    
    numbers_amount["Even"] = even_numbers_amount
    numbers_amount["Odd"] = odd_numbers_amount
    
    print(f"Dictionary after: {numbers_amount}") 

    
if __name__ == "__main__":
    main()
