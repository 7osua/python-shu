'''
link : https://www.pythontutorial.net/python-basics/python-unpack-list/
-----------------------------------------------------------------------
Learn how to unpack a list in Python to make your code more concise.
- Unpacking assigns elements of the list to multiple variables.
- Use the asterisk (*) in front of a variable like this *variable_name to pack the leftover elements of a list into another list.
'''

# Introduction to list unpacking
colors = ['red', 'green', 'blue']

red = colors[0]
green = colors[1]
blue = colors[2]

print(colors)
print(red, green, blue)

# sequence unpacking, you can assign elements of a list (and also a tuple) to multiple variables.
red, green, blue = colors
print(red, green, blue)

# red, green = colors # Error
# print(red, green)

# Unpacking Vs. Packing
red, green, *others = colors
print(red, green, others)

more_colors = ['cyan', 'magenta', 'yellow', 'black']
cyan, magenta, *others = more_colors
print(cyan, magenta, others)
