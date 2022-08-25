
string = "ABC for the purpose of LetterCounting program"
slowa = 1
litery = 0
hash_table = {}
for char in string:
    char = char.lower()
    if char == ' ':
        slowa += 1
    else:
        litery += 1
        if char in hash_table:
            hash_table[char]+=1
        else:
            hash_table[char]=1
print('Słowa: {}, Litery {}, Freq {}'.format(slowa, litery, hash_table))                
    
    
