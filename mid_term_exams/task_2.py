def main():
    n = int(input("Enter n (100 <= n < 1000): "))

    if n < 100 or n >= 1000:
        print("You entered a wrong number!")
        return
    
    count_of_numbers = 0
    print(f"Numbers from 1 to {n} divided by 13: ", end="")
    for i in range (1, n):
        if i % 13 == 0:
            count_of_numbers += 1
            print(i, end=", ")
    
    print("\nAmount of numbers found that can be divided by 13:", count_of_numbers)

if __name__ == "__main__":
    main()
