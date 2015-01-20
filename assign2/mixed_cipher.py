from __future__ import print_function
import sys
import string

def rm_dups(keyword):
    no_dups = []
    for x in keyword:
        if x not in no_dups:
            no_dups.append(x)
    return no_dups

upper_alpha = [x for x in string.ascii_uppercase]
lower_alpha = [x for x in string.ascii_lowercase]
characters = []

with open( sys.argv[1], 'r' ) as file:
    for line in file:
        for char in line:
            characters.append(char)

keyword = rm_dups([x for x in raw_input('Please enter a keyword for the mixed cypher: ')])

cipher_text_lower = rm_dups( keyword + lower_alpha )
cipher_text_upper = [x.upper() for x in cipher_text_lower]
ciphered_file = []
for key, char in enumerate(characters):
    if char == ' ' or char == '.':
        ciphered_file.append(char)
    elif char in lower_alpha:
        ciphered_file.append( cipher_text_lower[ lower_alpha.index(char) ] )
    elif char in upper_alpha:
        ciphered_file.append( cipher_text_upper[ upper_alpha.index(char) ] )

for x in ciphered_file:
    print(x, end='')
print()
