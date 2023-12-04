"""
# File 'Handle' as a Sequence
fhand = open('/Users/ea/Programming/Python/pyprojects/python_for_everybody/chapter_07/readme.txt')

# here's a tip for working dir vs relative path
#
# from pathlib import Path
# path = Path(__file__).parent.joinpath("readme.txt")


xfile = open('/Users/ea/Programming/Python/pyprojects/python_for_everybody/chapter_07/readme.txt')
for cheese in xfile:
    print(cheese)


# counting lines in a file
fhand = open('/Users/ea/Programming/Python/pyprojects/python_for_everybody/chapter_07/readme.txt')
count = 0
for line in fhand:
    count = count + 1
print('Line Count:', count)


# Reading the *WHOLE* File
fhand = open('/Users/ea/Programming/Python/pyprojects/python_for_everybody/chapter_07/readme.txt')
inp = fhand.read()          # inp is just a variable name for 'input'
print(len(inp))

print(inp[:20])             # printing the first 20 characters


# Searching through a file
fhand = open('/Users/ea/Programming/Python/pyprojects/python_for_everybody/chapter_07/readme.txt')
for line in fhand:
    line = line.rstrip()    # stripping white space (in this case new lines)
    if line.startswith('etc'):
        print(line)


# Skipping with 'continue'
fhand = open('/Users/ea/Programming/Python/pyprojects/python_for_everybody/chapter_07/readme.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('asdf'):
        continue
    print(line)

# Prompt for file name
fname = input('Enter file name: ')
fhand = open(fname)
count = 0
for line in fhand:
    if line.startswith('asdf'):
        count = count + 1
print('There were ', count, 'lines in, ', fname)
"""


# Dealing with bad file names frm user
fname = input('Enter file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened: ', fname)
    quit()

count = 0
for line in fhand:
    if line.startswith('asdf'):
        count = count + 1
print('There were ', count, 'lines in, ', fname)
