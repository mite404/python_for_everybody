# Try & Except

## the except block only triggers when something in the try block won't execute
## when a line of code within the try block won't execute -- that's the last line of code that'll
## run for that block

# ex 1
astr = 'Hello Bob'
try:
    istr = int(astr)    # this conversion fails so the program skips to the except
except:
    istr = -1
    
print('First', istr)

astr = 123
try:
    istr = int(astr)    # this conversion succeeds so it skips the except
except:
    istr = -1
    
print('Second', istr)

# ex 2
astr = 'Bob'
try:
    print('Hello')
    istr = int(astr)    # this line of code is invalid
    print('there')      ## this line never runs b/c 
except:                 ## the program has skipped ahead to except
    istr = -1
    
print('Done', istr)     ## and print