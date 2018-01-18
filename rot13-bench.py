#!/usr/bin/env python
# -*- coding: utf-8 -*-
# BUT WHY!! curiosity,fun, speed paranoia
from random import choice
import string
import timeit
from time import time
import rot13

'''
++++++++
Results
++++++++
Time required to make a list of 10000 strings  2.52859210968
This script will benchmark all 4 of the ROT functions..
This might take a while.. Continue? [y/n]y
Note the test will run 3 times x 10000 times for each test.. So the result
is the best of 3!

Using the dictionary we got 0.6673209667 sec for 10000 loops

Using the dict \w all the printable chars we got 0.3962030411 sec for
 10000 loops

Using the modulo we got 3.9189569950 sec for 10000 loops

Using the string.translate module we got 0.0100760460 sec for 10000 loops


'''

number_of_runs = 10000

ts = time()
random_strings = [''.join(choice(string.printable) for _ in range(1000))
                  for __ in range(number_of_runs)]
print 'Time required to make a list of 10000 strings ', time() - ts


def benchLazy(text):
    rot13.rot13Lazy(text)


def benchLazyV2(text):
    rot13.rot13LazyV2(text)


def benchMath(text):
    rot13.rot13Math(13, text)


def benchrotNoneliner(text):
    rot13.rotNoneliner(13, text)


def tests():
    if raw_input('This script will benchmark all 4 of the ROT functions..\
                 \nThis might take a while.. Continue? [y/n]').lower() == 'y':

        print 'Note the test will run 3 times x %i times for each test.. \
So the result is the best of 3!\n' % number_of_runs

        lazy = '{:.10f}'.format(min(timeit.repeat(
            "benchLazy(random_strings[i]); i += 1",
            "from __main__ import benchLazy, random_strings; i = 0",
            number=number_of_runs)))

        print 'Using the dictionary we got ' + lazy
        + ' sec for %i loops\n' % number_of_runs

        lazyV2 = '{:.10f}'.format(min(timeit.repeat(
            "benchLazyV2(random_strings[i]); i += 1",
            "from __main__ import benchLazyV2, random_strings; i = 0",
            number=number_of_runs)))

        print 'Using the dict \w all the printable chars\
 we got ' + lazyV2 + ' sec for %i loops\n' % number_of_runs

        math = '{:.10f}'.format(min(timeit.repeat(
            "benchMath(random_strings[i]); i += 1",
            "from __main__ import benchMath, random_strings; i = 0",
            number=number_of_runs)))

        print 'Using the modulo we got ' + math
        + ' sec for %i loops\n' % number_of_runs

        strPacket = '{:.10f}'.format(min(timeit.repeat(
            "benchrotNoneliner(random_strings[i]); i += 1",
            "from __main__ import benchrotNoneliner, random_strings; i = 0",
            number=number_of_runs)))

        print 'Using the string.translate module we got ' + strPacket +\
            ' sec for %i loops\n' % number_of_runs


if __name__ == '__main__':
    try:
        tests()
    except (KeyboardInterrupt, EOFError):
        print '\nQuitting..'
        quit(0)
