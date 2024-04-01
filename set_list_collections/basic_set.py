'''
link : https://www.pythontutorial.net/python-basics/python-set/
---------------------------------------------------------------
Learn about Python Set type and how to use it effectively.
A set is an unordered list of immutable elements. It means:

Elements in a set are unordered.
Elements in a set are unique. A set doesn’t allow duplicate elements.
Elements in a set cannot be changed. For example, they can be numbers, strings, and tuples, but cannot be lists or dictionaries.
'''

# Introduction to set type

'''To define a set in Python, you use the curly brace {}'''
'''You can pass an iterable to the set() function to create a set.'''

skills = {'Python Programming', 'PostgreSQL', 'JavaScript', 'TypeScript'}
another_skills = set(['Problem Solving', 'Critical Thingking'])

empty_set = {}  # To define an empty set, you cannot use the curly braces like this:
empty_set = set()

print(skills)
print(type(skills))
print(another_skills)
print(type(another_skills))

if not empty_set:
    print(f'is empyt_set value are empty = {not empty_set}.')

has_skills = True if not skills else False

print(f'are has_skills value are empty ? {has_skills}.')

chars = set('letters')

''' 
the original order of elements may not be preserved.
the string 'letter' has two e and t characters and the set() removes each of them.
'''

print(chars)

# Getting size of a set
ratings = {1, 2, 3, 4, 5}
print(f'the size of ratings = {len(ratings)} with values of {ratings}')

# Checking if an element is in a set
ratings = {1, 2, 3, 4, 5}
rating = 7

is_element_there = True if (rating in ratings) else False

if rating in ratings:
    print(f'The set contain {ratings} for elements with value of {rating}')
elif rating not in ratings:
    print(f'The set doesn\'t contain {ratings} for elements with value of {rating}')
print(is_element_there)

# Adding an element to a set.
another_skills.add('Python')
print(another_skills)

# Removing an element to a set.
skills.add('Software Developer')
print(skills)
skills.remove('TypeScript')
print(skills)

if 'JavaScript' in skills:
    skills.remove('JavaScript')
else:
    print('The set doesn\'t countain "Java"')

'''
the set has the discard() method that allows you to remove an element. 
And it doesn’t raise an error if the element is not in the list
'''
skills.discard("Java")
print(skills)

# Returning an element from a set

'''
To remove and return an element from a set, you use the pop() method.
Since the elements in a set have no specific order, the pop() method removes an unspecified element from a set.
'''

yet_another_skills = {'Problem Solving', 'Python Programming', 'Software Design'}
a_skill = yet_another_skills.pop()

print(yet_another_skills)
print(a_skill)

'''
To remove all elements from a set, you use clear() method.
'''

yet_another_skills.clear()
print('Not Empty' if yet_another_skills else 'Empty')

# Frozen a set

'''
To make a set immutable, you use the built-in function called frozenset(). 
The frozenset() returns a new immutable set from an existing one.
'''

skills = frozenset(skills)
# skills.add('Django')
'''
AttributeError: 'frozenset' object has no attribute 'add'
'''

# Looping Thorught set elements

print("Looping Thorught set elements")
for skill in skills:
    print(skill)

'''
To access the index of the current element inside the loop, 
you can use the built-in enumerate() function
'''

for index, skill in enumerate(skills, 1):
    print(f'{index} : {skill}')


'''
NOTE : Notice that every time you run the code, you’ll get the set elements in a different order.
'''