# link : https://www.pythontutorial.net/python-basics/python-syntax/
import keyword


# Whitespace and identation


# Define main function to print 'counter = 0' up to 'counter = 9'
def main():
    counter = 0
    max = 10
    while counter < max:
        print(f"counter = {counter}")
        counter += 1


main()  # call the main function.
"""
Python uses whitespace and indentation to construct the code structure.

By using indentation and whitespace to organize the code,
Python code gains the following advantages:
- First, you'll never miss the beginning or ending code of a block
  like in other programming languages such as Java or C#.
- Second, the coding style is essentially uniform.
  If you have to maintain another developer's code,
  that code looks the same as yours.
- Third, the code is more readable and clear
  in comparison with other programming languages.
"""


# type: ignore # Comments
# - The comments are as important as the code because they
#   describe why a piece of code was written.

# - When the Python interpreter executes the code,
#   it ignores the comments.

# - In Python, a single-line comment begins
#   with a hash (#) symbol followed by the comment.

# Continuation of statements

"""
- Python use a new line character to seperate statements.
  It places each statement on one line.
- However, a long statement can span multiple lines by using
  the (\) backslash character. # type: ignore
- The following example illustrates how to use the (\) backslash # type: ignore
  character to continue a statement in the second line.

[Code]
if (a == True) and (b == True) \
   (c == True):
    print("The continuation of statements.")

"""
if (
    (True == True)
    and (True == True)
    and (True == True)
    and (True == True)
    and (True == True)
    and (True == True)
    and (True == True)
):
    print("Continuation of statements")

# Identifiers
"""
- Identifiers are names that identify variables,
  functions, modules, classes, and other objects in Python.
- The name of an identifier needs to begin with a letter or underscore (_).
  The following characters can be alphanumeric or underscore.
- Python identifiers are case-sensitive.
  For example, the 'counter' identifier and 'Counter' identifier
  are different identifiers.
- In addition, you cannot use Python keywords for naming identifiers.
"""

counter = 2
Counter = 1
print(f"counter = {counter}\nCounter = {Counter}")

"""
[Output]
counter = 2
Counter = 1
"""


# Keywords

"""
[Notes]
- Some words have special meanings in python.
  They are called keywords.
- Python is growing language and evolving language.
  So it's keywords will keep increasing and changing.
- Python provide special module for listing its keywords
  called 'keyword' module.
- To find the current keyword list,
  we can use like this following code :

[Shell]
import keyword
print(keyword.kwlist)
"""

print(keyword.kwlist)
# yield += 1 # SyntaxError


# String literals

triple_str = """This is another string"""
double_triple_str = """There are two line of strings.
This is the first line of a strings.
This is the second line of a strings.
"""

# Python use :
# - single quotes '...'
# - double-quotes "..."
# - triple single quotes '''...''' to denote string literal
# - triple double quotes """...""" to denote string literal

print(triple_str)
print(double_triple_str)

"""
The string literal need to be surrounded with
the same type of quotes.
If we use a single quote to start a string literal,
we need to use the same single quote to end it.
"""


"""
Learn about the basic python sysntax,
to get started with the python language quickly.

Summary :
- A python statement ends with newline character.
- Python uses spaces and identation to organize its code structure.
- Identifiers are names that identify
  variables, functions, module, classes, etc ... in python.
- Comments discribe why the code works.
  Comments are ignored by the interpreter.
- Use the single quote, double-quotes, triple-quotes or
  triple double-quotes to denote.
"""
