"""
    Without using functions mentioned on lecture
"""

from random import randrange

def main():
    list_one = []
    list_two = []
    list_three = []

    lists = [
        list_one,
        list_two,
        list_three
    ]

    for list_ind in lists:
        for _ in range(randrange(10, 20)):
            ranom_number = randrange(1, 10)
            list_ind.append(ranom_number)

    len_list_one = len(list_one)
    len_list_two = len(list_two)
    len_list_three = len(list_three)

    print(f"List 1: {list_one}")
    print(f"List 2: {list_two}")
    print(f"List 3: {list_three}")

    sums = []

    for i in range(max(len_list_one, len_list_two, len_list_three)):
        sum_ = 0
        if i < len_list_one:
            sum_ += list_one[i]
        if i < len_list_two:
            sum_ += list_two[i]
        if i < len_list_three:
            sum_ += list_three[i]
        sums.append(sum_)
        
    print(f"Sums: {sums}")
if __name__ == "__main__":
    main()
