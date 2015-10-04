# -*- coding: utf-8 -*-

import requests
from lxml import html

def translit(word):
    conversion = {
        u'\u0410' : 'A',    u'\u0430' : 'a',
        u'\u0411' : 'B',    u'\u0431' : 'b',
        u'\u0412' : 'V',    u'\u0432' : 'v',
        u'\u0413' : 'Gh',    u'\u0433' : 'gh',
        u'\u0490' : 'G',    u'\u0491' : 'g',
        u'\u0414' : 'D',    u'\u0434' : 'd',
        u'\u0415' : 'E',    u'\u0435' : 'e',
        u'\u0404' : 'Ye',   u'\u0454' : 'je',
        u'\u0416' : 'Zh',   u'\u0436' : 'zh',
        u'\u0417' : 'Z',    u'\u0437' : 'z',
        u'\u0418' : 'Y',    u'\u0438' : 'y',
        u'\u0406' : 'I',    u'\u0456' : 'i',
        u'\u0407' : 'Ji',   u'\u0457' : 'ji',
        u'\u0419' : 'J',    u'\u0439' : 'j',
        u'\u041a' : 'K',    u'\u043a' : 'k',
        u'\u041b' : 'L',    u'\u043b' : 'l',
        u'\u041c' : 'M',    u'\u043c' : 'm',
        u'\u041d' : 'N',    u'\u043d' : 'n',
        u'\u041e' : 'O',    u'\u043e' : 'o',
        u'\u041f' : 'P',    u'\u043f' : 'p',
        u'\u0420' : 'R',    u'\u0440' : 'r',
        u'\u0421' : 'S',    u'\u0441' : 's',
        u'\u0422' : 'T',    u'\u0442' : 't',
        u'\u0423' : 'U',    u'\u0443' : 'u',
        u'\u0424' : 'F',    u'\u0444' : 'f',
        u'\u0425' : 'Kh',    u'\u0445' : 'kh',
        u'\u0426' : 'C',   u'\u0446' : 'c',
        u'\u0427' : 'Ch',   u'\u0447' : 'ch',
        u'\u0428' : 'Sh',   u'\u0448' : 'sh',
        u'\u0429' : 'Shh',  u'\u0449' : 'shh',
        u'\u044c' : 'j',
        u'\u042e' : 'Ju',   u'\u044e' : 'ju',
        u'\u042f' : 'Ja',   u'\u044f' : 'ja',
        u'\'' : "."
    }
    translit_word = []
    for c in word:
        translit_word.append(conversion.setdefault(c, c))
    return ''.join(translit_word)

with open("adjp.txt", "r") as f:
    adjps = f.readlines()

with open("adjp_w_tags.txt", "w") as f:
    for i in adjps:
        f.write(i)
        if not i.startswith("//"):
            word = translit(i[:-1].decode("utf-8"))
            page = requests.get("http://sum.in.ua/s/" + word[:-1])
            tree = html.fromstring(page.text)
            tags = tree.xpath('//abbr/text()')
            f.write("\t")
            if len(tags) == 0:
                f.write("---")
            else:
                for t in tags:
                   f.write(t.encode("utf-8").replace("\n", " "))
                   f.write(" ")
            f.write("\n")
