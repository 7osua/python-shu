"""
The pricing module has two functions that calculate the net price and tax
from the selling price, tax rate, and discount.

When you import a module, Python executes all the code from the corresponding file.
In this example, Python executes the code from the "pricing.py" file.
Also, Python adds the module name to the current module.


This module name allows you to access functions, variables, etc.
from the imported module in the current module.
"""


def get_net_price(price, tax_rate, discount=0):
    return price * (1 + tax_rate) * (1 - discount)


def get_tax_rate(price, tax_rate):
    return price * tax_rate
