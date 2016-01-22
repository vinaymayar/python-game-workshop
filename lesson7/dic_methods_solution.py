# Exercise 8
# Write a function contains_key that checks if a certain key is in a dictionary.

def contains_key(key, dic):
    return key in dic

# Exercise 9
# Write a function contains_value that checks is a value is in a dictionary.

def contains_value(value, dic):
    return value in dic.values()

# OR

def contains_value_2(value, dic):
    for key in dic:
        if dic[key] == value:
            return True
            break
    return False

dic = {"a": 1, "b": 2, "c": 3}
print (contains_key("a", dic)) # True
print (contains_key("d", dic)) # False

print (contains_value(1, dic)) # True
print (contains_value("a", dic)) # False

print (contains_value_2(1, dic)) # True
print (contains_value_2("a", dic)) # False



# Exercise 10
# Using the dictionary methods, write a function that increases by 1 all the
# values in a dictionary.

def increase_all_values(dic):
    for key in dic:
        dic[key] += 1

increase_all_values(dic)
print(dic) # should print {"a": 2, "b": 3, "c": 4}

# Exercise 10b
# Write a method that doesn't modify dic but returns a new dictionary with
# all values increased by one

def new_dict_with_increased_values(dic):
    new_dict = {}
    for key in dic:
        new_dict[key] = dic[key] + 1
    return new_dict

print(new_dict_with_increased_values(dic)) # should print {"a": 3, "b": 4, "c": 5}
