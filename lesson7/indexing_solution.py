# Exercise 1:
# Write a function that returns True if the first and last elements of two lists
# are the same, and return False otherwise.

def is_first_and_last_equal(list1, list2):
    return len(list1) > 0 and len(list2) > 0 and \
            list1[0] == list2[0] and list1[-1] == list2[-1]


print(is_first_and_last_equal([0, 1, 2, 3, 4, 5], [0, 5])) # should return True
print(is_first_and_last_equal([0, 1, 2, 3, 4, 5], [5, 0])) # should return False
print(is_first_and_last_equal([0, 1, 2, 3, 4, 5], [1, 5])) # should return False
print(is_first_and_last_equal([0, 1, 2, 3, 4, 5], [0, 4, 6, 9])) # should return False

# Exercise 2:
# Write a function that given the list [0, 1, 2, 3, 4, 5]
# prints
# [0, 1, 2, 3, 4, 5]
# [1, 2, 3, 4, 5]
# [3, 4, 5]
# [4, 5]
# [5]
# This function should work with any list that you pass to it.
# Remember: You can get the length of a list by doing len(list)

def print_sublists(l):
    sublist = l
    while len(sublist) > 0:
        print(sublist)
        sublist = sublist[1:]

print_sublists([0, 1, 2, 3, 4, 5])
