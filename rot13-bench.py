#!/usr/bin/env python
# -*- coding: utf-8 -*-
# BUT WHY!! curiosity,fun, speed paranoia
from random import choice
import string
import timeit
import rot13

'''
++++++++
Results
++++++++
This script will benchmark all 3 of the ROT functions..
This might take a while.. Continue? [y/n]y
Note the test will run 3 times x 10000 times for each test..
So the result is the best of 3!

Using the dictionary we got 3.2093930244 sec for 10000 loops

Using the dict \w all the printable charswe got 2.9111669064 sec for 10000loops

Using the modulo we got 6.3325240612 sec for 10000 loops

Using the string.translate module we got 2.5084860325 sec for 10000 loops

'''


# for benchmarking..
# a random string combination of digits, letters, punctuation, and ' '.
def benchLazy():
    randString = ''.join(choice(string.printable) for _ in range(1000))
    rot13.rot13Lazy(randString)


def benchLazyV2():
    randString = ''.join(choice(string.printable) for _ in range(1000))
    rot13.rot13LazyV2(randString)


def benchMath():
    randString = ''.join(choice(string.printable) for _ in range(1000))
    rot13.rot13Math(13, randString)


def benchrotNoneliner():
    randString = ''.join(choice(string.printable) for _ in range(1000))
    rot13.rotNoneliner(13, randString)


def tests():
    if raw_input('This script will benchmark all 3 of the ROT functions..\
                 \nThis might take a while.. Continue? [y/n]').lower() == 'y':

        print 'Note the test will run 3 times x 10000 times for each test.. \
So the result is the best of 3!\n'

        lazy = '{:.10f}'.format(min(timeit.repeat(
            "benchLazy()", "from __main__ import benchLazy", number=10000)))
        print 'Using the dictionary we got ' + lazy + ' sec for 10000 loops\n'

        lazyV2 = '{:.10f}'.format(min(timeit.repeat(
            "benchLazyV2()", "from __main__ import benchLazyV2", number=10000)))
        print 'Using the dict \w all the printable chars\
 we got ' + lazyV2 + ' sec for 10000 loops\n'

        math = '{:.10f}'.format(min(timeit.repeat(
            "benchMath()", "from __main__ import benchMath", number=10000)))
        print 'Using the modulo we got ' + math + ' sec for 10000 loops\n'

        strPacket = '{:.10f}'.format(min(timeit.repeat(
            "benchrotNoneliner()", "from __main__ import benchrotNoneliner",
            number=10000)))
        print 'Using the string.translate module we got ' + strPacket +\
            ' sec for 10000 loops\n'


if __name__ == '__main__':
    try:
        tests()
    except (KeyboardInterrupt, EOFError):
        print '\nQuitting..'
        quit(0)
