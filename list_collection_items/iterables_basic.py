'''
link : https://www.pythontutorial.net/python-basics/python-iterables/
----------------------------------------------------------------------
Learn about the Python iterables and iterators.
In Python, an iterable is an object that includes zero, one, or many elements.
An iterable has the ability to return its elements one at a time.
Because of this feature, you can use a for loop to iterate over an iterable.

- An iterable is an object that can be iterated over. An iterable has the ability to return one of its elements at a time.
- An iterator is an agent that performs iteration. It’s stateful. And an iterator is also an iterable object.
- Use the iter() function to get an iterator from an iterable object and the next() function to get the next element from the iterable object.
'''

# Introduction to iterables

for index in range(3):
    '''the range() function is an iterable because you can iterate over its result:'''
    print(index)

str = 'rgb'
for ch in str:
    print(ch)

ranks = ('high', 'medium', 'low')
for rank in ranks:
    print(rank)

'''The rule of thumb is that if you know if can loop over something, it’s iterable.'''

# Introduction to iterator

'''
An iterable can be iterated over. And an iterator is the agent that performs the iteration.
To get an iterator from an iterable, you use the iter() function.
Once you have the iterator, you can get the next element from the iterable using the next() function.
'''

colors = ['red', 'green', 'blue']
colors_iter = iter(colors)

color = next(colors_iter)
print(color)
color = next(colors_iter)
print(color)
color = next(colors_iter)
print(color)


iterator = iter(colors)
for color in iterator:
    print(color)
