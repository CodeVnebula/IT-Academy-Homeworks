LETTERS = 'abcdefghijklmnopqrstuvwxyz'

string =  input("Input: ").strip()

for character in string:
    if character.lower() not in LETTERS:
        string = string.replace(character, '')
isPalindrome = True
for i in range(0, len(string) // 2):
    if string[i].lower() != string[len(string) - i - 1].lower():
        isPalindrome = False
        break

print('Output: Is palindrome') if isPalindrome == True else print('Output: Is not palindrome')
