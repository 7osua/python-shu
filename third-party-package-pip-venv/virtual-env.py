# link : https://www.pythontutorial.net/python-basics/python-virtual-environments/


# Why we need Virtual Environment

import sys
import site

print(sys.prefix)
print(site.getsitepackages())

"""
Python stores all system packages in a specified folder when installing Python.
Typically, most system packages locate at subfolders of a path specified in the sys.prefix.
To find this path, you can import the sys module and display it as follows.

When you use pip to install third-party packages,
Python stores these packages in a different folder specified by the 'site.getsitepackges()' function.

You’ll be fine if you have some projects that use only standard Python libraries.
However, it’ll be a problem when you have some projects that use third-party packages.

Suppose you have two projects that use different versions of a library.
Since there is only one location to store the third-party packages,
you cannot keep different versions at the same time.

A workaround is that you can use the 'pip' command to switch between versions by installing/uninstalling the packages.
However, it will be time-consuming and not scale very well.

This is where virtual environments come into play.
"""
# What is a Python virtual environment
"""
Python uses virtual environments to create an isolated environment for every project.
In other words, each project will have its own directory to store third-party packages.

In case you have multiple projects that use different versions of a package,
you can store them in separate virtual environments.

Python includes the virtual environment module (venv) as a standard library since version 3.3.
"""

# Using the venv module to create a virtual environment

"""
The following example shows you how to create a new project on Windows,
which uses a virtual environment created by the venv built-in module.

1. First, create a new folder for hosting the project and virtual environment

	mkdir test-env
	cd test-env

2. Create a virtual environment with the name 'project_test' inside the 'test_env' folder:

	python -m venv project_test

The above command will create a new folder called 'project_test' with
all necessary tools and libraries for running Python programs.

Use the following command to check where the python.exe is located:

	where python

It’ll return the following path indicating that the python.exe is located in the installation folder:

	C:\Python\python.exe

1. First, activate the virtual environment by running the activate.bat file in the project_env/Scripts directory:

	project_test\Scripts\activate

Once executed, you’ll see the following in the terminal:

	(project_env) D:\test_env\project_env\Scripts>

The prefix (project_test) indicates that you’re in the project_test virtual environment.

Now, you can check where the python.exe is located again:

	where python

This time it returns the following paths:

	D:\test_env\project_test\Scripts\python.exe
	C:\Python\python.exe

The first line shows that the python.exe is located in the project_env/Scripts folder.
It means that if you run the python command within the project_test,
the D:\test_env\project_test\Scripts\python.exe will execute instead of C:\Python\python.exe.

This command executes the python.exe from the project_env and loads the packages
installed in the project_env virtual environment.

To deactivate the virtual environment, you can run the deactivate command:

	deactivate

It’ll return the following:

	D:\test_env\web_crawler>
"""

"""
Learn about virtual environment and how to use 'venv' module to create a virtual environment.
1. A virtual environment creates an isolated environment for a Python project.
2. Use the venv module to create a new virtual environment.
"""
