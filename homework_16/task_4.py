def merge_lists(list_one, list_two):
    mergred_list = []
    mergred_list = list_one + list_two
    length = len(mergred_list)
    
    for i in range(length):
        minimal = i
        for j in range(i+1, length):
            if mergred_list[j] < mergred_list[minimal]:
                minimal = j
        mergred_list[i], mergred_list[minimal] = mergred_list[minimal], mergred_list[i]

    return mergred_list  

def main():
    list_one = [1, 4, 7, 9, 14]
    list_two = [0, 5, 6, 11, 32, 54]
    print(merge_lists(list_one, list_two))
    
    list_three = [0, 3, 6, 9, 12]
    list_four = [1, 4, 7, 10, 13, 15]
    print(merge_lists(list_three, list_four))

    list_five = [100, 200, 300, 400, 500]
    list_six = [150, 250, 350, 450, 550, 600]
    print(merge_lists(list_five, list_six))

    list_seven = [-5, -3, 0, 2, 5]
    list_eight = [-10, -7, -4, -1, 1, 4]
    print(merge_lists(list_seven, list_eight))

    list_nine = [11, 13, 17, 19, 23]
    list_ten = [12, 14, 18, 20, 24, 25]
    print(merge_lists(list_nine, list_ten))

if __name__ == "__main__":
    main()
