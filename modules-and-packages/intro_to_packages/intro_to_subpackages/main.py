"""
- A Python package contains one or more modules. Python uses the folders and files structure to manage packages and modules.
- Use the "__init__.py" file if you want to initialize the package-level data.
- Use "__all__" variable to specify the modules that will load automatically when importing the package.
A package may contain subpackages.
"""

from sales import TAX_RATE
from sales.billing_sub_sales import *
from sales.delivery_sub_sales import delivery
from sales.order_sub_sales import order, DEFAULT_ITEMS

billing.handle_billing()
billing.resolve_billing()
cancel_billing.cancel_billing_handle()
delivery.handle_delivery()
order.handle_order()

print(f'TAX_RATE = {TAX_RATE}')
print(f'Order DEFAULT_ITEMS = {DEFAULT_ITEMS}')
