LETTERS = 'abcdefghijklmnopqrstuvwxyz'

string_one = input('Input: ').strip()
string_two = input('Input: ').strip()

for character in string_one:
    if character.lower() not in LETTERS:
        string_one = string_one.replace(character, '')
for character in string_two:
    if character.lower() not in LETTERS:
        string_two = string_two.replace(character, '')
isIn = True
for char in string_two:
    if char.lower() not in string_one.lower():
        isIn = False
        break
    else:
        string_one = string_one.replace(char, '', 1)
print('Output: YES') if isIn == True else print('Output: NO')
