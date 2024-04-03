'''
link : https://www.pythontutorial.net/python-basics/python-set-difference/
--------------------------------------------------------------------------
Learn about the set difference and how to use it to find difference between two or more sets.

- A difference between two sets results in a new set countaining elements in the first set that
  are not present on the second set.
- Use the difference() method or the difference "-" operator to find the difference between sets.
'''

# Introduction to the set difference

'''Using the set difference() method to find the difference between sets'''
s1 = {'python', 'java', 'c++'}
s2 = {'C#', 'java', 'c++'}

s1_difference_s2 = s1.difference(s2)
s2_difference_s1 = s2.difference(s1)

print(f's1 = {s1}')
print(f's2 = {s2}')
print(f's1_difference_s2 = {s1_difference_s2}')
print(f's2_difference_s1 = {s2_difference_s1}')

'''Using the set difference "-" operator to find the difference between sets'''
s1_difference_s2_operator = s1 - s2
s2_difference_s1_operator = s2 - s1
print(f's1_difference_s2_operator = {s1_difference_s2_operator}')
print(f's2_difference_s1_operator = {s2_difference_s1_operator}')

# The set difference() method vs. The set "&" operator
'''
The set difference() method can accept one or more iterables
(string, list, tuple, dictionary).
While the set difference "-" operator only allow sets. 

When you pass iterables to the set difference() method, it'll convert the iterables to sets
before performing the difference operation. 
'''

numbers = {7, 8, 9}
scores = [8, 9]
new_scores = numbers.difference(scores)

# another_scores = numbers - set(scores) TypeError: unsupported operand type(s) for -: 'set' and 'list'
another_scores = numbers - set(scores)

print(f'numbers = {numbers}')
print(f'scores = {scores}')
print(f'new_scores = {new_scores}')
print(f'another_scores = {another_scores}')


