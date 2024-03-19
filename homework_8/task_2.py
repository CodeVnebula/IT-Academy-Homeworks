while True:
    word = input("Enter just a word: ")
    if ' ' not in word:
        break

for i in range(len(word)):
    if word[i] not in ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']:
        print(word[i], end='')
