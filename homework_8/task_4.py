row_one = 'qwertyuiop'
row_two = 'asdfghjkl'
row_thr = 'zxcvbnm'
letters = row_one + row_two + row_thr

KEY = 1

while True:
    encrypt_or_decrypt = input("Enter action (e/d): ").lower()
    if encrypt_or_decrypt in ['e', 'd']:
        break

string = input('Enter text: ').lower()
  
for i in range(len(string)):
    letters_index = -1
    character = ''

    if string[i] not in letters:
        character = string[i]
        
    if encrypt_or_decrypt == 'e':
        if string[i] in row_one:
            letters_index = row_one.index(string[i])
            letters_index = (letters_index + KEY) % len(row_one)    
            character = row_one[letters_index]
        elif string[i] in row_two:
            letters_index = row_two.index(string[i])
            letters_index = (letters_index + KEY) % len(row_two)  
            character = row_two[letters_index]   
        elif string[i] in row_thr:
            letters_index = row_thr.index(string[i])
            letters_index = (letters_index + KEY) % len(row_thr) 
            character = row_thr[letters_index] 
            
    else:
        if string[i] in row_one:
            letters_index = row_one.index(string[i])
            letters_index = ((letters_index - KEY) + len(row_one)) % len(row_one)
            character = row_one[letters_index]
        elif string[i] in row_two:
            letters_index = row_two.index(string[i])
            letters_index = ((letters_index - KEY) + len(row_two)) % len(row_two)  
            character = row_two[letters_index]   
        elif string[i] in row_thr:
            letters_index = row_thr.index(string[i])
            letters_index = ((letters_index - KEY) + len(row_thr)) % len(row_thr) 
            character = row_thr[letters_index]
    print(character, end='')
