# Regular Expressions: Practical Applications
import re

data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
atpos = data.find('@')
print(atpos)

sppos = data.find(' ', atpos)
print(sppos)

host = data[atpos+1 : sppos]
print(host)


# The Double Split Pattern

line = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'

words = line.split()
email = words[1]                # stephen.marquard@uct.ac.za
pieces = email.split('@')       # ['stephen.marquard', 'uct.ac.za']
print(pieces[1])                # uct.ac.za


# The RegEx Version
import re

lin = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
y = re.findall('@([^ ]*)', lin)
print(y)
