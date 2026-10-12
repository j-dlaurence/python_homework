# J-D Laurence
# 10 Oct 2026

# Task 2

import csv
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
print(employees)