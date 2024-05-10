# https://www.pythontutorial.net/python-basics/python-issuperset/
# Learn how to use the Python issuperset() method to check if a set is a superset of another.
# - The set A is a superset of a set B if all elements of set B are elements of set A.
# - Use the Python issuperset() method to check if a set is a superset of another.
# - Use the superset operator (>=) or proper superset operator (>)
#   to check if a set is a superset or a proper superset of another set.


# Introduction to issuperset() method
numbers = {1, 2,  3, 4, 5}
scores = {1, 2, 3}


# Using the issubset() method
is_numbers_superset_of_scores = numbers.issuperset(scores)
is_numbers_superset_of_numbers = numbers.issuperset(numbers)
is_scores_superset_of_numbers = scores.issuperset(numbers)


print(f'is numbers = {numbers} superset of scores = {scores} ? {is_numbers_superset_of_scores}')
print(f'is numbers = {numbers} of numbers = {numbers} superset ? {is_numbers_superset_of_numbers}')
print(f'is scores = {scores} of numbers = {numbers} superset ? {is_scores_superset_of_numbers}')

# Using the superset operators '>='
is_numbers_superset_of_scores_operator = numbers >= scores
is_numbers_superset_of_numbers_operator = numbers >= numbers
is_scores_superset_of_numbers_operator = scores >= numbers

print(f'is numbers = {numbers} superset >= scores = {scores} ? {is_numbers_superset_of_scores_operator}')
print(f'is numbers = {numbers} superset >= numbers = {numbers} ? {is_numbers_superset_of_numbers_operator}')
print(f'is scores = {scores} superset >=  number {numbers} ? {is_scores_superset_of_numbers_operator}')


# Using the proper superset operator '>'
is_numbers_superset_of_scores_operator_proper = numbers > scores
is_numbers_superset_of_numbers_operator_proper = numbers > numbers
is_scores_superset_of_numbers_operator_proper = scores > numbers

print(f'is numbers = {numbers} superset > scores = {scores} ? {is_numbers_superset_of_scores_operator_proper}')
print(f'is numbers = {numbers} superset > numbers = {numbers} ? {is_numbers_superset_of_numbers_operator_proper}')
print(f'is scores = {scores} superset >  number {numbers} ? {is_scores_superset_of_numbers_operator_proper}')
