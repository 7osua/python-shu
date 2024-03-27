'''
link : https://www.pythontutorial.net/python-basics/python-list-comprehensions/
-------------------------------------------------------------------------------
Learn about Python List comprehensions that allow you to create a new list from an existing one.
- List comprehensions allow you to create a new list from an existing one.
- Use list comprehensions instead of map() or filter() to make your code more concise and readable.
'''

# Introduction to List Comprehensions

'''
In programming, you often need to transform elements of a list and return a new list.
Example :
get a list of squares based on this numbers list.
'''

numbers = [1, 2, 3, 4, 5]
squares = []

for number in numbers:
    squares.append(number**2)

print(f'numbers = {numbers}')
print(f'squares = {squares}')

# Using lambda expression and map() function
squares_lambda = []

squares_lambda = list(map(lambda number:number**2, numbers))
print(f'squares_lambda = {squares_lambda}')

# here’s the list comprehension
squares_comprehension = [number**2 for number in numbers]
print(f'squares_comprehension = {squares_comprehension}')

'''
A list comprehension consists of the following parts:

- An input list (numbers)
- A variable that represents the elements of the list (number)
- An output expression (number**2) that returns the elements of the output list from the elements of the input list.

[output_expression for element in list]
'''

# Using list comprehension with if expression

'''
The following show a list of the top five higest montains on Eart 
get a list of mountains where the height is greater than 8600 meters, 
you can use a for loop or the filter() function with a lambda expression like this:
'''

mountains = [['Makalu', 8485], ['Lhotse', 8516], ['Kanchendzonga', 8568], ['K2', 8611], ['Everest', 8848]]
higest_mountains = []
higest_mountains_lambda = []
higest_mountains_comprehension = []

for mountain in mountains:
    if(mountain[1] > 8600):
        higest_mountains.append(mountain)


higest_mountains_lambda = list(filter(lambda mountain: mountain[1] > 8600, mountains))
higest_mountains_comprehension = [mountain for mountain in mountains if mountain[1] > 8600]

print(mountains)
print(higest_mountains)
print(higest_mountains_lambda)
print(higest_mountains_comprehension)
