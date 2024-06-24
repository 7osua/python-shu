# link: https://www.pythontutorial.net/python-basics/python-variables/


# What is a variable ?
"""
When you develop a program, we need to manage values,
a lot of them!

To store values, you use variables.
In python, a variable is a label that you can assign a value to it.
A a variable is always associated with a value.
"""

message = "Hello, word!"
print(message)
# [Output] Hello, word!


message += " Good bye!"
print(message)
# [Output] Hello, word! Good bye!

"""
In this example, 'message' is a variable.
It holds the string 'Hello, World!'.
The 'print()' function shows the message 'Hello, World!' to the screen.

The next line assigns and add the string 'Good Bye!' to the 'message' variable
and print its value to the screen.

The variable 'message' can hold various values at different times.
And its value can change throughout the program.
"""

# Creating variables

"""
To define a variable, you can use the following syntax

  variable_name = value

- The '=' is the assignment operator. In this syntax,
  you assign a value to the 'variable_name'
- The value can be anything like a number, string, boolean, etc...
  that we can assign to the variable.
"""

# Define a variable named 'counter' and assigns the number 1 to it
counter = 1
print(counter)


# Naming variables
"""
When you name a variable, you need to adhere to some rules.
Or you'll get an error.

The follong are the variable rules that you shild keep in mind:
1. Variable name can contain only letter, number, and underscore (_).
   They can start with a letter or an underscore(_), not with number.
2. Variable name cannot contain spaces. To separate words in variables,
   you can use undescores for example 'sorted_ranks'.
3. Variable names cannot be the same as keywords, reserved words, and
   built-in functions in python.


The following guidelines help you define good variable names:

1. Variable names should be concise and descriptive. For example,
   the 'active_user' variable is more descriptive than the 'au'.
2. Use underscore (_) to seperate multiple words in the variable names.
3. Avoid using the letter 'l' and the uppercase 'O' because
   they look like the number 1 and 0.
"""

"""
Learn about variables and how to use the variables effectively.
"""
