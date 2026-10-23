# J-D Laurence

# Task 3

# Within the assignment3 folder, create a file called list-comprehensions.py.
# Add code that reads the contents of ../csv/employees.csv 
# into a list of lists using the csv module.

# The list comprehension should iterate through the items in the
#  list read from the csv file.
# Print the resulting list. Skip the item created for the 
# heading of the csv file.
# Using a list comprehension, create another list from the 
# previous list of names.
# This list should include only those names that contain
#  the letter "e". Print this list.

import csv
import traceback
from pathlib import Path

employees_csv_path = Path(__file__).parent.parent.resolve() / 'csv' / 'employees.csv'


def read_csv_file(file_path):
    try:
        with open(file_path, 'r', newline = '') as file: # r is default anyway
            reader = csv.reader(file)
            headers = next(reader) # we will discard these for now
            rows = list(reader)
        return rows

    except Exception as e:
            trace_back = traceback.extract_tb(e.__traceback__)
            stack_trace = list()
            for trace in trace_back:
                stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
            print(f"Exception type: {type(e).__name__}")
            message = str(e)
            if message:
                print(f"Exception message: {message}")
            print(f"Stack trace: {stack_trace}")

employees_list = read_csv_file(employees_csv_path)

format_list = [f"{row[1]} {row[2]}" for row in employees_list] #list comprehension
print(format_list)

list_e = [name for name in format_list if 'e' in name] # list comprehension, better than a combination of a lambda and a map and a filter
print(list_e)