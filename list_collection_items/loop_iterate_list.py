'''
link : https://www.pythontutorial.net/python-basics/python-for-loop-list/
-------------------------------------------------------------------------
Learn how to use the Python for loop to iterate over a list in Python.
- Use a for loop to iterate over a list.
- Use a for loop with the enumerate() function to access indexes.
'''

# Inroduction to loop over a list
cities = ['New York', 'Beijing', 'Cairo', 'Mumbai', 'Mexico']

for city in cities:
    print(city)


# Using for loop to iterate over a list with index
# You may want to access indexes of elements inside the loop. In these cases, you can use the enumerate() function.
# The enumerate() function returns a tuple that contains the current index and element of the list.

for index, city in enumerate(cities, 1):
    print(f'{index} : {city}')
