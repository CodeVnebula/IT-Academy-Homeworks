from task_1 import calc_gcd_iter

def calc_lcm_iter(a: int, b: int):
    return (a * b) // calc_gcd_iter(a, b)

def main():
    while True:
        a = int(input("Enter a: "))
        if 0 < a <= 10000:
            break
    
    while True:
        b = int(input("Enter b: "))
        if 0 < b <= 10000:          # pirobashi 0 < b < 10000 ewera magalitshi b iyo 10000 amitom <=
            break
    
    lcm_iter = calc_lcm_iter(a, b)
    print(f'LCM of {a} and {b} is {lcm_iter}')

if __name__ == "__main__":
    main()
