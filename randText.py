#!/usr/bin/env python
# -*- coding: utf-8 -*-
# first we will assume the input file is a txt because of course python cant
# read "words" of binary data files like pdf and doc..(at least with open/read)
# it can with the 'rb' flag but its pointless? ¯\_(ツ)_/¯
import random
import string
import sys


def scanFile(filePath):
    words = []
    try:
        with open(filePath, 'r') as fl:
            for line in fl:
                for word in line.strip().split():
                    if len(word) < 45 and word.islower() and word.isalpha():
                        # αποθηκεύονται όλες οι τριάδες των λέξεων
                        # όπως εμφανίζονται.
                        # islower() ==> κρατάμε μόνο τις λέξεις σε πεζά
                        words.append(word)
    except IOError:
        print 'No such file!!'
        quit(0)
    return words


def storeInTriplets(wordList):
    # creating the triplets
    return [[wordList[j], wordList[j + 1], wordList[j + 2]]
            for j in xrange(0, len(wordList) - 2)]


def validTriplets(tripleList, wordsToFind):
    # κρατά τις 2 τελευταίες λέξεις της τριάδας ώστε να δει
    # αν υπάρχει αυτή τριάδα που να ξεκινά από αυτές τις δύο λέξεις
    possibleFindings = []

    # if boths words are in a triplet note that triplet
    for idx, triplet in enumerate(tripleList):
        if wordsToFind[0] in triplet and wordsToFind[1] in triplet:
            possibleFindings.append(idx)

    findings = []

    # check those triplets for the correct order
    for i in possibleFindings:
        if tripleList[i][0] == wordsToFind[0]\
                and tripleList[i][1] == wordsToFind[1]:
            findings.append(i)

    # Αν υπάρχουν πάνω από μία τριάδες, τότε επιλέγει μία από αυτές στην τύχη.
    return random.choice(findings) if len(findings) > 0 else -1


def createText(tripleList, flag):
    c = 0
    finalText = random.choice(tripleList)
    # φτιάχνει κείμενο 200 περίπου λέξεων.
    while len(finalText) < 201:

        last2words = finalText[-2:]
        foundPosition = validTriplets(tripleList, last2words)

        if foundPosition > 0:
            finalText = finalText + tripleList[foundPosition]
            # finalText.extend(tripleList[foundPosition])
            # the += for lists calls extend which extends the same list without
            # making a new one..that functionality behaves unexpectedly here
            # because it mutates the tripleList itself ;)
        else:
            # the else happens usually when the txt file is less than 100
            # since the exercise doesnt clearly specify what should happen in
            # that case I will just assume  ¯\_(ツ)_/¯
            if len(finalText) > c and flag == 'y':
                print 'The script could not find a next valid triplet..\
 stopped at text length: ', len(finalText)
                c += len(finalText)
            finalText = random.choice(tripleList)

    return ' '.join(finalText)


if __name__ == '__main__':
    try:
        # because argc is not good enough and can only use argv..
        if len(sys.argv) == 2:
            txtFile = str(sys.argv[1])
        elif len(sys.argv) == 1:
            txtFile = raw_input('Enter file path ')
        else:
            print 'Wrong Number of args.. Either 1 or none..'
            quit(0)

        # could do a /usr/bin/file against the user file but since this is a py
        # script anyone (with some knowledge) can read the source..even if its
        # compiled(.pyc) or obfuscated
        if txtFile[-3:] != 'txt':
            print 'Only a txt file!..'
            quit(0)

        debugmsg = raw_input('Enable debug messages? [y/n] ')[0].lower()
        triList = storeInTriplets(scanFile(txtFile))
        # print triList

        resText = createText(triList, debugmsg)
        print '\nText with length ', len(resText.split()), '\n'
        print resText
    except (KeyboardInterrupt, EOFError):
        print '\nQuitting..'
        quit(0)
