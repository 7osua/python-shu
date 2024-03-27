'''
link : https://www.pythontutorial.net/python-basics/python-reduce-list/
-----------------------------------------------------------------------
Learn how to use the Python reduce() function to reduce a list into a single value.
'''

# Introduction to reduce() funtion to reducing a list into a single value

from functools import reduce

scores = [75, 65, 80, 95, 50]
total = 0

for score in scores:
    total += score

print(scores)
print(total)

'''
The reduce() function applies the fn function of two arguments 
cumulatively to the items of the list, from left to right, 
to reduce the list into a single value.

Unlike the map() and filter() functions, 
the reduce() isn’t a built-in function in Python. 
In fact, the reduce() function belongs to the functools module.
To use the reduce() function, you need to import it from the functools module 
the top of the file.
'''


def sum(a, b):
    print(f'a = {a}, b = {b}, {a} + {b} = {a + b}')
    return a + b


total_scores = reduce(sum, scores)
print(total_scores)

# Using reduce() function on a list with lambda expression
total_scores_lambda = reduce(lambda a, b: a + b, scores)
print(total_scores_lambda)
