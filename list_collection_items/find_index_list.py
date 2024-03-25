'''
link : https://www.pythontutorial.net/python-basics/python-find-index-of-element-in-list/
-----------------------------------------------------------------------------------------
Learn how to find the index of an element in a list.
Use the in operator with the index() function to find if an element is in a list.
'''

cities = ['New York', 'Beijing', 'Cairo', 'Mumbai', 'Mexico']
result = cities.index('Mumbai')
city = 'Osaka'

print(f'Mumbai at index = {result}')

if city in cities:
    result = cities.index('Osaka')
    print(f'The {city} has an index of {result}.')
else :
    print(f'The {city} doesn\'t exist on the list.')
