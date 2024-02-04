# Greedy Matching with RegEx

import re

'''
x = 'My 2 favorite number are 19 and 42'

y = re.findall('[0-9]+', x)
print(y)


y = re.findall('[aeiou]+', x)
print(y)


x = 'From: Using the : character'
y = re.findall('^F.+:', x)
print(y)


x = 'From: Using the : character'
y = re.findall('^F.+?:', x)
print(y)
'''


"""
text = "abbbbbbc"
pattern = re.compile(r"ab+?c")

match = pattern.match(text)

if match:
    print("Match found:", match.group())
else:
    print("No match found")
"""

x = 'stephen.marquard@uct.ac.za'
y = re.findall('\\S+@\\S+', x)
print(y)
