# link : https://www.pythontutorial.net/python-basics/python-directory/

"""
- Use the os.getcwd() function to get the current working directory.
- Use the os.chdir() function to change the current working directory to a new one.
- Use the os.mkdir() function to make a new directory.
- Use the os.rename() function to rename a directory.
- Use the os.rmdir() function to remove a directory.
- Use the os.walk() function to list the contents of a directory.
"""

import os

# Get the current directory
current_directory = os.getcwd()
base_directory = current_directory

print(current_directory)

os.chdir(r"..\fundamentals")
current_directory = os.getcwd()
print(current_directory)

"""
Get the current working directory.
The current working directory is the directory where the Python script is running.

To change the current working directory we can use the ".chdir()".
The ".chdir()" will change the value of the "current_directory" variable 
to the "../fundamentals" directory by re-assign new returned value of the 
'.getcwd()' function.
"""

# Joint and split the path

os.chdir(base_directory)
current_files = 'intro_directories.py'
join_base_directory_path = os.path.join(base_directory, current_files)
split_base_directory_path = os.path.split(join_base_directory_path)

print(join_base_directory_path)
print(split_base_directory_path)

"""
To make a program working across platform including windows, linux, and mac os
we need to use platform-independent file and directory path.

We can use the 'os.path' sub-module that contains several useful functions and constants
to join and split paths.

The join() function joins path components together and returns a path with the corresponding path separator. 
For example, it uses backslash (\) on Windows and forward slash (/) on macOS or Linux.

The split() function splits a path into components without a path separator. 
"""

# Test if a path is a directory

is_directory = True if os.path.exists(base_directory) and os.path.isdir(base_directory) else False
is_file = True if os.path.exists(join_base_directory_path) and os.path.isdir(join_base_directory_path) else False
print(f"is \"{base_directory}\" a directory : {is_directory}")
print(f"is \"{join_base_directory_path}\" a directory : {is_file}")

"""
To check if a path exists and is a directory, 
you can use the functions 'os.path.exists()' and 'os.path.isdir()' functions. 
"""


# Create a directory

new_directory_name = "new_directory"

if os.path.exists(new_directory_name):
    print(f'Failed, the {new_directory_name} already exist!')
else:
    os.mkdir(new_directory_name)
    print(f'Success, the {new_directory_name} has been created.')


"""
To create a new directory, we can use the "os.mkdir()" function.
Before created a new directory always check if a directory exists
first before creating a new directory.
"""

# Rename a directory

re_named_directory = "most_recent_directory"

if (os.path.exists(new_directory_name)) and (not os.path.exists(re_named_directory)):
    os.rename(new_directory_name, re_named_directory)
    print(f'Success, renaming the "{new_directory_name}" directory to "{re_named_directory}".')
else:
    print(f'Failed, the "{re_named_directory}" already exist!')

"""
To rename the directory, you use the os.rename() function.
"""

# Delete a directory

if os.path.exists(new_directory_name):
    os.rmdir(new_directory_name)
    print(f'Success, deleting the "{new_directory_name}".')
else:
    print(f'Failed, deleting the "{new_directory_name}", dir does not exists.')


"""
To delete a directory, you use the os.rmdir() function.
"""


# Traverse a directory recursively

path_to_d_partition = r"D:\\Music"

for root, dirs, files in os.walk(path_to_d_partition):
    print("{0} has {1} files.".format(root, len(files)))


"""
The os.walk() function allows you to traverse a directory recursively. 
The os.walk() function returns the root directory, the sub-directories, 
and files.
"""
