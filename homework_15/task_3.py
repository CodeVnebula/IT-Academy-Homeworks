def rotate_str_recurs(passed_str):
    if len(passed_str) == 0:
        return passed_str
    return rotate_str_recurs(passed_str[1:]) + passed_str[0]

def main():
    print(rotate_str_recurs('rare'))
    print(rotate_str_recurs('python'))
    print(rotate_str_recurs('rotate'))

if __name__ == "__main__":
    main()
