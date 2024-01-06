# Lists and Definite Loops
friends = ['Joeseph', 'Glenn', 'Sally']
for friend in friends:
    print('Happy New Year: ', friend)
print('done.')


# looking inside lists
friends = ['Joeseph', 'Glenn', 'Sally']
print(friends[1])

# lists are mutable
fruit = 'Banana'
fruit[0] = 'b'


fruit = 'Banana'
x = fruit.lower()
print(x)


lotto = [2, 14, 26, 41, 63]
lotto[2] = 28
lotto.append(55)
print(lotto)


# how long is a list?
# len returns the number of elements in a list or the number of characters in a string.
greet = 'Hello Bob'
print(len(greet))

x = [1, 2, 'joe', 99]
print(len(x))


# using the 'range' function to loop
# the range function returns a list of numbers that range from 0 to one less than the parameter.

print(range(4))

friends = ['Joeseph', 'Glenn', 'Sally']
print(len(friends))

friends = ['Joeseph', 'Glenn', 'Sally']
print(range(len(friends)))


# a tale of two loops
friends = ['Joeseph', 'Glenn', 'Sally']
"""
for friend in friends:
    print('Happy New Year: ', friend)
"""

for i in range(len(friends)):
    friend = friends[i]
    print('Happy New Year:', friend)
