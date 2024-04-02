'''
link : https://www.pythontutorial.net/python-basics/python-set-union/
---------------------------------------------------------------------
Learn how to union two or more sets by using the union() or set operator.

- The union of two or more sets return distinct values from both sets.
- Use union() or set union operator "|" to union two or mote sets.
- The union() method accepts one or more iterables while the set union operator "|" only accepts sets.
'''


# Introduction to the set union

s1 = {'Python', 'Java'}
s2 = {'C#', 'Java'}

# Union sets using union() method

s_union_intro = s1.union(s2)

print(f's1 = {s1} \ns2 = {s2}')
print(f's_union_intro = {s_union_intro}')

# Union sets using the union operator "|"

s_union_operator = s1 | s2

print(f's_union_operator = {s_union_operator}')

# the union() method vs. the union operator "|"

rates = {1, 2, 3}
ranks = [2, 3, 4]

'''
the union() method accept one or more iterables, converts the iterables to sets, and perform the union
'''
ratings = rates.union(ranks)


'''
the union operator "|" only allows sets, not like the union() method
'''

# ratings_operator = rates | ranks # TypeError: unsupported operand type(s) for |: 'set' and 'list
ratings_operator = rates | set(ranks)


print(f'rates = {rates}')
print(f'ranks = {ranks}')
print(f'ratings = {ratings}')
print(f'ratings_operator = {ratings_operator}')
