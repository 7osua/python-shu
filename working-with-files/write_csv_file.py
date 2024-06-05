# link : https://www.pythontutorial.net/python-basics/python-write-csv-file/


"""
Learn how to write data into a csv file using built-in "csv" module.
"""

import csv

"""
Steps for writing a CSV file
To write data into a CSV file, you follow these steps:

1. First, open the CSV file for writing (w mode) by using the open() function.
2. Second, create a CSV writer object by calling the writer() function of the csv module.
3. Third, write data to CSV file by calling the writerow() or writerows() method of the CSV writer object.
4. Finally, close the file once you complete writing data to it.

- It’ll be shorter if you use the with statement so that you don’t need to call the close() 
  method to explicitly close the file.
- If you’re dealing with non-ASCII characters, 
  you need to specify the character encoding in the open() function.
- To remove the blank line, you pass the keyword argument 
  newline='' to the open() function
"""


# Using  "writerow()" method of the "csv.writer()" function from the "csv" module.

file_to_write = 'write_country.csv'
dir_path = 'files'

header = ['name', 'area', 'country_code2', 'country_code3']
data_row = ['Afghanistan', 652090, 'AF', 'AFG']

file_country = open(f'{dir_path}\\{file_to_write}', mode='w', newline="")
csv_writer = csv.writer(file_country)
csv_writer.writerow(header)
csv_writer.writerow(data_row)
file_country.close()


with open(f"{dir_path}\\{file_to_write}", mode='w', encoding='utf-8', newline='') as file_country_again:
    some_csv_writer = csv.writer(file_country_again)

    some_csv_writer.writerow(header)
    some_csv_writer.writerow(data_row)


# Using "writerows()" method of the "csv.writerows()" from the "csv" module


"""
To write multiple rows to a CSV file at once, 
you use the writerows() method of the CSV writer object.
"""

file_to_write_mul = "write_countries.csv"

header_for_mul_rows = ["name", "area", "country_code2", "country_code3"]
data_rows = [
    ['Albania', 28748, 'AL', 'ALB'],
    ['Algeria', 2381741, 'DZ', 'DZA'],
    ['American Samoa', 199, 'AS', 'ASM'],
    ['Andorra', 468, 'AD', 'AND'],
    ['Angola', 1246700, 'AO', 'AGO']
]

with open(f"{dir_path}\\{file_to_write_mul}", mode='w', newline="") as file_country_mul:

    csv_writer_mul = csv.writer(file_country_mul)
    csv_writer_mul.writerow(header_for_mul_rows)
    csv_writer_mul.writerows(data_rows)


# Using "DictWriter()" class from the "csv" module.

"""
If each row of the CSV file is a dictionary, 
you can use the DictWriter class of the csv module to write the dictionary to the CSV file.

Below is an example how to use "DictWriter" class to write data to a csv file.
"""

# .csv header
header_for_dict_rows = ["name", "area", "country_code2", "country_code3"]

# .csv data
data_rows_for_dict = [
    {'name': 'Albania',
     'area': 28748,
     'country_code2': 'AL',
     'country_code3': 'ALB'},
    {'name': 'Algeria',
     'area': 2381741,
     'country_code2': 'DZ',
     'country_code3': 'DZA'},
    {'name': 'American Samoa',
     'area': 199,
     'country_code2': 'AS',
     'country_code3': 'ASM'}
]

file_to_write_dict_class = 'write_countries_dict.csv'


with open(f'{dir_path}\\{file_to_write_dict_class}', mode='w', encoding='utf-8', newline="") as file_countries_dict:
    csv_writer_dict = csv.DictWriter(file_countries_dict, fieldnames=header_for_dict_rows)
    csv_writer_dict.writeheader()
    csv_writer_dict.writerows(data_rows_for_dict)


"""
How the code example works :

1. First, we define variables that holds the field names and data rows of the csv file.
2. Next, we open/create if file not exist with the "open()" function.
3. Then, we create the new instance of the ".DictWriter" class by passing the file object ("files_countries_dict")
   and the "header_for_dict_rows" variable to "fieldnames" argument.
4. After that, for ".DictWriter()" we call the ".writeheader()" method for writing the header to CSV file.
5. Finally, we the write data rows to the CSV file using the ".writerows()" method.
"""
