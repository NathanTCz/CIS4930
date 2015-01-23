from __future__ import print_function
import sys
import string

def rm_dups(keyword):
    no_dups = []
    for x in keyword:
        if x not in no_dups:
            no_dups.append(x)
    return no_dups

lower_alpha = [x for x in string.ascii_lowercase]
characters = []

with open( sys.argv[1], 'r' ) as file:
    for line in file:
        for char in line:
            characters.append(char)

keyword = rm_dups([x for x in raw_input('Please enter a keyword for the mixed cipher: ')])

cipher_alpha = rm_dups( keyword + lower_alpha )
ciphered_file = []
for char in characters:
    if char == ' ' or char == '.':
        ciphered_file.append(char)
    elif char.islower():
        ciphered_file.append( cipher_alpha[ lower_alpha.index(char) ] )
    elif char.isupper():
        ciphered_file.append( cipher_alpha[ lower_alpha.index( char.lower() ) ].upper() )

print('Plaintext:   ', end='')
print(('').join(lower_alpha))
print('Ciphertext:  ', end='')
print(('').join(cipher_alpha))
print(('').join(ciphered_file))
