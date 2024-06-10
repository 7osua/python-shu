# link : https://www.pythontutorial.net/python-basics/python-list-files/

"""
Learn how to list files in a directory using the "os.walk()" function.

Sometimes, you may want to list all files from a directory for processing.
To list all files in a directory, we can use the "os.walk()" function.

The "os.walk()" function generates file names in a directory by walking the tree
either top-down or bottom-up.

The os.walk() function yields a tuple with three fields
(dirpath, dirnames, and filenames) for each directory in the directory tree.

Note that the os.walk() function examines the whole directory tree. Therefore,
we can use it to get all files from all directories and their subdirectories of a root directory.

summary :
- Use the 'os.walk' function to list files in a directory recursively.
- Define a reusable function for listing files in a directory using the 'os.walk()' funtion.
"""

import os

# Introduction to list file example

"""
The following example shows how to use the os.walk() function to list all HTML files 
from the 'F:\\StockbitBibit\bibit' directory:
"""
path_to_bibit = r"F:\\StockbitBibit\bibit"

# webm_files = []
#
# for dir_paths, dir_names, filenames in os.walk(path_to_bibit):
#     for filename in filenames:
#         if filename.endswith(".webm"):
#             webm_files.append(os.path.join(dir_paths, filename))
#         # print("dir_paths = ", dir_paths)
#         # print("dir_names = ", dir_names)
#         # print("filenames = ", filenames)
#
#
# for file in webm_files:
#     print(file)


"""
So how code above works :
1. First, we defined the target path which is 'F:\\StockbitBibit\bibit'.
2. Second,  initialize a list to store the path to 'webm_files'.
3. Next, call os.walk() function to examine directories of the 'F:\\StockbitBibit\bibit'
   The 'dirpath' stores the directory and 'filenames' store files in that directory.
4. Then, loop over the 'filenames' and add them to 'webm_files' list if their
   extensions are '.webm'
5. Finally, print output the filenames in the webm_files list:
  

Note that the 'os.path.join()' function returns 
the full path of the filename by joining the 'dirpath' with the 'filename'.
"""


# Defining a reusable list files function


def list_files_bibit(path, extentions=None):
    """ List all files in a directory specified by path
    Args:
        path - the root directory path
        extensions - a iterator of file extensions to include, pass None to get all files.
    Returns:
        A list of files specified by extensions
    """
    filepaths = []
    for root, _, files in os.walk(path):
        for file in files:
            if extentions is None:
                filepaths.append(os.path.join(root, file))
            else:
                for ext in extentions:
                    if file.endswith(ext):
                        filepaths.append(os.path.join(root, file))

    return filepaths

# Make list files function more efficient


def list_files_more_efficient(path, extensions=None):
    """ List all files in a directory specified by path
    Args:
        path - the root directory path
        extensions - a iterator of file extensions to include, pass None to get all files.
    Returns:
        A list of files specified by extensions
    """

    for root, _, files in os.walk(path):
        for file in files:
            if extensions is None:
                yield os.path.join(root, file)
            else:
                for ext in extensions:
                    if ext.endswith(ext):
                        yield os.path.join(root, file)


if __name__ == "__main__":
    # bibit_filepaths = list_files_bibit(path_to_bibit, ('.webm', '.mkv'))
    # for bibit_file in bibit_filepaths:
    #     print(bibit_file)

    another_bibit_filepaths = list_files_more_efficient(path_to_bibit, ('.webm', 'mkv'))
    for another_bibit_file in another_bibit_filepaths:
        print(another_bibit_file)

    print("\nUsing 'Generator' to yield each file at a time.")
    """
    If the number of files is small, the 'list_files_bibit()' function works fine. 
    However, when the number of files is large, returning a large list of files is not memory efficient.
    To resolve this, you can use a generator to yield each file at a time instead of returning a list
    """
