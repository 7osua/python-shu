# link : https://www.pythontutorial.net/python-basics/python-unpacking-tuple/

"""
Learn how to un-tuples.
"""
from operator import and_

# Review Tuples "()"

"""
- Python using commas" val1,val2" to define tuples, not parentheses().
- Python using parentheses "(val1, val2)", so to make the tuple more clearer.
- Python using empty parentheses (), to define an empty tuple.
- Python using the "tuple()" constructor to create a tuples.
- Unpacking tuples means assigning individual elements of a tuple to multiple variables.
- Use the * operator to assign remaining elements
  of an unpacking assignment into a list and assign it to a variable.
"""

a_tuple = 1, 2
a_tuple_wihtout_parentheses = (1,)
a_tuple_parentheses = (3, 4)
an_empty_tuple = ()
a_tuple_constructor = tuple([1, 2])
print(f"type : {type(a_tuple)} {a_tuple}")
print(f"type : {type(a_tuple_wihtout_parentheses)} {a_tuple_wihtout_parentheses}")
print(f"type : {type(a_tuple_parentheses)} {a_tuple_parentheses}")
print(f"type : {type(an_empty_tuple)} {an_empty_tuple}")
print(f"type : {type(a_tuple_constructor)} {a_tuple_constructor}")


# Introduction to unpacking a tuple


"""
Unpacking a tuple means splitting the tuples elements into individual variables.
Take a look below example.
The left side is a tuple of two variables x_val and y_val.
The right side is also a tuple of two integers 1 and 2.
"""

x_val, y_val = (1, 2)
print(f"x_val = {x_val} y = {y_val}")


"""
The expression assign the tuple elements on the right side (1,2) to each variable on the left side
(x_val,y_val) based on the relative position of each element.
x_val will take 1.
y_val will take 2.
"""

x_val, y_val, z_val = 1, 2, 3
numbers = x_val, y_val, z_val

print(
    f"x_val = {x_val} {type(x_val)} | y_val = {y_val} {type(y_val)} | z_val = {z_val} {type(z_val)}"
)
print(f"numbers = {numbers} {type(numbers)}")


# Using unpacking tuple to swap values of two variables

x_val = 9
y_val = 10
print(f"x_val = {x_val} | y_val = {y_val}")

temp_val = x_val
x_val = y_val
y_val = temp_val
print(f"x_val = {x_val} | y_val = {y_val}")

"""
with unpacking tuple syntax We can achieve the same result
"""
x_val = 9
y_val = 10
print(f"x_val = {x_val} | y_val = {y_val}")

x_val = 9
y_val = 10
x_val, y_val = y_val, x_val
print(f"x_val = {x_val} | y_val = {y_val}")


# x_val, y_val = 1, 2, 3  # ValueError : to many values to unpack.
x_val, y_val, _ = 1, 2, 3

print(f" x_val, y_val, _ = {x_val}, {y_val}, {_}")


# Extended the unpacking using "*" operator

red, green, *other = (192, 210, 100, 0.5)

"""
Sometimes you don't want to unpack every single item in tuple.
For example, you may want to unpack only the first and the second elements.
In this case, you can achieve this by using "*" operator.
The remaing elements will tranform into a list which assigned to "*other".
"""
print(f"red = {red} | green = {green} | other = {other} type : {type(other)}")


# red, green, *other, *another = (192, 210, 100, 0.5) # SyntaxError: multiple starred expressions in assignment


# Using the "*" operator in the right hand side

odd_numbers = (1, 3, 5)
even_numbers = (2, 4, 6)

numbers = (*odd_numbers, *even_numbers)

print(
    f"odd_numbers = {odd_numbers}\neven_numbers = {even_numbers}\nnumbers = {numbers}"
)
