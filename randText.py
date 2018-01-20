#!/usr/bin/env python
# -*- coding: utf-8 -*-
# first we will assume the input file is a txt because of course python cant
# read "words" of binary data files like pdf and doc..(at least with open/read)
import random


def scanFile(filePath):
    words = []
    with open(filePath, 'r') as fl:
        for line in fl:
            for word in line.strip().split():
                if len(word) < 45 and word.islower():
                    words.append(word)
    return words


def storeInTriplets(wordList):
    while len(wordList) % 3 != 0:
        wordList.pop()
    return [[wordList[i], wordList[i + 1], wordList[i + 2]]
            for i in xrange(0, len(wordList), 3)]


def foundTriplets(tripleList, wordsToFind):
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
    finalText = random.choice(tripleList)
    while len(finalText) < 206:
        last2words = finalText[-2:]
        foundPosition = foundTriplets(tripleList, last2words)
        if foundPosition:
            finalText.append(tripleList[foundPosition])
        else:
            print 'stuff to do when not found!!'
            break
    return ' '.join(finalText)


if __name__ == '__main__':
    txtFile = raw_input('Enter file path ')
    # could do a /usr/bin/file against the user file but since this is a py
    # script anyone (with some knowledge) can read the source..even if its
    # compiled(.pyc) or obfuscated
    if txtFile[-3:] != 'txt':
        print 'Only a txt file!..'
        quit(0)
        try:
            triList = storeInTriplets(scanFile(txtFile))
            print triList
            print createText(triList)
        except (KeyboardInterrupt, EOFError):
            print '\nQuitting..'
            quit(0)
