i = 1
while i < 10:
    j = 1
    while j < i + 1:
        result = i * j
        print(j, " x ", i, " = ", result, end="    ")
        
        if result < 10:             # Again this thing does nothing to code
            print(' ', end='')      # Implemented just for better output readability
        j += 1
    i += 1
    print()
