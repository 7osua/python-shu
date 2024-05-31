# link : https://www.pythontutorial.net/python-basics/python-module/

"""
Learn about modules, how to import objects from module, and how to developing with modules.
- A module is a Python source code file with the .py extension.
  The module name is the Python file name without the extension.
- To use objects from a module, you import them using the import statement.
"""


# Introduction to modules

# 1. Import "module_name"
import pricing
# 2. Import "module" as "module_new_name"
import pricing as selling_price
# 3. from "module_name" import "object_name"
from pricing import get_net_price
from pricing import get_tax_rate
# 4. from "module_name" import "object_name" as "object_new_name"
from pricing import get_net_price as calculate_net_price



"""
A a module is a piece of software that has a specific functionality.
A python module is a file that contains code.

A module has a name specified by filename without ".py" extension.
For example, if we have a file called "pricing.py", the module name
is "pricing"


To use objects defined in a module from another file, 
you can use the import statement.
"""


net_price = pricing.get_net_price(price=100, tax_rate=0.01)
net_price_using_new_name_module = selling_price.get_net_price(price=100, tax_rate=0.02)
net_price_with_object_reference_net_price = get_net_price(price=100, tax_rate=0.03)
tax_rate_with_object_reference_tax_rate = get_tax_rate(price=100, tax_rate=0.03)
net_price_with_new_name_reference_object = calculate_net_price(price=100, tax_rate=0.04)
print(f'net_price = {net_price}')
print(f'net_price_using_new_name_module = {net_price_using_new_name_module}')
print(f'net_price_with_object_reference_net_price = {net_price_with_object_reference_net_price}')
print(f'tax_rate_with_object_reference_tax_rate = {tax_rate_with_object_reference_tax_rate}')
print(f'net_price_with_new_name_reference_object = {net_price_with_new_name_reference_object}')
