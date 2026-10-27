# J-D Laurence
# 10 Oct 2026

# Task 2

import csv
import traceback
import os
import custom_module
from datetime import datetime
from pathlib import Path # this is to make it easier to locate the csv file no matter where the script or debugger is being run


def read_employees():
    employees_dict = {}
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
            employees_dict['fields'] = fields
            employees_dict['rows'] = rows

        return employees_dict
   
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

#print(all_employees_dict())

# Task 10
def get_this_value():
    return os.environ.get('THISVALUE')

#print(get_this_value())


# Task 11
def set_that_secret(secret):
    custom_module.set_secret(secret)

#set_that_secret("butterfly")
#print(custom_module.secret)

# Task 12
def read_minutes():
    minutes1_path = Path(__file__).parent.parent / 'csv' / 'minutes1.csv' 
    minutes2_path = Path(__file__).parent.parent / 'csv' / 'minutes2.csv'

    def csv_to_dict(file_path):
        try: 
            with open(file_path, 'r') as file:
                reader = csv.reader(file)
                fields = tuple(next(reader))            
                rows = [tuple(row) for row in reader]
                output = {"fields": fields, "rows" : rows}
        
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
        return output
    
    minutes1 = csv_to_dict(minutes1_path)
    minutes2 = csv_to_dict(minutes2_path)
    
    return minutes1, minutes2

minutes1, minutes2 = read_minutes()
# print(minutes1)
# print(minutes2)

# Task 13
def create_minutes_set():
    
    # set1 = set()
    # set2 = set()
    # for row in minutes1["rows"]:
    #     set1.add(row)
    # for row in minutes2["rows"]:
    #     set2.add(row)  

    # but since the set constructor takes an interable, it's quicker (and does the same thing) to do this:
    set1 = set(minutes1["rows"])
    set2 = set(minutes2["rows"])
    return set1.union(set2) # a union combines the two and removes any duplicates
   
    # this could even be simplified to
    # return set(minutes1["rows"]) | set(minutes2["rows"]) since the bar is a union operator for sets
    # equivalent to the 'or' operator since we want items in one or the other 

minutes_set = create_minutes_set()
# print(len(minutes1["rows"]), len(minutes2["rows"]))
# print(len(set(minutes1["rows"])), len(set(minutes2["rows"])))
# print(len(create_minutes_set()))

# Task 14
def create_minutes_list():
    mins_list = list(minutes_set)
    formatted_mins_list = list(map(lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")), mins_list))
    return formatted_mins_list

minutes_list = create_minutes_list()
# print(minutes_list)

# Task 15
def write_sorted_list():
    minutes_list.sort(key=lambda item: item[1]) #this tells it to sort by the value of item[1] for each in the list, which is the date
    converted_mins_list = list(map(lambda x: (x[0], datetime.strftime(x[1], "%B %d, %Y")), minutes_list))
    minutes_path = Path(__file__).parent / 'minutes.csv' 
    try:
        with open(minutes_path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(minutes1["fields"])
            writer.writerows(converted_mins_list)  

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
    return converted_mins_list

write_sorted_list()


                            
    

