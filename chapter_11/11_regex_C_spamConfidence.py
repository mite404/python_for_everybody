# RegEx C - Spam Confidence Program Example
# opening a file, searching for a string

import re

filename = '/Users/ea/Programming/Python/pyprojects/python_for_everybody/chapter_11/mbox-short.txt'

numlist = list()

with open(filename) as hand:
    for line in hand:
        line = line.rstrip()
        stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line)
        if len(stuff) != 1: continue
        num = float(stuff[0])
        numlist.append(num)

if numlist:
    print('Maximum:', max(numlist))
else:
    print('No matches found.')
