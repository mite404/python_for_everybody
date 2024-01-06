# Welcome to Dictionaries - bags that have no order
# so we index things we put in a dictionary with a "lookup tag"

purse = dict()
purse['money'] = 12
purse['candy'] = 3
purse['tissues'] = 75
# print(purse)

# print(purse['candy'])

purse['candy'] = purse['candy'] + 2
print(purse)


# dictionaries are like lists except that they use keys instead of numbers to
# look up values

lst = list()
lst.append(21)
lst.append(183)
# print(lst)
lst[0] = 23
print(lst)

ddd = dict()
ddd['age'] = 21
ddd['course'] = 182
print(ddd)


# Dictionary Literals (Constants)
jjj = {'chuck':1, 'fred':42, 'jan':100}
print(jjj)

ooo = {}
print(ooo)
