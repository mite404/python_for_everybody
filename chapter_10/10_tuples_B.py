# Tuples B
'''
c = {
    'a': 10,
    'b': 1,
    'c': 22,
}
tmp = list()
for k, v in c.items():
    tmp.append((v, k))

# print(tmp)


tmp = sorted(tmp, reverse=True)
print(tmp)
'''

fhand = open('romeo.txt')
counts = dict()
for line in fhand:
    words = line.split()
    for word in words:
        counts[word1] = counts.get(word, 0) + 1

lst = list()
for key, val in counts.items():
    newtup = (val, key)
    lst.append(newtup)

lst = sorted(lst, reverse=True)

for val, key in lst[:10]:
    print(key, val)

#solving the for loop for list using 'List Comprehension'
print( sorted([ (v, k) for k, v in c.items() ]) )
