# link : https://www.pythontutorial.net/python-basics/python-issubset/

# Learn about how to use the issubset() method to check if a set is a subset of another set.
# Set A is a subset of Set B if all elements of the set A are also elements of the set B
# Use Set issubset() method return True if a set is a subset of another set.
# Use the subset operator "<=" or the proper subset operator "<" to check
# if a set is a subset or a proper subset of another set.

# Introduction to issubset() method

numbers = {1, 2, 3, 4, 5}
scores = {1, 2, 3}

# Using the issubset() method
is_scores_sub_set_of_numbers = scores.issubset(numbers)
is_numbers_sub_set_of_scores = numbers.issubset(scores)


# Using the subset operator "<="

is_scores_sub_set_of_numbers_operator = scores <= numbers
is_numbers_sub_set_of_numbers_operator = numbers <= numbers
is_numbers_sub_set_of_scores_operator = numbers <= scores


# Using the proper subset operator "<"
is_scores_proper_sub_set_numbers_operator = scores < numbers
is_numbers_proper_sub_set_numbers_operator = numbers < numbers
is_numbers_proper_sub_set_scores_operator = numbers < scores

print(f'numbers = {numbers}')
print(f'scores = {scores}')
print(f'is scores sub-set of numbers ? {is_scores_sub_set_of_numbers}')
print(f'is numbers sub-set of scores ? {is_numbers_sub_set_of_scores}')
print(f'is scores sub-set of numbers with "<=" operator ? {is_scores_sub_set_of_numbers_operator}')
print(f'is numbers sub-set of numbers with "<=" operator ? {is_numbers_sub_set_of_numbers_operator}')
print(f'is numbers sub-set of scores with "<=" operator ? {is_numbers_sub_set_of_scores_operator}')
print(f'is scores proper sub-set of numbers with "<" operator ? {is_scores_proper_sub_set_numbers_operator}')
print(f'is numbers proper sub-set of numbers with "<" operator ? {is_numbers_proper_sub_set_numbers_operator}')
print(f'is numbers proper sub-set of scores with "<" operator ? {is_numbers_proper_sub_set_scores_operator}')
