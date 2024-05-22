# link : https://www.pythontutorial.net/python-basics/python-try-except-finally/


"""
Learn about the Python try...except...finally statementL
Use Python try...catch...finally statement to execute a code block whether an exception occurs or not.
Use the finally clause to clean up the resources such as closing files.
"""

# Introduction to try:...except:...finally:... statement


"""
The try...except statement allows you to catch one or more exceptions in the try clause 
and handle each of them in the except clauses.
The try...except statement also has an optional clause called finally.

The finally clause always executes whether an exception occurs or not. 
And it executes after the try clause and any except clause.
"""

# Using try:...except:...finally:... statement

a = 10
b = 11

try:
    c = a / b
    print(c)
except ZeroDivisionError as error:
    print(error)
finally:
    print("finishing up.")


# Using try:...finally:... statement

"""
Typically, you use this statement when you cannot handle the exception but you want to clean up resources. 
For example, you want to close the file that has been opened.
"""

a = 10
b = 2

try:
    c = a / b
    print(c)
finally:
    print("finishing up.")
