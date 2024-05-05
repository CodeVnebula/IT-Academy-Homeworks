import random

def main():
    my_list = []
    for _ in range(50):
        random_element = random.randint(1, 29)
        my_list.append(random_element)
    print(f"List before {my_list}")

    new_list = []
    for element in my_list:
        if element not in new_list:
            new_list.append(element)
    print(f"List - {new_list}")
    print(f"Length - {len(new_list)}")

if __name__ == "__main__":
    main()
