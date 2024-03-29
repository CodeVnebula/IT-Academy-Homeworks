import sys
LETTERS = 'abcdefghijklmnopqrstuvwxyz'

string_one = input('Input: ').strip()
string_two = input('Input: ').strip()

if len(string_one) != len(string_two):
    print("NO")
    sys.exit(0)

for character in string_one:
    if character.lower() not in LETTERS:
        string_one = string_one.replace(character, '')
for character in string_two:
    if character.lower() not in LETTERS:
        string_two = string_two.replace(character, '')
        
is_in = True
for char in string_two:
    if char.lower() not in string_one.lower():
        is_in = False
        break
    else:
        string_one = string_one.replace(char, '', 1)
print('Output: YES') if is_in == True else print('Output: NO')
