# link : https://www.pythontutorial.net/python-basics/python-__name__/


"""
Learn about the "__name__" variable and how to use it.

- Python assign the '__main__' to the __name__ variable when you run the script
  directly and the module name if you import the script as a module.
- Since the __name__ variable has double underscores at both sides, it’s called dunder name.
  The dunder stands for double underscores.
- The __name__ is a special variable in Python.
  It’s special because Python assigns a different value to it depending on how its containing script executes.
  When you import a module, Python executes the file associated with the module.
- When you run the script directly, Python sets the __name__ variable to '__main__'.
- However, if you import a file as a module, Python sets the module name to the __name__ variable.
"""


import billing

print(f'Running from : {__name__} => billing.py') # if the "billing" module imported and used in "main.py"
print(f'Running from : {__name__} => main.py')
billing.print_billing_docs()
