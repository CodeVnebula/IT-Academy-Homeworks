LETTERS = 'abcdefghijklmnopqrstuvwxyz'

string =  input("Input: ").strip()

for character in string:
    if character.lower() not in LETTERS:
        string = string.replace(character, '')
is_palindrome = True
for i in range(0, len(string) // 2):
    if string[i].lower() != string[len(string) - i - 1].lower():
        is_palindrome = False
        break

print('Output: Is palindrome') if is_palindrome == True else print('Output: Is not palindrome')
