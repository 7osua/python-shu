'''
link : https://www.pythontutorial.net/python-basics/python-function-docstrings/
-----------------------------------------------------------------------------------
Learn about how to use docstrings to add documentation to a function.
Learn to how use the help() function to get the documentation of a function.
Learn how to place a string, either single-line or multi-line strings, as the first line in the function to add documentation to it.
'''

help(print)

# Using docstrings to document functions
def sum(a,b):
    "Return the sum of two arguments"
    return a + b

help(sum)

# Using multi-line docstring to document a funtions.
def add(a,b):
    '''
    Add two arguments

    Arguments :
    a : an integer
    b : an integer

    Return :
    The sum of two arguments
    '''
    return a + b

help(add)