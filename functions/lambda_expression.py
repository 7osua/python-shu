'''
link : https://www.pythontutorial.net/python-basics/python-lambda-expressions/
------------------------------------------------------------------------------
Use lambda expressions to create anonymous functions, which are functions without names.
A lambda expression accepts one or more arguments, contains an expression, and returns the result of that expression.
Use lambda expressions to pass anonymous functions to a function and return a function from another function.
'''


# Functions that accept a function
def get_full_name(first_name, last_name, formatter_func):
    return formatter_func(first_name, last_name)


def first_last(first_name, last_name):
    return f"{first_name} {last_name}".upper()


def last_first(first_name, last_name):
    return f"{last_name}, {first_name}".upper()


full_name = get_full_name("josua", "manullang", first_last)
print(f"full_name = {full_name}")

full_name = get_full_name("josua", "manullang", last_first)
print(f"full_name = {full_name}")

full_name = get_full_name("john", "doe", lambda first_name, last_name: f"{first_name} {last_name}".upper())
print(f"full_name with lambda expression = {full_name}")

full_name = get_full_name("john", "doe", lambda first_name, last_name: f"{last_name}, {first_name}".upper())
print(f"full_name with lambda expression = {full_name}")

# Functions that return a function
def times(n):
    return lambda x : x * n

double = times(2)
triple = times(3)

result = double(2)
print(f"result x double = {result}")

result = double(3)
print(f"result x double= {result}")

result_triple = triple(4)
print(f"result x triple = {result_triple}")

result_triple = triple(5)
print(f"result x triple= {result_triple}")


# Lambda function in a loop
