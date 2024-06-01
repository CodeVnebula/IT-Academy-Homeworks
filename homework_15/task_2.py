def is_prime(number):
    print(f"Num - {number} ", end="")
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True

def main():

    print(is_prime(2))
    print(is_prime(1))
    print(is_prime(5))
    print(is_prime(8))
    print(is_prime(-5))
    print(is_prime(17))
    print(is_prime(15))
    print(is_prime(54))

if __name__ == "__main__":
    main()
