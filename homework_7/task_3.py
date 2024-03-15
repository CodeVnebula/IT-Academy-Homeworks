while True:
    n = int(input("enter number: "))
    if n >= 0 and n < 10000:
        break

sum_of_digits = 0
print("reversed number is ", end="")
while n > 0:
    sum_of_digits += n % 10
    print(n % 10, end="")           # reversing could be done easier maybe
    n = n // 10                     
print()

print("sum of digits:", sum_of_digits)
