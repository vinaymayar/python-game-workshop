# Exercise 3:
# Write a function that returns True if the first list contains all elements of
# the second list, and False otherwise

def contains(list1, list2):
    for element in list2:
        if element not in list1:
            return False
    return True


print(contains([0, 1, 2, 3, 4, 5], [0, 5])) # should return True
print(contains([0, 1, 2, 3, 4, 5], [5, 0])) # should return True
print(contains([0, 1, 2, 3, 4, 5], [1, 5])) # should return True
print(contains([0, 1, 2, 3, 4, 5], [0, 4, 6, 9])) # should return False

