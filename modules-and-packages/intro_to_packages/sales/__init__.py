# link : https://www.pythontutorial.net/python-basics/python-packages/


"""
By convention, when we import a package, python will execute the "__init__.py",
to initialize package-level data.
"""

# import the order module automatically

"""
In addition to initialize package-level data, the "__init__.py" also
allows us to automatically import modules from the packages.
"""


from sales.billing import print_billing

TAX_RATE = 0.03
__all__ = ['order', 'delivery']
