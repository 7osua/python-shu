# link : https://www.pythontutorial.net/python-basics/python-kwargs/


"""
Learn about the **kwargs parameters.

The **kwargs is called a keyword parameter.
When a function has the **kwargs parameter, it can accept a variable number of keyword arguments as dictionary.

- Use the **kwargs parameter to allow the function to accept a variable number of keywords arguments.
- Inside the function, the **kwargs argument is a dictionary that contains all
  keyword arguments as its name-value pairs.
- Preceded double stars (**) to a dictionary argument to pass it to **kwargs parameter.
- Always place the **kwargs parameter at the end of the parameter list, or you will get an error.
"""


# Introduction to the "**kwargs" parameters.

def connect(**kwargs):
    print(type(kwargs))
    print(kwargs)


connect()
connect(sever='localhost', port=3306, user='root', password='pyth0n!')


# Using **kwargs parameter with other parameters.

# def connect_fn(**kwargs, fn): #SyntaxError: invalid syntax
#     print(kwargs)


'''
The fn function can accept a variable number of the positional arguments. 
Python will pack them as a tuple and assign the tuple to the args argument.
The fn function also accepts a variable number of keyword arguments. 
Python will pack them as a dictionary and assign the dictionary to the kwargs argument.
'''


def connect_fn(fn, **kwargs):  # SyntaxError: invalid syntax
    print(f'kwargs parameters with other parameters : {type(kwargs)}')
    print(kwargs, fn)

def fn(*args, **kwargs):
    print(f'args = {args} : type = {type(args)}')
    print(f'kwargs = {kwargs} : type = {type(kwargs)}')

connect_fn(1)
fn(1,2, x_val=3, y_val=4)
