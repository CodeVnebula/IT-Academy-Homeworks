while True:
    n = int(input("Enter n [1, 49]: "))
    if n > 0 and n < 50:
        break
left_side = '/'
right_side = "\\"
top = '*'
middle = '|'
for i in range(0, n):
    print((n - i) * ' ', end='')
    if i == 0:
        print(top, end='') 
    else:
        if i == n - 1:
            print(i * left_side + middle + i * right_side, "\n", (n - 1) * ' ' + middle, end='')
        else:
            print(i * left_side + middle + i * right_side, end='')

    print()
          