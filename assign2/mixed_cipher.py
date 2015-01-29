'''
Nathan Cazell (ntc10)
1/21/15
'''

from __future__ import print_function
import sys
import string

def rm_dups(keyword):
    return [x for i, x in enumerate(keyword) if i is keyword.index(x)]

lower_alpha = [x for x in string.ascii_lowercase]

with open( sys.argv[1], 'r' ) as file:
    characters = [char for line in file for char in line]

keyword = rm_dups([x for x in raw_input('Please enter a keyword for the mixed cipher: ')])

cipher_alpha = rm_dups( keyword + lower_alpha )
ciphered_file = []
for char in characters:
    if char.islower():
        ciphered_file.append( cipher_alpha[ lower_alpha.index(char) ] )
    elif char.isupper():
        ciphered_file.append( cipher_alpha[ lower_alpha.index( char.lower() ) ].upper() )
    else:
        ciphered_file.append(char)

print('Plaintext:   ', end='')
print(('').join(lower_alpha))
print('Ciphertext:  ', end='')
print(('').join(cipher_alpha))
print(('').join(ciphered_file))
