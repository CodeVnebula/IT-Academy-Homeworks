def cel_to_fah(celsius):
    return celsius * 9/5 + 32

def fah_to_cel(fahrenheit):
    return (fahrenheit - 32) * 5/9

def main():
    print(cel_to_fah(30))  # Expected output: 86
    print(cel_to_fah(-10))  # Expected output: 14
    print(cel_to_fah(100))  # Expected output: 212
    print(fah_to_cel(86))  # Expected output: 30
    print(fah_to_cel(32))  # Expected output: 0
    print(fah_to_cel(212))  # Expected output: 100


if __name__ == "__main__":
    main()
   