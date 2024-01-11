def list_loop():
    # Lists and Definite Loops
    friends = ['Joeseph', 'Glenn', 'Sally']
    for friend in friends:
        print('Happy New Year: ', friend)
    print('done.')


def inside_lists():
    # looking inside lists
    friends = ['Joeseph', 'Glenn', 'Sally']
    print(friends[1])


def list_mutable():
    # lists are mutable
    fruit = ['Banana']
    fruit[0] = 'b'


def w():
    def longest_word(words):
        longest_so_far = ''
        for word in words:
            length = len(word)
            if length > len(longest_so_far):
                longest_so_far = word
        return longest_so_far

    sentence = input('Enter a sentence: ')
    words = sentence.split(' ')
    output = max(words, key=len)

    print(f"The longest word is '{output}'")


def main():
    func1 = list_loop
    func2 = inside_lists
    func3 = list_mutable
    func4 = w

    # call the functions
    func1()
    func2()
    func3()
    func4()

if __name__ == "__main__":
    main()
