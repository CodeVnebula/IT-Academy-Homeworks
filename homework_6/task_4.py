print()

while True:
    n = int(input("Enter n: "))
    if n > 0 and n < 10:
        break

print()

i = 1
while i < (n*2):
    j = 1
    if i <= n:                      # While i <= n rows will increase
        while j < i + 1:            # on each iteration of outer loop 
            print(j, end=" ")       
            j += 1
        print()
        
    else:
        while j <= n - (i - n):     # After i > n rows will decrease
            print(j, end=" ")       # on each iteration of outer loop
            j += 1
        print()
    i += 1
print()
