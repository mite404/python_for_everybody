# Multi-way Decisions

## with else
x = 20

if x < 2 :
    print('small')
elif x < 10 :
    print('medium')
else :
    print('LARGE')
    
print('fin.')

## no else
x = 50

if x < 2 :
    print('small')
elif x < 10 :
    print('medium')   

# if x is larger than 10, skip to the end. only fin will print  
print('fin.')


## 3rd example:
x = 101
if x < 2 :
    print('small')
elif x < 10  :
    print('medium')
elif x < 20  :
    print('big')
elif x < 40  :
    print('large')
elif x < 100 :
        print('huge')
else :
    print('gigantic')


## 2 multi-way puzzle examples
###     which line of code will never execute?

# puzzle 1
if x < 2 :
    print('below 2')
elif x >= 2 :
    print('2 or more')
else :
    print('something else')
    
# puzzle 2
if x < 2 :
    print('below 2')
elif x < 20 :
    print('below 20')
elif x < 10 :           #this line of code will never run if x < 10 b/c the previous elif will always be true first
    print('below 10')
else :
    print('something else')