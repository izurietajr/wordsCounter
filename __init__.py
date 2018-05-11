# -*- coding: utf-8 -*-

import os, sys
import operator


def openFile():
    name = "texto.txt"
    return open(name, "r", encoding="utf-8")


def getStringsList(file):
    text = file.read()
    file.close()
    text = text.replace("\n", " ")
    elements = text.split(" ")
    words = [w.lower() for w in elements]
    coincidences = {}
    for w in words:
        if w in coincidences:
            n = coincidences[w]
            coincidences[w] = n + 1
        else:
            coincidences[w] = 1
    return coincidences


file = openFile()
dic = getStringsList(file)
sorted_dic = sorted(dic.items(), key=operator.itemgetter(1))
for (word, count) in sorted_dic:
    print(word, count, "\n")