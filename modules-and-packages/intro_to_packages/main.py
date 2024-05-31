# link : https://www.pythontutorial.net/python-basics/python-packages/


"""
Learn about the packages and how to use them to structure application.

- When the number of modules grows. it will become difficult to keep them in one location.
- The packages allow us to organize modules in the hierarchical structure.


- The way Python organizes packages and modules like the Operating System structures the folders and files.
- To create a package, you create a new folder and place the relevant modules in that folder.
- To instruct Python to treat a folder containing files as a package,
  you need to create a "__init__.py" file in the folder.
"""

# Introduction to the packages.


# import sales.billing as billing
# import sales.delivery as delivery
# import sales.order as order
# Importing Packages
# from sales import TAX_RATE
# from sales import *

"""
To access an object from a module that belong to package, se use the "." notation
"""

# order.print_order()
# delivery.print_delivery()
# billing.print_billing()
# print(TAX_RATE)


from sales import *
import sales

order.print_order()             # call a module object reference with "from <package> import *"
delivery.print_delivery()       # call a module object reference with "from <package> import *"
print(sales.TAX_RATE)           # calling module after Initializing a package in "__init__.py" with "import sales"
sales.billing.print_billing()   # calling module after Initializing a package in "__init__.py" with "import sales"
