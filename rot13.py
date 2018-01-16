#!/usr/bin/env python
# -*- coding: utf-8 -*-
from string import ascii_lowercase as alc, ascii_uppercase as auc, maketrans
# made by using
# a = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
# generate b by passing a to another func or online :D
# b = 'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm'
# and just dict(zip([i for i in a], [i for i in b]))

letterDict = {'A': 'N', 'C': 'P', 'B': 'O', 'E': 'R', 'D': 'Q',
              'G': 'T', 'F': 'S', 'I': 'V', 'H': 'U', 'K': 'X', 'J': 'W',
              'M': 'Z', 'L': 'Y', 'O': 'B', 'N': 'A', 'Q': 'D', 'P': 'C',
              'S': 'F', 'R': 'E', 'U': 'H', 'T': 'G', 'W': 'J', 'V': 'I',
              'Y': 'L', 'X': 'K', 'Z': 'M', 'a': 'n', 'c': 'p', 'b': 'o',
              'e': 'r', 'd': 'q', 'g': 't', 'f': 's', 'i': 'v', 'h': 'u',
              'k': 'x', 'j': 'w', 'm': 'z', 'l': 'y', 'o': 'b', 'n': 'a',
              'q': 'd', 'p': 'c', 's': 'f', 'r': 'e', 'u': 'h', 't': 'g',
              'w': 'j', 'v': 'i', 'y': 'l', 'x': 'k', 'z': 'm'}


def rot13Lazy(strng):  # the lazy :D
    res = ''
    for char in strng:
        res += letterDict[char] if char.isalpha() else char
    return res


lowerAl = 'abcdefghijklmnopqrstuvwxyz'


def rot13Math(n, text):  # math's guy favorite
    res = ''
    for l in text:
        try:
            rotted = lowerAl[(lowerAl.index(l.lower()) + n) % 26]
            res += rotted if l.islower() else rotted.upper()
        except ValueError:
            res += l
    return res


def rotNoneliner(n, text):  # the oneliner..
    return text.translate(maketrans(alc + auc, alc[n:] + alc[:n]
                                    + auc[n:] + auc[:n]))

# The fastest of all is the oneliner with 2nd place the lazy..see tests @-bench


if __name__ == '__main__':
    while True:
        try:
            print rotNoneliner(13, raw_input('Enter text to "encrypt" '))
        except (KeyboardInterrupt, EOFError):
            print '\nQuitting..'
            quit(0)
