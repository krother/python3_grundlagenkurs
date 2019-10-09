
import string

abc = string.ascii_lowercase
coded = abc[-8:] + abc[:-8]

chiffre = dict(zip(abc, coded))

text = input('enter sentence to code: ')
print(''.join([chiffre.get(c, '-') for c in text.lower()]))
