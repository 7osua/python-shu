# link : https://www.pythontutorial.net/python-basics/python-pip/

"""
Learn about pip and how to use it to manage third-party packages.
"""

# Install a Package

import requests

"""
- To install a package from PyPI, you use the following command on Windows :

    pip install <package_name>

- Than, change 'pip' to 'pip3' on macOS and Linux

    pip3 install <packages_name>

For example, the following command installs the 'requests' package:

    pip install requests

The following code uses the 'requests' package to make an HTTP request to the 'https://github.com/7osua'
and displays the HTTP status code.
"""
response = requests.get("https://github.com/7osua")

print(response.headers["content-type"])
print(response.status_code)

# Introduction to Python Package Index (pip)

"""
Python has a rich standard library that you can use immediately in your project.
In case you need a package that isn’t available in the standard library, you can find it on the Python Package Index.

The Python Package Index (PyPI) is the largest Python repository.
It contains many Python packages developed and maintained by the Python community.
"""

# What is "pip"
"""
'pip' is the package installer for Python. Pip allows you to install packages from PyPI and other repositories.
Python comes with pip by default. To check if pip is available on your computer,
you can open the command prompt (or Powershell) on Windows and type the following command:

    pip --V
"""

# List installed packages

"""
To list all installed packages, you use the following pip command:

    pip list

It’ll return a list of packages installed on your computer.
To check what packages are outdated.

    pip list --outdated
"""

# Uninstall a package

"""
To uninstall a package, you use the pip uninstall command:

    pip uninstall <package_name>

It’ll prompt you for a confirmation like this:

    Proceed (y/n)?

If you type y, pip is going to uninstall the package. Otherwise, it won’t do so.
"""

# List dependencies of a package

"""
When you install a package and if that package uses other packages,
'pip' will install the package and its dependency, and also a dependency of dependencies, and so on.
To show the dependencies of a package, you use the following command :

    pip show <package_name>

The Requires line lists out the packages used by the requests packages.
"""

# Summary
# Python package index provides third-party Python packages developed and maintained by the Python community.
# Use Python installer for Python (pip) to manage third-party Python packages.
