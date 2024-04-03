string = input("Enter a text: ")
print()
for i in range(0, len(string), 2):
    if string[i] not in ['e', 'E']:
        print(string[i], end='')
