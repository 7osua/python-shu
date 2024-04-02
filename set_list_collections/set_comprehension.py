'''
link : https://www.pythontutorial.net/python-basics/python-set-comprehension/
-----------------------------------------------------------------------------
Learn how to use Python set comprehension to create a new set based on an existing one.

Use Python set comprehension to create a new set based on an existing set
by applying an expression to each element of the existing set.
'''


# Introduction to set comprehension
tags = {'Pandas', 'Numpy', 'Django'}

lowercase_tags = set()
uppercase_lambda_tags = set()
uppercase_expression_tags = set()
uppercase_expression_if_tags = set()

for tag in tags:
    lowercase_tags.add(tag.lower())

uppercase_lambda_tags = set(map(lambda tag: tag.upper(), tags))
uppercase_expression_tags = set([tag.upper() for tag in tags])
uppercase_expression_if_tags = {tag.upper() for tag in tags if tag != 'Numpy'}

print(tags)
print(lowercase_tags)
print(uppercase_lambda_tags)
print(uppercase_expression_tags)
print(uppercase_expression_if_tags)
