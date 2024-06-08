# link : https://www.pythontutorial.net/python-basics/python-delete-file/


import os

file_to_delete = 'already_exist_file.txt'
path = 'files'
is_file_exist = os.path.exists(f'{path}\\{file_to_delete}')

if is_file_exist:
    os.remove(f'{path}\\{file_to_delete}')
    print(f'Success, deleting the {file_to_delete} file! ')
else:
    print(f'Failed, the {file_to_delete} file does not exist! ')


try:
    os.remove(f'{path}\\{file_to_delete}')
    print(f'Success, deleting the {file_to_delete} file! ')
except FileNotFoundError:
    print(f'Failed, the {file_to_delete} file does not exist! ')

"""
To delete a file we can use the ".remove()" function of the "os" built-in module.

    import os
    os.remove(file)
    

if the "file" does not exist, the "os.remove()" will issue a "FileNotFoundError" error.

To avoid the error we check if the "file" exists before deleting it.
Alternatively we can use "try:...except:..." statement to catch the exception
if the file does not exist.
"""
