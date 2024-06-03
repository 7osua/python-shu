# link : https://www.pythontutorial.net/python-basics/python-create-text-file/


"""
Learn how to create a new text file using the open() function.
- Use the open() function with the 'w' or 'x' mode to create a new text file.

To create a new text file, you use the open() function.
The open() function has many parameters :

    a_file = open("path_to_file", "mode")

In this syntax, the path_to_file parameter specifies the path to the text file that you want to create.

For creating a new text file, you use one of the following modes:

'w' – open a file for writing. If the file does not exist,
      the open() function creates a new file. Otherwise, it’ll overwrite the contents of the existing file.
'x' – open a file for exclusive creation. If the file exists,
      the open() function raises an error (FileExistsError). Otherwise, it’ll create the text file.

"""

filename = 'hello.txt'
existing_file = 'already_exist_file.txt'
dirname = 'unknown-dir'

with open(f'files/{filename}','w') as a_file:
    a_file.write("Hello world, from python!")
    a_file.close()

"""
In this example, Python raises an exception because the "unknown-dir" directory does not exist. 
Therefore, it could not create the "hello.txt" file in that directory.
Also, you can handle the exception using the try-except statement as follows:
"""
try:
    one_more_file = open(f'{dirname}/{filename}', 'w')
    a_file.write('Hello world, from python 02')
    a_file.close()
except FileNotFoundError:
    print(f'The {dirname} directory does not exist !02.')


"""
If you don’t want to create a new text file in case it already exists, 
you can use the 'x' mode when calling the open() function.
"""
try:
    file_to_write = open(f'files/{existing_file}', 'x')
    file_to_write.write('Hello world, from python 03.')
    file_to_write.close()
except FileExistsError:
    print(f'Error! The {filename} already exist !03.')


"""
In this example, Python raises an exception because the file already exist. 
Therefore, it could not create the "already_exist_file.txt" file in 'files' directory.
Also, you can handle the exception using the try-except statement as follows:
"""
try:
    another_file = open(f'files/{existing_file}', 'x')
    another_file.write('Hello world, from python 04.')
    another_file.close()
except FileExistsError:
    print(f'Error! The {filename} already exist !04.')
