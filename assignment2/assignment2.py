# J-D Laurence
# 10 Oct 2026

# Task 2

import csv
import traceback

from pathlib import Path # this is to make it easier to locate the csv file no matter where the script or debugger is being run


def read_employees():
    dict = {}
    csv_path = Path(__file__).parent.parent / 'csv' / 'employees.csv' # __file__ refers to the location of this script; Path turns that into a path object
    try: 
        with open(csv_path, 'r') as file:
            reader = csv.reader(file)          
            
            # One way to do this is:
            # rows = []
            # for row in reader:
            #    rows.append(row)
            
            # now we put the first line into 'fields' and delete it, and put the rest into 'rows
            # dict['fields'] = rows[0]
            # del rows[0]
            # dict['rows'] = rows

            # however there is an easier way, because reader is an iterator. When we call next() on an iterator
            # it returns the next line but also moves the current position onward once, so that when we use the 
            # iterator again it starts from the next entry, meaning we can easily put the rest into rows:

            fields = next(reader)
            rows = list(reader) 
            dict['fields'] = fields
            dict['rows'] = rows

        return dict
   
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

       
employees = read_employees()
#print(employees)


# Task 3
def column_index(field):
    index = employees["fields"].index(field)
    return index


employee_id_column = column_index("employee_id")
# print(employee_id_column)

# Task 4
def first_name(row):
    first_name_col = column_index("first_name")
    # row_list =  employees["rows"]
    # row = row_list[row]
    # rtn_val = row[first_name_col]
    # return rtn_val

    return employees["rows"][row][first_name_col]

#print(first_name(2))

# Task 5
def employee_find(employee_id):
    def employee_match(row):
        return int(row[employee_id_column]) == employee_id

    matches=list(filter(employee_match, employees["rows"]))
    return matches

# Task 6
def employee_find_2(employee_id):
    matches = list(filter(lambda row : int(row[employee_id_column]) == employee_id , employees["rows"]))
    return matches

# Task 7
def sort_by_last_name():
    # sort() calls this on each row and sorts by whatever it returns,
    # so it returns the last name from the row.
    # We look up the column position by name rather than hard-coding 2,
    # in case the column order in the csv ever changes.
    # def last_name_key(row):
    #     last_name_col = column_index("last_name")
    #     return row[last_name_col] 
  
    # employees["rows"].sort(key=last_name_key) # this line first identifies the last_name for each row, using the last_name_key function
    # and then every row in employees["rows"] is sorted on that value. Sort() automtically passes the next list object to the function
    # which in this case represents a row, so we refer to that variable as row as a parameter for the key function
    # return employees["rows"]

    # But we can do this quicker with a lamda
    employees["rows"].sort(key = lambda row : row[column_index("last_name")] )
    return employees["rows"]
    # this is equivalent: the sort function is being passed a key that is each row at a time being turned into the col index of last_name in that row

# Task 8
def employee_dict (row):
    # employee = dict.fromkeys (employees["fields"]) # this line creates a new dictionary and fills the keys from the iterable supplied
    # for i, key in enumerate(employee):
    #     employee[key] = row[i]

    # del employee["employee_id"] # we are told not to include this
    # return employee

    # An easier way is to use zip()
    employee  = dict(zip(employees["fields"], row))
    del employee["employee_id"] # we are told not to include this
    return employee

row = employees["rows"][3]
#print(employee_dict(row))

# Task 9
# Create a function called all_employees_dict.

# The keys in the dict are the employee_id values from the rows in the employees dict.
# For each key, the value is the employee dict created for that row. (Use the employee_dict function you created in task 8.)
# The function should return the resulting dict of dicts.

# Add a line to your program that calls this function and prints the result.

# Get the test working.

def all_employees_dict():
    # output = {}
    # employee_id_index = column_index("employee_id")
    # for row in employees["rows"]:
    #     employee_id = row[employee_id_index]
    #     employee_data = employee_dict(row)
    #     output[employee_id] = employee_data
    # return output

    # or we use dict comprehension, which is the name given for defining a dict comprehensively in this manner:
    employee_id_index = column_index("employee_id")
    return {row[employee_id_index]: employee_dict(row) for row in employees["rows"]}

print(all_employees_dict())

    

