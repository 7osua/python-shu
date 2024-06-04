# link : https://www.pythontutorial.net/python-basics/python-check-if-file-exists/

"""
Learn how to check if a file exists.
When processing files, you’ll often want to check if a file exists
before doing something else with it such as reading from the file or writing to it.
To do it, you can use the ".exists()" function from the "os.path" module
or ".is_file()" method from the "Path" class in the "pathlib" module.

    from os.path import exists  # Using standard library, which exists() is a function.
    from pathlib import Path    # Using object-oriented approach, which "Path" is a class contain "is_file()" method.

    file_exists = exists(path_to_file)


    path = Path("path_to_file\\filename.txt")
    path.is_file()


- Use os.path.exists() function or Path.is_file() method to check if a file exists.

"""

from os.path import exists
from pathlib import Path

# Using os.path.exists() function to check if file exist

file_to_check = 'hello.txt'
path_to_file = 'files'

is_file_existing = exists(f'{path_to_file}\\{file_to_check}')
print(f'is_file_existing = {is_file_existing}')


# Using pathlib module to check if file exists
is_filepath_existing = Path(f'{path_to_file}\\{file_to_check}')
print(f'is_filepath_existing = {is_filepath_existing.is_file()}')

if is_filepath_existing.is_file() and is_file_existing:
    print(f'The file {path_to_file}\\{file_to_check} exist.')
else:
    print(f'The file {path_to_file}\\{file_to_check} does not exist.')
