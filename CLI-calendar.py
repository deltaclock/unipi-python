#!/usr/bin/env python
# -*- coding: utf-8 -*-
# simple port of linux cal in python...
# python 2.7 supports directory comprehension!!!!!
# we get the dict below with {v:k for k,v in enumerate(calendar.month_abbr)}

import calendar

monthsDict = {'Mar': 3, 'Feb': 2, 'Aug': 8,
              'Sep': 9, 'Apr': 4, 'Jun': 6,
              'Jul': 7, 'Jan': 1, 'May': 5,
              'Nov': 11, 'Dec': 12, 'Oct': 10}


def handCraftedCalendar(monthN, yearN):
    # tabs needed.. else looks asymetrical..
    print '\t\t' + calendar.month_name[monthN] + '\t' + str(yearN) + '\n'
    print 'Su\tMo\tTu\tWe\tTh\tFr\tSa\n'
    monthData = calendar.monthrange(yearN, monthN)
    idx = monthData[0] + 1
    print ('\t' * idx if monthData[0] != 7 else 0),
    for date in range(monthData[1]):
        idx += 1
        if idx > 7:  # so it brakes on the saturday
            print '\n'
            idx = 1
        print str(date + 1) + '\t',


def CpythonCal(year, mon):
    # brainless but good looking..
    try:
        return calendar.TextCalendar(calendar.SUNDAY).formatmonth(year, mon)
    except ValueError:
        return 'Seriously?!..Negative Number!!'


if __name__ == '__main__':
    try:
        # title makes the first letter uppercase
        mon = monthsDict[raw_input('Enter the Month ')[:3].title()]
        year = int(raw_input('Enter the Year '))
    except KeyError:
        print 'Enter the Month Correctly!'
    except ValueError:
        print 'Thats NOT a valid Year'
    else:
        print '\n'
        handCraftedCalendar(mon, year)
        print '\n'  # cause..rip terminal
        # print CpythonCal(year, mon)
