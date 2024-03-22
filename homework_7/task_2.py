while True:
    n = int(input("Enter number: "))
    if n > 0 and n <= 1000:
        break
print(n, end="")
i = 0
while n != 1:
    if n % 2 == 0:
        n = n // 2
    else:
        n = (n * 3) + 1
    print(" ->", n, end="")
    i += 1  
