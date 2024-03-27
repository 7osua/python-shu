'''
link : https://www.pythontutorial.net/python-basics/python-dictionary/
----------------------------------------------------------------------
Learn about Python Dictionary which allows you to organize related information.
- A Python dictionary is a collection of key-value pairs, where each key has an associated value.
- Use square brackets or get() method to access a value by its key.
- Use the del statement to remove a key-value pair by the key from the dictionary.
- Use for loop to iterate over keys, values, and key-value pairs in a dictionary.
'''

# Intro to dictionary type

'''
A Python dictionary is a collection of key-value pairs where each key is associated with a value.
A value in the key-value pair can be a number, a string, a list, a tuple, or even another dictionary. 
A key in the key-value pair must be immutable. In other words, the key cannot be changed.
Python uses curly braces {} to define a dictionary. 
Inside the curly braces, you can place zero, one, or many key-value pairs.
'''

empty_dictionaries = {}
print(type(empty_dictionaries))

person = {
    'firts_name': 'John',
    'last_name': 'Doe',
    'age': 25,
    'favorite_colors': ['blue', 'green'],
    'active': True
}

print(person)

# Accessing values in a Dictionary
'''
To access a value by key from a dictionary, 
you can use the square bracket notation or the get() method.
'''

print(person['firts_name'])
print(person['last_name'])

'''
If you attempt to access a key that doesn’t exist, you’ll get an error.
To avoid this error, you can use the get() method of the dictionary.
If the key doesn’t exist, the get() method returns None instead of throwing a KeyError. 
Note that None means no value exists.

The get() method also returns a default value 
when the key doesn’t exist by passing the default value to its second argument.
'''

# ssn = person['ssn'] # KeyError : 'ssn'
ssn = person.get('ssn', '000-00-0000')
print(ssn)

# Adding new key-value pairs
person['gender'] = 'Male'

# Modifyin value in a key-value pair
person['age'] = 26

# Removing key-value pairs
del person['active']

print(person)

# Looping through a dictionary

'''
Looping all key-value pairs in a dictionary

dictionary provides a method called items() that returns an object 
which contains a list of key-value pairs as tuples in a list.
'''

print(person.items())

'''
iterate over all key-value pairs in a dictionary, 
you use a for loop with two variable key and value to unpack each tuple of the list.
'''

print('Looping through a dictionary')
for key, val in person.items():
    print(f'{key} : {val}')

# Looping through all the keys in a dictionary

print('Looping through all the keys in a dictionary')
for key in person.keys():
    print(key)

# Looping through all the values in a dictionary

print('Looping through all the values in a dictionary')
for val in person.values():
    print(val)
