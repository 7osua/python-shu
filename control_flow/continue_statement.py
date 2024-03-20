'''
link : https://www.pythontutorial.net/python-basics/python-continue/
-----------------------------------------------------------------------
Learn about the Python continue statement and how to use it to control the loop.
'''

#  'continue' statement in a 'for' loop example
for index in range(10):
    if (index % 2):
        continue
    print(f'{index} % 2 = {index % 2}')
    print(index)

#  'continue' statement in a 'while' loop example
counter = 0
while counter < 10:
    counter += 1

    if not counter % 2:
        continue

    print(f'not {counter} % 2 = {not counter % 2}')
    print(counter)
