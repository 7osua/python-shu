"""
link : https://www.pythontutorial.net/python-basics/python-type-conversion/
---------------------------------------------------------------------------
learn about type conversion in Python and some useful type conversion functions.
"""

net_price = input('Enter the price ($) : ')
tax_rate = input('Enter the tax rate (%) : ')
tax_amount = float(tax_rate) * int(net_price) / 100
print(tax_amount)

print("----------------------------")
value = input('Enter a value\n')
print(value)
print(type(value))
