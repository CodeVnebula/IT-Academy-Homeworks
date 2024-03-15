for i in range(1, 10):
    for j in range(1, i + 1):
        result = i * j
        print(j, " x ", i, " = ", result, end="    ")
        
        if result < 10:             # Again this thing does nothing to code
            print(' ', end='')      # Implemented just for better output readability
    print()
