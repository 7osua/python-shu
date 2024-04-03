'''
link : https://www.pythontutorial.net/python-basics/python-set-intersection/
----------------------------------------------------------------------------
Learn about the Set Intersection and how to use it to intersect two or more sets.

- The intersection of two or more sets returns elements that exists in all sets.
- Use the set intersection() method or intersection set operator "&" to intersect two or more sets.
'''

# Introduction to set intersection.
s1 = {'Python', 'Java', 'C++'}
s2 = {'C#', 'Java', 'C++'}
s_intersection_method = s1.intersection(s2)
s_intersection_operator = s1 & s2

print(f's1 = {s1}')
print(f's2 = {s2}')
print(f's_intersection_method = {s_intersection_method}')
print(f's_intersection_operator = {s_intersection_operator}')

# Intersection operator "&" Vs. Intersection() method

'''
The intersecton operator "&" only allow sets.
While, The intersection() method can accept any iteratbles,
like string, list, tuple, and dictionary.
'''

numbers = {1, 2, 3}
scores = [2, 3, 4] # type list

numbers_itersect_method = numbers.intersection(scores)
# numbers_itersect_operator = numbers & scores # TypeError: unsupported operand type(s) for &: 'set' and 'list'

print(f'numbers = {numbers}')
print(f'scores = {scores}')
print(f'number_intersect_method = {numbers_itersect_method}')
print(f'number_intersect_operator = {numbers_itersect_operator}')
