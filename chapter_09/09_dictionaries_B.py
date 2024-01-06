# Using Dictonaries to count
ccc = dict()
ccc['csev'] = 1
ccc['cwen'] = 1
# print(ccc)
ccc['cwen'] = ccc['cwen'] + 1
print(ccc)

# Dictionary Tracebacks
ccc = dict()
print(ccc['csev'])
'csev' in ccc

counts = dict()
names = ['csev', 'cwen', 'csev', 'ziqan', 'cwen']
for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] = counts[name] + 1
print(counts)

# simplified counting with get() Method
counts = dict()
names = ['csev', 'cwen', 'csev', 'ziqan', 'cwen']
for name in names:
    counts[name] = counts.get(name, 0) + 1
print(counts)
