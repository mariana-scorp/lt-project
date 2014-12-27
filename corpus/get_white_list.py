# -*- coding: utf-8 -*-

import os, sort

CATS = "ABCDEFGHI"

books = []
articles = []

def add_books(name, books, articles):
        f = open(name, "r")
        text = f.read()
        author_ind = text.find("<author_surname_1>")
        if author_ind != -1:
            author = text[author_ind + 18:text.find("</author_surname_1>")]
        else:
            author_ind = text.find("<author_surname>")
            author = text[author_ind + 16:text.find("</author_surname>")]
        title = text[text.find("<title>") + 7:text.find("</title>")]
        if author != "":
            string = author.decode("utf-8") + ". " + title.decode("utf-8")
            books.append(sort.Word(string.encode("utf-8")))
        else:
            articles.append(sort.Word(title))        
        f.close()

for name in os.listdir("."):
    if name.endswith(".txt") and name[0] in CATS and name[1] == "_":
        add_books(name, books, articles)
    
for name in os.listdir("Processed_good"):
    if name.endswith(".txt") and name[0] in CATS and name[1] == "_":
        add_books("Processed_good/" + name, books, articles)

sort.quicksort(books, 0, len(books) - 1)
sort.quicksort(articles, 0, len(articles) - 1)

f = open("!_white_list.txt", "w")

f.write("-----------------------------")
f.write("\n")
f.write(u"Опрацьовані книжки".encode("utf-8"))
f.write("\n")
f.write("-----------------------------")
f.write("\n")

f.write(books[0].word)
f.write("\n")
for i in range(1, len(books) - 1):
    if books[i].word != books[i - 1].word:
        f.write(books[i].word)
        f.write("\n")

f.write("-----------------------------")
f.write("\n")
f.write(u"Опрацьовані статті без автора".encode("utf-8"))
f.write("\n")
f.write("-----------------------------")
f.write("\n")

f.write(articles[0].word)
f.write("\n")
for i in range(1, len(articles) - 1):
    if articles[i].word != articles[i - 1].word:
        f.write(articles[i].word)
        f.write("\n")

f.write("-----------------------------")

f.close()
