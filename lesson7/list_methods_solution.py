# Exercise 4
# Write a function concatenate that takes in two lists and makes a new list
# containing all elements of the first list followed by all
# elements of the second list.
# concatenate([1, 2, 3], [4, 5, 6]) -> [1, 2, 3, 4, 5, 6]

def concatenate(list1, list2):
    new_list = list1[:] # same as list[0:-1], makes a copy of list
    for element in list2:
        new_list.append(element)
    return new_list

# OR

def concatenate_2(list1, list2):
    return list1 + list2 # This works!

print(concatenate([1, 2, 3], [4, 5, 6]))

print(concatenate_2([1, 2, 3], [4, 5, 6]))

# Exercise 5
# Write a function clear that takes in a list and removes all its elements.

def clear(l):
    while len(l) > 0:
        l.pop(0)

my_list = [1, 2, 3, 4, 5]
clear(my_list)

# my_list should now be empty
print(my_list)
