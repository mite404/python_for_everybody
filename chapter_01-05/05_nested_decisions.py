# Nested decisions

x = 100
if x > 1:
    print('More than 1')
    if x < 100:
        print('Less than 100')
if x < 100:
    print('Fuck you')
if x == 100:
    print('All right, all right, all right')
print('Finito')
