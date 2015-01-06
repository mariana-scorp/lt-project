#!/usr/bin/python3

import sys
import locale


def rev_sort_key(str):
  return locale.strxfrm( ''.join(reversed(str)) )


if __name__ == '__main__':
  if len(sys.argv) < 2:
    print("Usage:", sys.argv[0], "<input_file>")
    sys.exit(1)

  locale.setlocale(locale.LC_ALL, 'uk_UA.UTF-8')

  with open(sys.argv[1]) as in_file:
    lines = in_file.readlines()

  lines = sorted(lines, key=rev_sort_key);

  out = open("output.txt", "w")

  for i in lines:
    out.write(i)

  out.close()

  print("Done.")
