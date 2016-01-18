# 4. Variables in terms of other variables.
# Not all variables need to assigned to constant values. They can also be
# assigned to other variables or expressions.

year_i_was_born = 1995
this_year = 2016
my_age = this_year - year_i_was_born
# We defined my_age in terms of the variables this_year and year_i_was born


# What happens to my_age if I reassign this_year or year_i_was_born?
# Reassign one of the variables and see what happens!
# Why does that happen?

year_i_was_born = 1993
print("The year I was born is {}, but my age is still {}".format(year_i_was_born, my_age))

# This happens because my_age was assigned the result of the expression, 21, not
# the expression itself. So, changing year_i_was_born after my_age has been
# evaluated, does not affect its value.

