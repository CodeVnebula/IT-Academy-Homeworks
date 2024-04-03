while True:
    word = input("Enter just a word: ")
    if ' ' not in word:
        break
if len(word) % 2 == 0:
    print(word[0] * 5)
    print((word[len(word)//2 - 1] + word[len(word)//2 + 1]) * 5)
    print(word[len(word) - 1] * 5)
else:
    print(word[0] * 5)
    print(word[len(word) // 2] * 5)
    print(word[len(word) - 1] * 5)
