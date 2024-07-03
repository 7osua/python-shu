# link : https://www.pythontutorial.net/python-basics/python-type-conversion/


# Introduction to type conversion

value = input("Enter a value:")  # [Input] 100
print(value)
# [Output] 100

"""
- First, get input from users, using the 'input()' function.
- Then, execute the code above to prompt for assign to the 'value' variable.
  After assign the code will display the value that user input.
- However, the 'input()' function will return a string type, not an integer.
"""

net_price = input("Enter the price ($) : ")  # [Input] 100
tax_rate = input("Enter the tax rate (%) : ")  # [Input] 10
# tax_amount = tax_rate * net_price / 100  # [Error] TypeError

# Using the 'int()' function to convert the input strings to numbers
tax_amount = int(tax_rate) * int(net_price) / 100
print(f"The tax amount is: ${tax_amount}")
# [Output] The tax amount is: $10.0

"""
The following example prompts you to enter two input values:
'net_price' and 'rax_rate'. After that, it calculates the
'tax_amount' and displays the result on the screen.

When you execute the program and enter some numbers. You will get an error.
This happen because the 'input()' function return value with strings data type.
So we cannot apply the '*' multiply or the '/' devide operator to calculates
the 'tax_amount'.

To solve this issue, you need to convert the strings to numbers
before performing calculations.

To convert a string to a number, you use the 'int()' function. More precisely,
the 'int()' function converts a string to an integer.
"""

# Other type conversion functions

print(bool(tax_amount))
# [Output] True

print(str(tax_amount))
# [Output] 10.0

"""
Besides the int(str) functions, Python supports other type conversion functions.
The following shows the most important ones for now:

- float(str) -> convert a string to a floating-point number.
- bool(val) -> convert a value to a boolean value, either True or False.
- str(val) -> return the string representation of a value.
"""

# Getting the type of a value

type(100)
# [Output] <class 'int'>

type(2.0)
# [Output] <class 'float'>

type("Hello")
# [Output] <class 'str'>

type(True)
# [Output] <class 'bool'>

"""
To get the type of value, you use the 'type(...)' function.

As you can see clearly from the output:

The number 100 has the type of 'int'.
The number 2.0 has the type of 'float'.
The string 'Hello' has the type of 'str'.
And the True value has the type of 'bool'.

In front of each type, you see the 'class' keyword.
It isn't important for now. And you'll learn more
about the 'class' later.
"""

"""
Learn about type conversion in Python and some useful type conversion functions.

[Summary]
- Use the 'input()' function to get an input string from users.
- Use type conversion function such as 'int()', 'float()', 'str()', and 'bool()'
  to convert a value from one type to another.
  Use the 'type()' function to get the type of a value.
"""
