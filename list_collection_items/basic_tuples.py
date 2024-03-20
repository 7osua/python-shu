'''
link : https://www.pythontutorial.net/python-basics/python-tuples/
------------------------------------------------------------------
Learn about Python tuples and how to use them effectively.
A tuple is a list that cannot change. Python refers to a value that cannot change as immutable.
So by definition, a tuple is an immutable list.
'''

# Defining a Tuple.
rgb = ("red", "green", "blue")

print(rgb[0])
print(rgb[1])
print(rgb[2])

# Defining a tuple that has one element.
numbers = (3,)
print(type(numbers))

numbers = (3)
print(type(numbers))

# Assigning a tuple
days = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday")
print(days)

days = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")
print(days)
