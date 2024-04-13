def to_upper(given_list):
    up_case_list = []
    for item in given_list:
        up_case_list.append(item.upper())
    return up_case_list

def remove_short_strings(given_list):
    new_list = []
    for item in given_list:
        if len(item) >= 3:
            new_list.append(item)
    return new_list

def main():
    random_strings = ['ac', 'dg', 'hijk', 'lmno', 'pqrst', 'uvw', 'abcdef', 'il', 'mnsaopqr', 's', 'stuvwx']
    print("List before: ", random_strings)
    random_short_strings = remove_short_strings(random_strings)
    print("List after:", to_upper(random_short_strings))

if __name__ == "__main__":
    main()
