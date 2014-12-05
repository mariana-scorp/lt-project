import os

CATS = "ABCDEFGHI"

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
f.write("Category\tNumber of words\n")
for cat in CATS:
    f.write(cat + "       \t" + str(categories[cat]) + "\n")
f.close()
