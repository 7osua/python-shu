'''
link : https://www.pythontutorial.net/python-basics/python-functions/
----------------------------------------------------------------------
Learn to develop Python functions by using the def keyword.
'''

# Defining a Function
def greet():
    """Display a greeting to users."""
    print('Hi')

greet()

# Passing infromation to "function f()" with parameters.
def greet_user(name):
    print(f'Hello {name}')

greet_user(name = "josua")

# Returnng a value
def greet_user_text(name):
    return f'Ola {name}!'
greetingText = greet_user_text(name = "Manullang")

print(greetingText)


# Function with multiple parameters.
def sum(a, b):
    return int(a) + int(b)

print(sum(1,4))
