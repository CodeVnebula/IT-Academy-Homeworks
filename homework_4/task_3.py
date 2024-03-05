while True:
    number = int(input("Enter number between 0-1000: "))
    if 0 < number < 1000: 
        break

for i in range(1, number + 1):
    if number % i == 0:
        print(i, end=" ")