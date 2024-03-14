print()

while True:
    n = int(input("Enter n: "))
    if n > 0 and n < 10:
        break

print()

i = 0
while i <= n:
    print((n - i) * '  ', i, end='')
    j = i - 1
    while j >= 0:
        print('', j, end='')
        j -= 1
    k = 1
    while k <= i:
        print('', k, end='')
        k += 1
    
    print()
    i += 1

"""example:

          0
        1 0 1
      2 1 0 1 2
    3 2 1 0 1 2 3
  4 3 2 1 0 1 2 3 4
5 4 3 2 1 0 1 2 3 4 5

"""
