dictionary = [
    {"alma": "apple"},
    {"fa": "tree"}
]

# Implement this method. It should add the given key-value pair to the
# list 'dictionary'


def add_word(hun_word, eng_word,dict):
    dict.append( {hun_word : eng_word } )

# Implement these methods. They should return the translation of the given
# word form the list 'dictionary'


def translate_to_eng(hun_word, diction):
    for items in diction:
        if hun_word in items:
            print(items)
    



#def translate_to_eng(hun_word):
    pass


add_word("paradicsom", "tomato" , dictionary)
#print(dictionary)

translate_to_eng("alma" , dictionary)


