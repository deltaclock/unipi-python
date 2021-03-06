#!/usr/bin/env python
# -*- coding: utf-8 -*-
# unicode for some weird roman numbers..
# please set your terminal charset to utf-8
romanNums = ((u'\u2188 ', 100000), (u'\u2187 ', 50000),
             (u'\u2181 ', 10000), (u'\u2180 ', 5000),
             ('M', 1000), ('CM', 900), ('D', 500),
             ('CD', 400), ('C', 100), ('XC', 90),
             ('L', 50), ('XL', 40), ('X', 10),
             ('IX', 9), ('V', 5), ('IV', 4), ('I', 1))


def int2roman(num):
    resStr = ''
    for letter, numValue in romanNums:
        while num >= numValue:
            resStr += letter
            num -= numValue
    return resStr

# confirm with http://www.tuomas.salste.net/doc/roman/numeri-romani.html


if __name__ == '__main__':
    while True:
        try:
            numN = int(raw_input('Enter a number '))
            if len(str(numN)) > 10 or numN <= 0:
                print 'Romans didnt knew that number...'
            else:
                print int2roman(numN).encode('utf-8')
        except ValueError:
            print 'ONLY integers...'
        except (KeyboardInterrupt, EOFError):
            print '\nQuitting..'
            quit(0)
