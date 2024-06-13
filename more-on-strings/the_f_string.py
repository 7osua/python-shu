# Introduction to the Python F-strings

name = "john"
s = f"Hello, {name}"
print(s)

first_name = "John"
last_name = "Doe"
print(f"Hello, {' '.join((first_name, last_name))}!")

"""
1. First, define a variable with the value 'John'.
2. Then, place the 'name' variable inside the curly braces '{}'
   in the literal string.
3. Finally, print out the 's' variable.
"""

# Multiline f-strings

name = "John"
website = "PythonTutorial.net"

message = f"Hello {name}.\n" f"You're learning Python at {website}."
print(message)

message = f"""Hello {name}.
You're learning Python at {website}."""
print(message)


"""
Python 3.6 introduced the f-strings
that allow us to format text strings faster and more elegant.
The f-strings provide a way to embed variables and expressions
inside a string literal using a clearer syntax than
the 'format()' method.

Note! :
- That you need to prefix the string with the letter 'f' to indicate
  that it is an f-string.
  It’s also valid if you use the letter in uppercase (F).
- Python evaluates the expressions in f-string at runtime.
  It replaces the expressions inside an f-string with their values.

"""

# The evaluation order of expressions in Python f-strings


def inc(numbers: list[int], value: int) -> int:
    numbers[0] += value
    return numbers[0]


numbers: list[int] = [0]
result_text = f"{inc(numbers, 1)}, {inc(numbers, 2)}"

print(result_text)

"""
Python evaluates the expressions in an f-string
in the left-to-right order.
This is obvious if the expressions have side effects like the example above.
"""


# Format numbers using f-strings

number = 16
print(f"{number:x}")
"""
The above example use a f-string to format an integer as hexadecimal.
"""

float_number = 0.01
print(f"{float_number:e}")
"""
The following example uses the f-string to format a number as a scientific notation.
"""

pad_number = 200
print(f"{pad_number:06}")
"""
If you want to pad zeros at the beginning of the number, you use the f-string format as above.
"""

result_number = 9.98567
print(f"{result_number: .2f}")
"""
To specify the number of decimal places, you can also use the f-string.
"""

large_number = 400000000000
print(f"{large_number: ,}")
"""
If the number is too large, you can use the number separator to make it easier to read:
"""

percantege_number = 0.1259
print(f"{percantege_number: 0.2%}")
print(f"{percantege_number: 0.1%}")
"""
To format a number as a percentage, you use the following f-string format
"""

"""
Learn about the f-string and how to use them to format strings
and make code more readable.

1. f-string provide an elegant way to format text strings.
2. f-string will replaces the result of an expression embedded inside
   the curly braces {} in an f-string at runtime.
"""

# link : https://www.pythontutorial.net/python-basics/python-f-strings/
