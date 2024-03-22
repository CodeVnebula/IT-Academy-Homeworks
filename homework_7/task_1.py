while True:
    n = int(input("Enter number: "))
    if n >= 0 and n < 20:
        break

first = 0
second = 1
next_num = 0

i = 0
while i < n:
    print(next_num, end=" ")
    first = second
    second = next_num 
    next_num = first + second  
    i += 1
