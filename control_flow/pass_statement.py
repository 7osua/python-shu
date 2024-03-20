'''
link : https://www.pythontutorial.net/python-basics/python-pass/
----------------------------------------------------------------------
learn how to use the Python pass statement as a placeholder.
Use the "pass" statement to create a placeholder for the code that you’ll implement later.
'''

counter = 0
max = 10

# pass statement with the if statement example
if counter <= max:
    counter += 1
else :
    pass

print(counter)

# pass statement with the for statement example
for i in range(1,100):
    pass

# pass statement with the while statement example
while counter != 2:
    pass
    counter += 1
print(counter)


# pass statement with functions and classes
def fn():
    pass

class stream:
    pass
