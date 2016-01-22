# Define a function histogram() that takes a list of integers and prints a
# histogram to the screen. For example, histogram([4, 9, 7]) should print the
# following:

# ****
# *********
# *******

def histogram(l):
    for i in l:
        print("*" * i)

histogram([4, 9, 7])

# Define a function overlapping() that takes two lists and returns True if they
# have at least one member in common, False otherwise.
#
# overlapping([2, 3, 4], [3, 6, 7]) -> True
# overlapping([2, 3, 4], [5, 6, 7]) -> False

def overlapping(list1, list2):
    for element in list1:
        if element in list2:
            return True

    return False

print(overlapping([2, 3, 4], [3, 6, 7]))
print(overlapping([2, 3, 4], [5, 6, 7]))

# Write a function that returns a dictionary that maps a list of words to
# the lengths of the correponding words.
# map_length(["my", "name", "is", "Boo"]) -> {"my": 2, "name": 4, "is": 2, "Boo": 3}
def map_length(l):
    lengths = {}
    for word in l:
        lengths[word] = len(word)

    return lengths

print(map_length(["my", "name", "is", "Boo"]))

# Write a function that returns dictionary that counts how many words of a
# certain length are there in a list of words.
# word_length_count(["my, "name", "is", "Boo"]) -> {2: 2, 4: 1, 3: 1}

def word_length_count(l):
    length_counts = {}
    for word in l:
        word_len = len(word)
        if word_len in length_counts:
            length_counts[word_len] += 1
        else:
            length_counts[word_len] = 1
    return length_counts

print(word_length_count(["my", "name", "is", "Boo"]))

# Write a function max_in_list() that takes a list of numbers and returns the
# largest one.

def max_in_list(l):
    if len(l) == 0:
        print("Error: list has no elements")
        return None # No answer

    maximum = l[0]
    for elem in l:
        if elem > maximum:
            maximum = elem

    return maximum

print(max_in_list([0, 4, 2, 10, -5]))

# Write a function filter_long_words() that takes a list of words and an integer
# n and returns a new list with all words longer than length n filtered out.

def filter_long_words(words, n):
    filtered_words = []
    for word in words:
        if len(word) > n:
            continue
        filtered_words.append(word)
    return filtered_words

print(filter_long_words(['hello', 'hi', 'functions', 'lists', 'dicts'], 8))
print(filter_long_words(['hello', 'hi', 'functions', 'lists', 'dicts'], 4))
