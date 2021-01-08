# https://www.grimmstories.com/de/grimm_maerchen/rotkaeppchen

import random
import sys

ALPHABET = 'abcdefghijklmnopqrstuvwxyzäöü.,!" \n'
CODE_CHARS = ALPHABET[:-6]
SUBST_PER_LEVEL = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

def clean(s):
    result = ""
    s = s.replace('ß', 'ss')
    for char in s.lower():
        if char in ALPHABET:
            result += char
        else:
            result += " "
    return result

def get_code(text, n):
    code = {}
    while len(code) < n:
        char = random.choice(CODE_CHARS)
        coded = random.choice(CODE_CHARS).upper()
        if char not in code \
           and char != coded.lower() \
           and char in text \
           and coded not in code.values():
                code[char] = coded
    return code

def apply_code(code, text):
    """return encoded text"""
    result = ""
    for char in text:
        result += code.get(char, char)
    return result


def play_level(text, ncoded, seed):
    text = text.strip()
    random.seed(seed)
    code = get_code(text, ncoded)
    text = clean(text)
    backup = apply_code(code, text)
    coded = backup

    while coded.lower() != text:
        print("\n" + coded)
        s = input("\nWelchen Buchstaben ersetzen? (# für neu anfangen)")
        if s == '#':
            coded = backup
        elif s == '!':
            print(code)
            coded = text
        else:
            t = input("\nWomit ersetzen? ")
            coded = coded.replace(s.upper(), t.lower())
        print('\n'*10)

    print(coded)
    print('\nGESCHAFFT!!!')
    y = input('\nnoch ein Level? (ja/nein)')
    if y.lower().startswith('n'):
        sys.exit(0)


text = open('geisslein.txt').read()
text = text.replace('\n', '\n\n')
text_pieces = text.split('----')

i = 1
for level in zip(text_pieces, SUBST_PER_LEVEL, range(1, 11)):
    print('-' * 40)
    print(f'    LEVEL {i}')
    print('-' * 40)
    play_level(*level)
    i += 1

print('ALLES GESCHAFFT')
