# -*- coding: utf-8 -*-
import os

file_list = []

for f in os.listdir("."):
    if (f.endswith(".txt") and not f.endswith("_filtered.txt") and not "_new" in f):
        file_list.append(f)

for i in file_list:
    name = i
    f = open(i, "r")
    wordlist = []
    multi = []
    for line in f.readlines():
        if (u"\ ".encode("utf-8") not in line):
            apostrophe = line.find("\"")
            if (apostrophe != -1):
                word = line[:apostrophe] + "'" + line[apostrophe+1:]
                wordlist.append(word)
            else:
                wordlist.append(line)
        else:
            multi.append(line)

    if (len(wordlist) > 0):
        wordlist = set(wordlist)
        wordlist = sorted(wordlist)
        f1 = open(name[:-4] + "_filtered.txt", "w")
        for j in wordlist:
            f1.write(j)
        f1.close()
    if (len(multi) > 0):
        multi = set(multi)
        multi = sorted(multi)
        f2 = open(name[:-4] + "_multi.txt", "w")
        for j in multi:
            f2.write(j)
        f2.close()
    f.close()
    
