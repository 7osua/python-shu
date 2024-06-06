# link : https://www.pythontutorial.net/python-basics/python-rename-file/
# Learn how to rename a file using the "os.rename()" function.


"""
Summary : Use the "os.rename()" function to rename a file.
"""
import os


old_file_name = "learn_material.txt"
new_file_name = "learn_material_update_file_name.txt"
dir_path = "files"

try:
    os.rename(f"{dir_path}\\{old_file_name}", f"{dir_path}\\{new_file_name}")
except FileNotFoundError as error:
    print(error)
except FileExistsError as error:
    print(error)


"""
To rename a file, you use the os.rename() function.

    import from os
    
    os.rename(src, dist)
    
If the "src" file does not exist, the "os.rename()" function raises a "FileNotFound" error.
Similarly, if the "dst" file already exist, the "os.rename()" function raise a "FileExistError" error.


To avoid an error if the "learn_material.txt" doesn’t exist and/or the "learn_material_update_file_name.txt" 
file already exists, you can use the try:...except: statement.
"""
