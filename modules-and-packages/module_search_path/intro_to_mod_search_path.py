# link : https://www.pythontutorial.net/python-basics/python-module-search-path/

"""
Learn how module search path works in when we import a module into a program.
When you import a module,
Python will search for the module file from the folders specified in the "sys.path" variable.

Python allows you to modify the module search path by changing, adding,
and removing elements from the "sys.path" variable.
"""


# Introduction to module search path
import sys


sys.path.append("F:\\LearnEarn\\Now\\01-write\\python-shu-ha-ri\\python-shu\\modules-and-packages\\module_search_path\\modules\\")


# Modifying the module search path at runtime


for path in sys.path:
    print(path)

import recruitment
recruitment.hire()
