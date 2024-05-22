# link : https://www.pythontutorial.net/python-basics/python-try-except/


"""
Learn how to use the Python try...except statement to handle exceptions gracefully.
In Python, there’re two main kinds of errors: syntax errors and exceptions.

- Use Python try...except statement to handle exceptions gracefully.
- Use specific exceptions in the except block as much as possible.
- Use the except Exception statement to catch other exceptions.
"""

# Understanding syntax error


"""
When you write an invalid Python code, you’ll get a syntax error.
the Python interpreter detected the error at the if statement since a colon (:) is missing after it.
"""

current = 1

if current < 1:  # SyntaxError: expected ':'
    current += 1

print(f'current = {current}')

# Understanding "Exceptions"

"""
Even though when your code has valid syntax, it may cause an error during execution.

In Python, errors that occur during the execution are called exceptions. The causes of exceptions mainly come from the environment where the code executes. For example:

Reading a file that doesn’t exist.
Connecting to a remote server that is offline.
Bad user inputs.

When an exception occurs, the program doesn’t handle it automatically. This results in an error message.
"""

# Handling exceptions


"""
Errors that occur during the execution are called exceptions.
Exceptions have different types such as TypeError, NameError, etc... 
"""

try:
    print('Enter the net sales for')
    previous = float(input('- Previous : '))
    current = float(input('- Current : '))

    change = (current - previous) * 100 / previous

    if change > 0:
        results = f'Sales Increase {abs(change)}%'
    else:
        results = f'Sales Decrease {abs(change)}%'

    print(results)
except  ValueError:
    print('Error! Please enter a number for net sales.')
except ZeroDivisionError:
    print('Error! The prior net sales cannot be zero.')
except Exception as error:
    print(error)
