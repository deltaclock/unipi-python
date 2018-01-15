#!/usr/bin/python
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

    for idx, triplet in enumarate(tripleList):
        if wordsToFind[0] in triplet and wordsToFind[1] in triplet:
            possibleFindings.append(idx)

    findings = []

    for i in possibleFindings:
        if tripleList[i][0] == wordsToFind[0]
        and tripleList[i][1] == wordsToFind[1]:
            findings.append(i)

    return random.choice(findings)


def createText(tripleList):
    finalText = random.choice(tripleList)
    while len(finalText) < 206:
        last2words = finalText[-2:]
        finalText.append(tripleList[foundTriplets(tripleList, last2words)])


if __name__ == '__main__':
    scanFile(raw_input('Enter file path '))
