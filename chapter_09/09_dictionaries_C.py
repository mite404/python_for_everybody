# Counting Pattern using a dictionary

"""
counts = dict()
print('Enter a line of text:')
line = input('')

words = line.split()

print('Words:', words)

print('Counting:', words)

print('Counting...')
for word in words:
    counts[word] = counts.get(word, 0) + 1
print('Counts', counts)


# definite loops and dictionaries
counts = {'chuck': 1, 'fred': 42, 'jan': 100}
for key in counts:
    print(key, counts[key])


jjj = {'chuck': 1, 'fred': 42, 'jan': 100}
print(list(jjj))

jjj = {'chuck': 1, 'fred': 42, 'jan': 100}
print(jjj.items())
"""

jjj = {'chuck': 1, 'fred': 42, 'jan': 100}
for aaa, bbb in jjj.items():
    print(aaa, bbb, sep=", ")
