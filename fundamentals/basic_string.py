"""
link : https://www.pythontutorial.net/python-basics/python-string/
"""

# Introduction to string
"""
A string is a series of characters. In pyhton, anything inside
quotes is a string. You can use either single or double quotes.
"""

message = "this is a string in python"
print(message)
# [Output] this is a string in python

message = "this is also a string"
print(message)
# [Output] this is also a string

message = "it's a string"
print(message)
# [Output] it's a string

message = '"beautiful is better than ugly.". said Tim Peters'
print(message)
# [Output] "beautiful is better than ugly.". said Tim Peters

"""
If a string contains a single quote, you should place it in double-quotes.
And when a string contains double quotes, you can use the single quotes
"""

message = "It's \" also a valid string"  # using \ as escape an character
print(message)
# [Output] It's " also a valid string

"""
To escape the quotes, you use the backslash.
The Python interpreter will treat the backslash character special.
If you don't want it to do so, you can use raw strings by adding
the letter 'r' before the first quote.
"""

message = r"C:\python\bin"  # 'r' means raw string
print(message)
# [Output] C:\python\bin


# Creating multiline strings
help_message = """
Usage : mysql command
    -h hostname
    -d database name
    -u username
    -p password
"""
print(help_message)
# [Output]
#
# Usage : mysql command
#     -h hostname
#     -d database name
#     -u username
#     -p password

"""
To span a string multiple lines, you use triple-quotes.
"""

# Using variables in strings with the f-strings

name = "john"
greet_text = f"hello {name}"  # f-string, embed variables value inside a string
print(greet_text)
# [Output] hello john

"""
Sometimes, you want to use the values of variables in a string.
For example, you may want to use the value of the 'name' variable
inside the 'greet_text' string variable.

To do it, you place the letter 'f' before
the opening quotation mark and put the brace around the variable 'name'.
Python will replace the {name} by the value of the 'name' variable.
"""

# Concatinating strings

greeting = "Good " "morning!"  # string concatenating
print(greeting)
# [Output] Good morning!

"""
When you place the string literals next to each other,
python automatically concatenates them into one string.
To concatenate two string variables,
you use the operator '+'.
"""

greet_txt = "Good "
time = "Afternoon"
greet_txt = greet_txt + time + "!"
print(greet_txt)
# [Output] Good Afternoon!

# Accessing string elements
"""
Since a string is a sequence of characters,
you can access its elements using an index.
The first character in the string has an index of zero.

The following example shows how to access elements
using an index.
"""
str = "Python String"

print(str[0])
# [Output] P
print(str[1])
# [Output] y


"""
- First, create a variable that holds a string "Python String".
- Then, access the first and second characters of the string
  by using the square brackets [] and indexes.

If you use a negative index, Python returns
the character starting from the end of the string.
"""

print(str[-1])
# [Output] g
print(str[-2])
# [Output] n


"""
The following illustrates the indexes of
the string "Python String"

+---+---+---+---+---+---+---+---+---+---+---+---+---+
| P | y | t | h | o | n |   | S | t | r | i | n | g |
+---+---+---+---+---+---+---+---+---+---+---+---+---+
  0   1   2   3   4   5   6   7   8   9   10  11  12
-13  -12  -11  -10 -9  -8  -7  -6  -5  -4  -3  -2  -1
"""

# Getting the length of a string
"""
To get the length of a string, you use the 'len()' function.
"""
str_len = len(str)
print(str_len)
# [Output] 13

# Slicing strings


print(str[0:2])
# [Output] Py

"""
Slicing allows you to get a substring from a string.
The 'str[0:2]' returns a substring that includes
the character from the index 0 (included) to 2 (excluded).

The syntax for slicing is as follows:
   string[start:end]

The substring always includes the character
at the start and excludes the string at the end.
The start and end are optional.
If you omit the start, it defaults to zero.
If you omit the end, it defaults to the string's length.
"""

# Strings are immutable


str[0] = "C"  # TypeError


new_str = "C" + str[1:]
print(new_str)
# [Output] Cython String

"""
[Note]
Python strings are immutable. It means that you cannot change the string.
For example, you'll get an error if you update
one or more characters in a string.

When want to modify a string, you need to create
a new one from the existing string.
"""


"""
Learn about Python string and its basic operations.

[Summary]

- In python, a string is a series of characters. Also,
  python strings are immutable.
- Use quotes, either single quotes or double quotes to
  string literals.
- Use the backslash character to escape quotes in strings.
- Use raw string r"..." to escape the backslash character.
- Use f-string to insert subtitute variables in literal strings.
- Places literal strings next to each other to concatenate them. And
- Use the '+' operator to concatenate string variables.
- Use the 'len(...)' function to get the size of a string.
- Use the 'str[n]' to access the character at the position 'n' of
  the string 'str'.
- Use slicing to extract a substring from a string.
"""
