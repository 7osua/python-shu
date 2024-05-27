# link : https://www.pythontutorial.net/python-basics/python-args/

"""
Learn about the "*args" parameters and how to use them for defining variadic functions.
- Use the *arg arguments for a function that accepts a variable
  number of arguments.
- The *args argument exhausts positional arguments so
  you can only use keyword arguments after it.
"""

# Review tuple unpacking

"""
The following example unpacks a tuple into two variables.
"""
x, y = 10, 20


def add(x_el, y_el):
    return x_el + y_el


result = add(10, 20)
print(f"x = {x}\ny = {y}")
print(f"result = {result}")

"""
Another example,
unpacks a tuples and assigns into two variables
and the remaining elements within tuples into the list.
"""
x_val, y_val, *z_val = 10, 20, 30, 40

"""
When passing optional arguments 10, 20, 30, 40
to the function, assigns 10 to "x_val", 20 to "y_val"
and a tuple (30, 40) to "z_val".

!!! the "z_val" is a tuple, not a list
"""


def add_val(x_el01, y_el01, *z):
    total_calc = x_el01 + y_el01
    print(type(z))
    for z_val_el in z:
        total_calc += z_val_el

    return total_calc


result_val = add_val(10, 20, 30, 40)
print(f"x_val = {x_val}\ny_val = {y_val}\n*z_val = {z_val}")
print(f"result_val = {result_val}")

# Introduction to the "*" args parameter.
'''
When a function has a parameter preceded by an asteriks "*", 
it can accept a variable of number of arguments. 
It can accept zero, one, or more arguments to the "*" args parameter.
'''


def add_with_variadic_parameter(*args):
    print(f'*args = {type(args)}')
    print(args)
    total_sum_el = 0
    for arg in args:
        print(arg)
        total_sum_el += arg
    return total_sum_el


add_with_variadic_parameter()
'''
In python the parameters like "*" args are called variadic parameters.
Function that have variadic parameters are called variadic functions.
'''
total = add_with_variadic_parameter(1, 2, 3)
print(f'total = {total}')

# Introduction to the "*" args argument exhaust positional arguments.
'''
- If we use the "*" args  argument, we cannot add more positional arguments.
- To use argument after the "*" arg argument we can assign with keyword arguments "kwargs" after the "*" args argument.
- The following example is an error because it uses a positional argument after the "*" args argument.
'''


def add_exhaust_positional_arguments(x_arg, y_arg, *args, z_arg):
    return x_arg + y_arg + sum(args) + z_arg


# total = add_exhaust_positional_arguments(1, 2, 3, 4)
# TypeError: missing 1 required keyword-only argument : 'z'
total = add_exhaust_positional_arguments(2, 4, 6, 8, z_arg=10)
print(f'total = {total} with exhaust the positional arguments.')


# Introduction to the unpacking arguments.
a_point = 1, 2
'''
The following print_point() function accepts two arguments and returns a string
as a representation of a point wit x-coordinate and y-coordinate.
'''


def print_point(x_point, y_point):
    return f'x = {x_point}, y = {y_point}'
# a_point_text = print_point(a_point)
# TypeError: print_point() missing 1 required positional argument: 'y_point'


'''
When we preceded the argument a_point with the *, python unpacks the tuple and assigns 
its elements to x_point and y_point parameters.
'''
a_point_text = print_point(*a_point)
print(a_point_text)
