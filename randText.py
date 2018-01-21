#!/usr/bin/env python
# -*- coding: utf-8 -*-
# first we will assume the input file is a txt because of course python cant
# read "words" of binary data files like pdf and doc..(at least with open/read)
import random
import string


def scanFile(filePath):
    words = []
    with open(filePath, 'r') as fl:
        for line in fl:
            for word in line.strip().split():
                if len(word) < 45 and word.islower():
                    # removing punctuation and hoping
                    words.append(word.translate(None, string.punctuation))
    return words


def storeInTriplets(wordList):
    while len(wordList) % 3 != 0:
        wordList.pop()
    return [[wordList[i], wordList[i + 1], wordList[i + 2]]
            for i in xrange(0, len(wordList), 3)]


def validTriplets(tripleList, wordsToFind):
    possibleFindings = []

    for idx, triplet in enumerate(tripleList):
        if wordsToFind[0] in triplet and wordsToFind[1] in triplet:
            possibleFindings.append(idx)
    # print 'printing possible findings ',
    # print possibleFindings
    findings = []

    for i in possibleFindings:
        if tripleList[i][0] == wordsToFind[0]\
                and tripleList[i][1] == wordsToFind[1]:
            findings.append(i)
    # print 'printing findings ',
    # print findings
    return random.choice(findings) if len(findings) > 0 else False


def createText(tripleList):
    c = 0
    finalText = random.choice(tripleList)
    print 'The script will try again and again..Until success..'
    while len(finalText) < 201:
        # print finalText
        last2words = finalText[-2:]
        foundPosition = validTriplets(tripleList, last2words)
        if foundPosition:
            finalText += tripleList[foundPosition]
        else:
            # since the exercise doesnt clearly specify what should happen in
            # that case I will just assume  ¯\_(ツ)_/¯
            if len(finalText) > c:
                print 'NEW record!!! Length: ', len(finalText)
                c += len(finalText)
            finalText = random.choice(tripleList)

    return ' '.join(finalText)


if __name__ == '__main__':
    try:
        txtFile = raw_input('Enter file path ')
        # could do a /usr/bin/file against the user file but since this is a py
        # script anyone (with some knowledge) can read the source..even if its
        # compiled(.pyc) or obfuscated
        if txtFile[-3:] != 'txt':
            print 'Only a txt file!..'
            quit(0)
        triList = storeInTriplets(scanFile(txtFile))
        # print triList
        resText = createText(triList)
        print 'Words count: ', len(resText.split()), '\n'
        print resText
    except (KeyboardInterrupt, EOFError):
        print '\nQuitting..'
        quit(0)
