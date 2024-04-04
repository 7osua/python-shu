# link : https://www.pythontutorial.net/python-basics/python-symmetric-difference/
# --------------------------------------------------------------------------------
# Learn how to find the symmetric difference between two or more sets.
# - The symmetric difference between two or more sets is a set of elements that are in all sets,
#   but not in their intersections.
# - Use the symmetric_difference() method or the symmetric difference "^" operator
#   to find the symmetric difference of two or more sets.

# Introduction to the symmetric difference of sets

'''
The symmetric difference between two sets is a set of elements that are in either set, 
but not in their intersection.
'''

s1 = {'Python', 'Java', 'C++'}
s2 = {'C#', 'Java', 'C++'}

# Using the symmetric_difference() method to find the symmetric difference of sets

s_symmetric_diff_method = s1.symmetric_difference(s2)  # return a new set of elements, doesn't modify the original sets.

print(f's1 = {s1}')
print(f's2 = {s2}')
print(f's_symmetric_difference = {s_symmetric_diff_method}')

# Using the symmetric difference operator "^" to find the difference of sets

s_symmetric_diff_opr = s1 ^ s2

print(f's_symmetric_diff_opr = {s_symmetric_diff_opr}')

# The symmetric_difference() method vs. The symmetric difference operator "^"

# The symmetric_difference() method accepts one or more iterables,
# that can be string, list, tuples or dictionary.

scores = {7, 8, 9}
ranks = [8, 9, 10]

new_set_difference_method = scores.symmetric_difference(ranks)

# The symmetric difference operator \"^\" only applies to sets.
# you\'ll get an error if used with iterables that are not sets.

new_set_difference_operator = scores ^ set(ranks)
# new_set_difference_operator = scores ^ ranks  #  TypeError: unsupported operand type(s) for ^: 'set' and 'list'

print(f'new_set_difference_method = {new_set_difference_method}')
print(f'new_set_difference_operator = {new_set_difference_operator}')
