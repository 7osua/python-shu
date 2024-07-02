# link : https://www.pythontutorial.net/python-basics/python-boolean/

# Introduction to Boolean data type

"""
In programming, you oftern want to check if a conditions is
true or not and perform some actions based on result.

To represent true and false, Python provides you with the boolean
data type. The boolean value has technical name as 'bool'.

The boolean data type has two values: 'True' and 'False'.

- Note that the boolean values 'True' and 'False' start with
  the capital letters 'T' and 'F'.
"""

# Defines two boolean variables
is_active = True
is_admin = False
print(is_active, is_admin)
# [Output] True False


# Compare two numbers, will returns the result as boolean value
is_under_age = 15 < 18
print(is_under_age)
# [Output] True

is_legal_to_vote = 15 > 18
print(is_legal_to_vote)
# [Output] False


# Compare two strings results in a boolean value
print("a" > "b")
# [Output] False

print("a" < "b")
# [Output] True

# The 'bool()' function

"""
To find out if a value is 'True' or 'False',
you use the 'bool()' function.
"""

# evaluate value if true or false with bool()

print(bool(100))
# [Output] True

print(bool("Hi"))
# [Output] True

# Falsy value

print(False)
# [Output] False

print(bool(None))
# [Output] False

print(bool(""))  # An empty string
# [Output] False

print(bool(0))  # The number zero
# [Output] False

print(bool([]))  # An empty list
# [Output] False

print(bool(()))  # An empty tuple
# [Output] False

print(bool({}))  # An empty dictionary
# [Output] False

"""
As you can see clearly from the output, some values evaluate to
'True' and the others evaluate to 'False'.

When a value evaluates to 'True', it's truthy.
If a value evaluates to 'False', it's falsy.

The truthy values are the other values that are not falsy.
"""


"""
Learn about the Python boolean data type, falsy and truthy values.

[Summary]
- Python boolean data types has two values : 'True' and 'False'.
- Use the 'bool()' function to test if a value is 'True' or 'False'.
- The falsy values evaluate to 'False' while the truthy values
  evaluates to 'True'.
- Falsy values are 'False', 'None', the number zero,
  an empty string, an empty list, an empty tuple, an empty dictionary.
- Truthy values are the values that are not falsy.
"""
