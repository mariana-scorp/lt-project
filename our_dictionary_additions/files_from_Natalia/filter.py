# -*- coding: utf-8 -*-
import os

file_list = []

for f in os.listdir("."):
    if (f.endswith(".txt") and not f.endswith("_filtered.txt") and not f.endswith("_new.txt")):
        file_list.append(f)

for i in file_list:
    f = open(i, "r")
    f1 = open(i[:-4] + "_filtered.txt", "w")
    wordlist = []
    for line in f.readlines():
        if (u"\ ".encode("utf-8") not in line):
            apostrophe = line.find("\"")
            if (apostrophe != -1):
                word = line[:apostrophe] + "'" + line[apostrophe+1:]
                wordlist.append(word)
            else:
                wordlist.append(line)

    wordlist = set(wordlist)
    wordlist = sorted(wordlist)
    for i in wordlist:
        f1.write(i)

    f.close()
    f1.close()
