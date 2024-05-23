# link : https://www.pythontutorial.net/python-basics/python-for-else/


"""
Learn how to use for:...else:... statement and how to use it effectively.
- The for statement can have an optional else clause.
- Use Python for else statement to execute a code block
  if the loop does not encounter a break statement or if
  the iterables object has no item.
"""

# Introduction to for:...else:... statement


# Example
"""Search a person by name"""
people = [{'name': 'John', 'age': 25},
          {'name': 'Jane', 'Age': 22},
          {'name': 'Peter', 'age': 30},
          {'name': 'Jenifer', 'Age': 28}]

name = input('Enter a name : ')
# found = False # If not using for:...else:... statement

for person in people:
    if person['name'].lower() == name.lower():
        # found = True  # Id not using for:...else:... statement
        print(person)
        break
# if not found : # Id not using for:...else:... statement
else:
    print(f'{name} not found!')
