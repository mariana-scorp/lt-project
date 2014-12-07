import os

CATS = "ABCDEFGHI"
FRACTIONS = {"A": 25, "B": 3, "C": 7, "D": 7, "E": 3, "F": 5, "G": 10, "H": 15, "I": 25}

categories = dict()
for cat in CATS:
    categories[cat] = 0

for name in os.listdir("."):
    if name.endswith(".txt") and name != "statistics.txt":
        f = open(name, "r")
        text = f.read()
        cat = text[text.find("<id>") + 4]
        if cat in CATS:
            length_id = text.find("<length>")
            length = text[length_id + 8:text.find("</length>")]
            categories[cat] += int(length)
        else:
            print "Invalid category in " + name + ": " + cat
        f.close()

f = open("statistics.txt", "w")
f.write("Category\tFraction\t# of collected words\t# of words to collect\n")
for cat in CATS:
    s = "%-8s\t%-8s\t%-20s\t%s\n" % (cat, str(FRACTIONS[cat]) + "%",
                                     str(categories[cat]),
                                     str(int(10000 * FRACTIONS[cat]
                                          - categories[cat])))
    f.write(s)
f.close()
