# link : https://www.pythontutorial.net/python-basics/python-partial-functions/
from functools import partial

"""
Learn about partial functions and how to define partial functions using
the partial function and using it from the functools module.
"""
import functools

# Introduction to partial functions.
"""
The following example defines a function that multiplies multiplies arguments.
The case are you just want to multiply an argument with specified number, e. g. "2".
To do that we can reuse multiply function like this :
"""

"""
The "double()" function returns the "multiply()" function.
It passed the number 2 to the second argument of the "multiply()" function.
The "double()" function freezes the second argument of the "multiply()" function.
In other words, "double()" function reduces the complexity of the "multiply()" function.
In python the "double()" function called partial function.
"""


def multiply(a, b):
    return a * b


def double(a):
    return multiply(a, 2)


result = double(10)
print(f'result = {result}')


"""
Python provides you with the partial function from the functools standard module 
to help you define partial functions more easily.
The partial function returns new partial object, which is a callable.
When you call the partial object, Python calls the "fn()" function 
with the positional arguments (*args) and keyword arguments (**kwargs).
"""


# Introduction to partial function from functools module.
# functools.partial(fn, /, *args, **kwargs)

double_with_partial_object = partial(multiply, b=3)
result_with_partial_object = double_with_partial_object(10)
print(f'double_with_partial_object = {result_with_partial_object}')


# Partial function with varaibles.


def multiply_val(a_val, b_val):
    return a_val * b_val

x_val = 4
calculate_mul = partial(multiply_val, x_val)
result_val = calculate_mul(10)

print(f'result_val = {result_val} : calculate_mul() with variables as a argument.')
