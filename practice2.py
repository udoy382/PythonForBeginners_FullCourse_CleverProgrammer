# Practice Dictionaries


'''
word_frequency('I love Batman because I am Batman')
{'I': 2, 'love':1, 'Batman':2, 'am': 1}
'''

def word_frequency(phrase):
    result = {}
    words = phrase.split()
    for word in words:
        if word not in result:
            result[word] = 1
        else:
            result[word] += 1
    return result


# print(word_frequency('I love Batman because I am Batman'))
print(word_frequency(input("Please Enter your Phrase: ")))
