'''
link: https://www.pythontutorial.net/python-basics/python-while/
-----------------------------------------------------------------
Learn about the Python while statement and how to use it to run a code block as long as a condition is true.
'''

# while statement
max = 5
counter = 0

while counter < 5:
    print(counter)
    counter += 1


command = ''

while command.lower() != 'quit':
    command = input('> ')
    print(f'echo: {command}')
