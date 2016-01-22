# Exercise 7
# Write a function char_freq() that takes in a string and counts the number of
# times each letter appeared in the string.
# For example, the string "abca" should return a dictionary in the form
# {"a": 2, "b": 1, "c": 1}.

def char_freq(s):
    frequencies = {}
    for char in s:
        if char in frequencies:
            frequencies[char] += 1
        else:
            frequencies[char] = 1
    return frequencies

print(char_freq("abca"))
print(char_freq("elephant"))
print(char_freq("alphabet"))
print(char_freq("abcabcabcabcabc"))
