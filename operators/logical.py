'''
link : https://www.pythontutorial.net/python-basics/python-logical-operators/
-----------------------------------------------------------------------------------------
Learn about Python logical operators and how to use them to combine multiple conditions.
Sometimes, you may want to check multiple conditions at the same time. To do so, you use logical operators.
'''

price = 9.99

# The "and" operator
print(f'price > 9 and price < 10 = {price > 9 and price < 10}')
print(f'price > 10 and price < 20 = {price > 10 and price < 20}')

# The "or" operator
print(f'price > 10 or price < 20 = {price > 10 or price < 20}')
print(f'price > 10 or price < 5 = {price > 10 or price < 5}')

# The "not" operator
price = 9.99
print(f'not price > 10 = {not price > 10}')
print(f'not price < 10 = {not price < 10}')

# Combine logical operators
print(f'not (price > 5 and price < 10) = {not (price > 5 and price < 10)}')

# Precedence of Logical Operators
