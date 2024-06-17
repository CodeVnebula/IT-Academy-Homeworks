from random import randint

def main():
    random_numbers = []

    for _ in range(100):
        random_number = randint(10, 999999999)
        random_numbers.append(random_number)

    numbers_sorted_ascending = sorted(random_numbers ,key=lambda item: len(str(item)), reverse = False)
    numbers_sorted_descending = sorted(random_numbers ,key=lambda item: len(str(item)), reverse = True)
    minimum_length_number = min(random_numbers)
    maximum_length_number = max(random_numbers)

    print(f"\nList sorted in ascending way:\n {numbers_sorted_ascending} \n\n")
    print(f"List sorted in descending way:\n {numbers_sorted_descending}\n\n")
    print(f"Shortest element in list (could be more than one): {minimum_length_number}\n")
    print(f"Longest element in list (could be more than one): {maximum_length_number}\n")

if __name__ == "__main__":
    main()
