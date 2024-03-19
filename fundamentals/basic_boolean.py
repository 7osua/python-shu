'''
link : https://www.pythontutorial.net/python-basics/python-boolean/
-------------------------------------------------------------------
learn about the Python boolean data type, falsy and truthy values.
'''

is_active = True
is_admin = False
print(is_active, is_admin)

is_under_age = 20 > 18
print(is_under_age)

print('a' > 'b')
print('a' < 'b')

# evaluate value if true or false with bool()
print(bool(100))
print(bool('Hi'))

# falsy value
print(False)
print(bool(''))
print(bool(0))
print(bool(None))
print(bool([]))
print(bool(()))
print(bool({}))
