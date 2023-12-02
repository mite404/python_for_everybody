# Sample Try & Except

rawstr = input('Enter a number: ')
try:
    ival = int(rawstr)
except:
    ival = -1   # ival is just a way to trigger printing 'not a valid number' 

if ival > 0 :   # using less than 0 as a trigger
    print('Good job')
else:
    print('Not a valid number')
    