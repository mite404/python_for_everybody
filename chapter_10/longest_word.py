# a good example of multiple concepts and syntaxes in Python

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
