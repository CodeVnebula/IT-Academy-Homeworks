def calc_gcd_recur(a: int, b: int):
    if a == b:
        return a
    elif a > b:
        return calc_gcd_recur(a - b, b)
    
    return calc_gcd_recur(a, b - a)

def main():
    while True:
        a = int(input("Enter a: "))
        if 0 < a <= 10000:
            break
    
    while True:
        b = int(input("Enter b: "))
        if 0 < b <= 10000:          # pirobashi 0 < b < 10000 ewera magalitshi b iyo 10000 amitom <=
            break
    
    gcd_recur = calc_gcd_recur(a, b)
    print(f'GCD of {a} and {b} is {gcd_recur}')

if __name__ == "__main__":
    main()