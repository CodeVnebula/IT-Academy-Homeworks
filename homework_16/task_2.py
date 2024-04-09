import random  

def main():
    my_list = []
    new_list = []  
    for _ in range(50):
        random_element = random.randrange(1, 29)
        my_list.append(random_element)
    
    for i in range(len(my_list)):
        for _ in range(0, my_list[i]):
            new_list.append(my_list[i])
    print(f"List - {new_list}")
    print(f"Length - {len(new_list)}")

if __name__ == "__main__":
    main()
