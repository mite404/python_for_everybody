"""
# best friends: Strings and Lists
abc = 'With three words'
stuff = abc.split()
print(stuff)

abc = 'With three words'
stuff = abc.split()
print(len(stuff))

abc = 'With three words'
stuff = abc.split()
print(stuff[0])

# looping through all the words
abc = 'With three words'
stuff = abc.split()
for w in stuff :
        print(w)


# using a delimiter to parse data from a list
line = 'A lot                   of spaces'
etc = line.split()
print(etc)

line = 'first;second;third'
thing = line.split()
print(thing)

line = 'first;second;third'
thing = line.split()
print(len(thing))

line = 'first;second;third'
thing = line.split(';')
print(thing)
"""

"""
fhand = open('/Users/ea/Programming/Python/pyprojects/python_for_everybody/chapter_08/mbox-short.txt')
for line in fhand:
        line = line.rstrip()
        if not line.startswith('From ') : continue
        words = line.split()
        print(words[2])
"""


# the DOUBLE SPLIT Pattern
fhand = open('/Users/ea/Programming/Python/pyprojects/python_for_everybody/chapter_08/mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From ') : continue
    words = line.split()
    email = words[1]
    pieces = email.split('@')
    print(pieces[1])
