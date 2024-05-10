# link : https://www.pythontutorial.net/python-basics/python-disjoint-sets/
# Learn about disjoint sets and how to use the Python isdisjoint() method to check if two sets are disjoint.
# - Two sets are disjoint if they have no element in common.
# - Use set isdisjoint() method to check if two sets are disjoint.


# Introduction to isdisjoint() method


odd_numbers = {1, 3, 5}
even_numbers = {2, 4, 6}

letters = {'A', 'B', 'C'}
alpha_numerics = {'A', 1, 2}

# Use isdisjoint() method


is_odd_numbers_even_numbers_is_disjoint = odd_numbers.isdisjoint(even_numbers)
is_letters_alphanumerics_is_disjoint = letters.isdisjoint(alpha_numerics)

print(f'is odd_numbers = {odd_numbers} and even_numbers = {even_numbers} disjoint ? {is_odd_numbers_even_numbers_is_disjoint}')
print(f'is letters = {letters} and alpha_numerics = {alpha_numerics} disjoint ? {is_letters_alphanumerics_is_disjoint}')
