## a simple example for the DEF function

def thing() :
    print('Hello')
    print('Fun')


thing()
print('Zip')
thing()

## a more complex ex


def greet(lang) :
        if lang == 'es' :
            return 'Hola'
        elif lang == 'fr' :
            return 'Bonjour'
        else:
            return 'Hello'

print(greet('es'), 'Tom')
print(greet('es'), 'Dick')
print(greet('fr'), 'Harry')
