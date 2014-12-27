# -*- coding: utf-8 -*-
import os

file_list = []

for f in os.listdir("."):
    if f.endswith("_new_reversed.txt"):
        file_list.append(f)

for name in file_list:
    nocaps = []
    caps = []
    f = open(name, "r")
    for line in f.readlines():
        if line.decode("utf-8").islower():
            nocaps.append(line)
        else:
            caps.append(line)
    f.close()
    if len(caps) > 0:
        f1 = open(name, "w")
        for word in nocaps:
            f1.write(word)
        f1.close()
        f2 = open(name[:-4] + "_caps.txt", "w")
        for word in caps:
            f2.write(word)
        f2.close()
