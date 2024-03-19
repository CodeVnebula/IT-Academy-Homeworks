string = input("Enter a text: ")
print()
for i in range(len(string)):
    if i % 2 == 0 and string[i] not in ['e', 'E']:
        print(string[i], end='')
