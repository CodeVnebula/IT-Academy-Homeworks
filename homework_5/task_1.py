while True:
    n = int(input("Enter n [1/49]: "))
    if n > 0 and n < 50:
        break

for i in range(1, n + 1):
    if i < 10:                          # Code from ln.7 to ln.10 does absolutely nothing 
        print(' ', i, " - ", end="", sep="")     # but I implemented This part just for better readability 
    else:                               # Of given results in the end (As we aren't focused on efficiency)
        print(i, " - ", end="", sep="")

    count = 0
    for j in range(1, i + 1):
        if i % j == 0:
            count += 1                  # As asked we need to print only 3 divisors of num so this variable is
            if count <= 3:              # for checking how many times did we print a divisor already 
                print(j, end=" ")
    print()
