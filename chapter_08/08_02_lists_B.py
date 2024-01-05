# concatenating lists using "+" operator
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)


# list slicing
t = [9, 41, 12, 3, 74, 15]
t[1:3]
t[:4]
t[3:]
t[:]


# building a list from scratch
stuff = list()
stuff.append('book')
stuff.append(99)
stuff.append('cookie')
print(stuff)


# is something in a list?
some = [1, 9, 21, 10, 16]
9 in some

15 in some

20 not in some

# lists are in order
friends = ['Joseph', 'Glenn', 'Sally']
friends.sort()
print(friends)
print(friends[1])

# built-in functions and lists
nums = [3, 41, 12, 9, 74, 15]
print(len(nums))

print(max(nums))

print(min(nums))

print(sum(nums))

print(sum(nums)/len(nums))

# making a loop without a list
total = 0
count = 0
while True:
    inp = input('Enter a number: ')
    if inp == 'done' : break
    value = float(inp)
    total = total + value
    count = count + 1
average = total / count
print('Average:', average)

# making a loop with a list
numlist = list()
while True:
    inp = input('Enter a number: ')
    if inp == 'done' : break
    value = float(inp)
    numlist.append(value)

average = sum(numlist) / len(numlist)
print('Average:', average)
