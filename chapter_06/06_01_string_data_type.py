# String Data Type - reading and converting


str1 = "Hello"
str2 = 'there'
bob = str1 + ' ' + str2
print(bob)

str3 = '123'
# str3 = str3 + 1   this string (str3) needs to be converted to an
# integer (int) first before being concatenated with another int

x = int(str3) + 1
print(x)


# Looking Inside Strings
fruit = 'banana'
letter = fruit[5]       # square brackets = an 'index operator'
print(letter)           # we're indexing the character at position 1 in 'banana' which is the 2nd character in the string


# look inside 'fruit' string and return total num characters
fruit = 'banana!!'
print(len(fruit))




# using a while loop to return every letter in 'fruit' via an index
# ex 1:
fruit = 'banana'
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(index, letter)
    index = index + 1

# using a for loop to return every letter in 'fruit'
# ex 2:
fruit = 'banana'
for letter in fruit:
    print(letter)

# using a for loop to return every letter in 'fruit' <-- the most elegant solution
# ex 3:
for letter in 'banana':
    print(letter)

for n in 'banana':
    print(n)



# counting the number of times we encounter the letter 'a'
word = 'banana'
count = 0
for letter in word:
    if letter == 'a':
        count = count + 1
print(count)


"""
# return first and last characters in 'fruit'
fruit = 'banana'
letter = fruit[5]

x = 2
w = fruit[x - 2]
last = fruit[5]
print('First character: ', w)
print('Last character: ', last)
"""
