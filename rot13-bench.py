#!/usr/bin/env python
# -*- coding: utf-8 -*-
# BUT WHY!! curiosity,fun, speed paranoia
from random import choice
import string
import timeit
from time import time
import rot13
import matplotlib.pyplot as plt
import numpy as np

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
print 'Time required to make\
 a list of {:d} strings {:.10f}'.format(number_of_runs, time() - ts)


def benchLazy(text):
    rot13.rot13Lazy(text)


def benchLazyV2(text):
    rot13.rot13LazyV2(text)


def benchMath(text):
    rot13.rot13Math(13, text)


def benchrotNoneliner(text):
    rot13.rotNoneliner(13, text)


def graph(performanceList):
    # Restore the rc params from Matplotlib’s internal defaults.
    plt.rcdefaults()
    plt.style.use('ggplot')
    fig, ax = plt.subplots(figsize=(18, 7))  # max screen width
    plt.subplots_adjust(left=0.05, right=0.95, top=0.9, bottom=0.1)

    funcs = ('Lazy', 'LazyV2', 'Math', 'Strings')
    y_pos = np.arange(len(funcs))

    ax.barh(y_pos, performanceList, align='center',
            color='dodgerblue')
    ax.set_yticks(y_pos)
    ax.set_yticklabels(funcs)
    ax.invert_yaxis()  # labels read top-to-bottom
    ax.set_xlabel('seconds (less is better)')
    ax.set_title('Time each function took to complete')
    ax.set_xlim([0, performanceList[2]])

    plt.show()


def tests():

    print 'Note the test will run 3 times x {} times for each test.. \
So the result is the best of 3!\n'.format(number_of_runs)

    lazy = min(timeit.repeat(
        "benchLazy(random_strings[i]); i += 1",
        "from __main__ import benchLazy, random_strings; i = 0",
        number=number_of_runs))

    print 'Using the dictionary we got {:d} sec\
 for {:.10f} loops\n'.format(number_of_runs, lazy)

    lazyV2 = min(timeit.repeat(
        "benchLazyV2(random_strings[i]); i += 1",
        "from __main__ import benchLazyV2, random_strings; i = 0",
        number=number_of_runs))

    print 'Using the dict \w all the printable chars\
 we got {:d} sec for {:.10f} loops\n'.format(number_of_runs, lazyV2)

    math = min(timeit.repeat(
        "benchMath(random_strings[i]); i += 1",
        "from __main__ import benchMath, random_strings; i = 0",
        number=number_of_runs))

    print 'Using the modulo we got {:d} sec\
 for {:.10f} loops\n'.format(number_of_runs, math)

    strPacket = min(timeit.repeat(
        "benchrotNoneliner(random_strings[i]); i += 1",
        "from __main__ import benchrotNoneliner, random_strings; i = 0",
        number=number_of_runs))

    print 'Using the string.translate module we got {:d} sec\
 for {:.10f} loops\n'.format(number_of_runs, strPacket)

    return [lazy, lazyV2, math, strPacket]


if __name__ == '__main__':
    try:
        if raw_input('This script will benchmark all 4 of the ROT functions..\
                     \nThis might take a while..\
 Continue? [y/n] ').lower() == 'y':

            res = tests()

            if raw_input('Do you also want a\
 diagram of the above numbers? [y/n] ').lower() == 'y':

                graph(res)
    except (KeyboardInterrupt, EOFError):
        print '\nQuitting..'
        quit(0)
