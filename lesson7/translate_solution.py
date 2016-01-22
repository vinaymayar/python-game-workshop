# Exercise 6:
# Use a dictionary to make a function to translate words in English to
# Portuguese. The function takes in a list of words in English.
# To do this, you will add new entries to the translation dictionary.

def translate(list_of_words):
    translated = []

    translation = {
        "my": "meu",
        "name": "nome",
        "is" : "e",
        "Lara": "Lara",
        "I": "eu",
        "am": "sou",
        "the": "o/a",
        "best": "melhor"
    }

    for word in list_of_words:
        if word in translation:
            translated.append(translation[word])
        else:
            translated.append("?")

    return translated

print(translate(['my', 'name', 'is', 'Lara']))
print(translate(['I', 'am', 'the', 'best']))
