# link : https://www.pythontutorial.net/python-basics/python-raw-strings/


# Introduction to raw strings

s = "lang\tver\nPython\t3"
print(s)

"""
In python, when we prefix a string with letter 'r' or 'R' such as
r'...' and R'...', that string becomes a raw string. Unlike a reguler
string, raw string treats the backslashes '\' as literal characters

Use raw strings when we deal with strings that have many backslashes.
1. Using with reguler expression
2. directory path on windows

This happen because python use '\' to represent special characters
such as tabs and newlines. Python uses the backslash '\' to signify
the start of an escape sequence.

A raw string is like its regular string with the backslash (\)
represented as double backslashes (\\)
"""

s1 = r"lang\tver\nPython\t3"
s2 = "lang\\tver\\nPython\\t3"
print(s1)
print(s2)

"""
In a reguler string, python counts an escape sequence as a single
character.
How ever, in a raw string, python counst the backslash '\' as
one character.
"""

s3 = "\n"
s4 = r"\n"
print(len(s3))
print(len(s4))

"""
since the backslash '\' escapes the single quote ' or double quotes ",
a raw string cannot end with an odd number of backslashes.
"""
# s5 = r"\"  	# SyntaxError
# s6 = r"\\\" 	# SyntaxError


# Use raw strings to handle file path on windows

"""
On windows OS, backslashes used to seperate paths.
Python treats '\u' in the path as a Unicode
escape but could not decode it.
"""

# dir_path = "C:\user\tasks\new" # SyntaxError
# print(dir_path)

"""
To make it easy, you can turn the 'dir_path' into a raw string.
"""

dir_path = r"C:\user\tasks\new"
print(dir_path)


# Convert a reguler string into a raw string

s7 = '\n'
raw_string = repr(s7)
raw_string_without_quote = repr(s7)[1:-1]
print(s7)
print(raw_string) # out : '\n'
print(raw_string_without_quote)

"""
To conver a reguler string into a raw string, we can use
the built-in 'repr()' function.

Note :
the 'raw_string' has the quote at the beginning and end of the strings.
To remove the ' quote, we can use slices [1:-1].
"""

"""
Learn about raw strings and how to use it to handle strings that threat
backslash as literal character.

summary :
- Prefix a literals string with the letter 'r' and 'R' to
  turn a reguler strig into a raw string.
- Raw strings treat backslash as a literal character.
"""
