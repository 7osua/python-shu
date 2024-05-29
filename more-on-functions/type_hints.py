# link : https://www.pythontutorial.net/python-basics/python-type-hints/
from typing import Union
from typing import List

"""
Learn about type hints and how to use mypy tool to check types statically.
- Use type hints and static type checker tools to make your code more robust.
"""

# Introduction to The type hints.

"""
Python uses dynamic typing, in which a function’s variables, parameters, and return values 
can be any type. 
Also, the types of variables can change while the program runs.
Generally, dynamic typing makes it easy to program and 
causes unexpected errors that you can only discover until the program runs.
"""


def say_hi(name):
    return f'Hi {name}'


def say_hi_type_hint(name: str) -> str:
    """The following example defines a simple function that accepts a string and returns another string"""
    return f'Hi {name}'


"""
Besides the str type, you can use other built-in types such as int, float, bool, and bytes for type hintings.
"""
greeting_text = say_hi('john')
greeting_text_with_hint = say_hi_type_hint("test")
print(greeting_text)
print(greeting_text_with_hint)

# Using a static type checker tool: mypy
"""
Since Mypy is a third-party package, you need to install it using the following pip command.

    pip install mypy
    
    mypy  app.py more-on-functions/type_hints.py
"""

# Using Type Hinting & Type Inference

name: str = 'John'
name = 'Jane'


# Adding type hints for multiple types

def add(x, y):
    return x + y


def add_with_union_type(x: Union[int, float], y: Union[int, float]) -> Union[int, float]:
    """The numbers can be integers or floats. You can use the module to set type hints for multiple types."""
    return x + y


def add_with_union_syntax(x: int | float, y: int | float) -> int | float:
    return x + y


result_add = add(40, 30)
result_add_union = add_with_union_syntax(60, 10)
result_add_union_syntax = add_with_union_syntax(65, 5)
result_add_union_syntax_float = add_with_union_syntax(64.5, 5.5)

print(f'result_add = {result_add}')
print(f'result_add_union = {result_add_union}')
print(f'result_add_union_syntax = {result_add_union_syntax}')
print(f'result_add_union_syntax_float = {result_add_union_syntax}')

# Introduction to The Type Aliases

number = Union[int, float]


def add_with_union_type_aliases(x: number, y: number) -> number:
    """
    we assign the Union[int, float] type an alias Number and use the Number alias in the add() function.
    """
    return x + y


# Adding type hint for lists, sets, and dictionaries

ratings: list = [1, 3, 5]
ratings_list_of_integers: List[int] = [2, 4, 5]
# ratings = { 'x' : 1, 'y' : 4}
# error: Incompatible types in assignment (expression has type "Dict[int, str]",
# variable has type "List[Any]") Found 1 error in 1 file (checked 1 source file).

print(f'ratings = {ratings} | type : {type(ratings)}')
print(f'ratings_ratings_list_of_integers = {ratings_list_of_integers} | type = {type(ratings_list_of_integers)} ')


# None Type

def log(message: str) -> None:
    """
    If a function does not explicitly return a value, you can use None to type hint the return value.
    """
    print(f'message : {message}')

log("Succes: no issue found in 1 source file")
