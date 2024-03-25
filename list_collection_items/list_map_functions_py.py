'''
link : https://www.pythontutorial.net/python-basics/python-map-list/
---------------------------------------------------------------------
Learn how to use the Python map() function with lists.
When working with a list (or a tuple), you often need to transform the elements of the list and return a new list that contains the transformed element.
'''

bonuses = [100, 200, 300]
new_bonuses = []

for bonus in bonuses:
    new_bonuses.append(bonus * 2)

print(bonuses)
print(new_bonuses)

# Introduction to Map Function
'''
The map() function iterates over all elements in a list (or a tuple), applies a function to each, and returns a new iterator of the new elements.
'''


def double(bonus):
    return 2 * bonus


iterator_with_func = map(double, bonuses)
iterator = map(lambda bonus: bonus * 2, bonuses)
print(list(iterator_with_func))
print(list(iterator))

# Using the map() function for a list of strings
names = ['David', 'Peter', 'Jennifers']
new_names = map(lambda name: name.upper(), names)

print(names)
print(list(new_names))
