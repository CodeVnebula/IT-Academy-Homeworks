while True:
    word = input("Enter just a word: ")
    if ' ' not in word:
        break

i = 0
while i < len(word):
    if len(word) % 2 == 0:
        if i == 0:
            print(word[i] * 5)
        elif i == len(word) - 1:
            print(word[i] * 5)
        elif i == len(word) // 2 - 1:
            print((word[i] + word[i + 1]) * 5)
    else:
        if i == 0:
            print(word[i] * 5)
        elif i == len(word) - 1:
            print(word[i] * 5)
        elif i == len(word) // 2:
            print(word[i] * 5)
    i += 1
