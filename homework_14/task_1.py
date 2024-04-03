def calc_gcd_iter(a: int, b: int):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a

def main():
    while True:
        a = int(input("Enter a: "))
        if 0 < a <= 10000:
            break
    
    while True:
        b = int(input("Enter b: "))
        if 0 < b <= 10000:          # pirobashi 0 < b < 10000 ewera magalitshi b iyo 10000 amitom <=
            break
    
    gcd_iter = calc_gcd_iter(a, b)
    print(f'GCD of {a} and {b} is {gcd_iter}')
    
if __name__ == "__main__":
    main()
    