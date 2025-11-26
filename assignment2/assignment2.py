import csv
import traceback
import os
import custom_module
from datetime import datetime

#task 2
def read_employees():
    employees = {
        "fields": [],
        "rows": []
    }
    try:
        with open("../csv/employees.csv", "r") as f:
            reader = csv.reader(f)
            for i, row in enumerate(reader):
                if i == 0:
                    employees["fields"] = row
                else:
                    employees["rows"].append(row)
            return employees
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
        return employees


employees = read_employees()
print(employees)

#task 3
def column_index(column_name):
    return employees["fields"].index(column_name)

employee_id_column = column_index("employee_id")
print(employee_id_column)

#task4
def first_name(row_number):
    inx = column_index("first_name")
    row = employees["rows"][row_number]
    return row[inx]

print(first_name(1))

#task5
def employee_find(employee_id):
    def employee_match(row):
        return int(row[employee_id_column]) == employee_id 
    matches=list(filter(employee_match, employees["rows"]))
    return matches

print(employee_find(7))

#task6
def employee_find_2(employee_id):
   matches = list(filter(lambda row : int(row[employee_id_column]) == employee_id , employees["rows"]))
   return matches

print(employee_find_2(7))

#task7
def sort_by_last_name():
    last_name_column= column_index("last_name")
    employees["rows"].sort(key=lambda row: row[last_name_column])
    result = employees["rows"]
    return result

print(sort_by_last_name())

#task8
def employee_dict(row):
    fields = employees["fields"]
    result = {}
    id_index = column_index("employee_id")
    for i in range(len(fields)):
        if i == id_index:
            continue
        else:
            key = fields[i]
            value = row[i]
            result[key] = value
    return result

print(employee_dict(employees["rows"][0]))

#task9
def all_employees_dict():
    result = {}
    id_col = column_index("employee_id")
    for row in employees["rows"]:
        employee_id = row[id_col]
        info = employee_dict(row)
        result[employee_id] = info
    return result

print(all_employees_dict())

#task10
def get_this_value(*args):
    return os.getenv("THISVALUE")

#task11
def set_that_secret(new_secret):
    custom_module.set_secret(new_secret)

set_that_secret("CTD is cool")
print(custom_module.secret)

#task12

def read_minutes():
    
    def read_help(path):
        result = {
        "fields":[],
        "rows":[]
    }
        with open(path) as f:
            reader = csv.reader(f)

            for i, row in enumerate(reader):
                if i == 0:
                    result["fields"] = row
                else:
                    result["rows"].append(tuple(row))
            return result
            
    minutes1 = read_help("../csv/minutes1.csv")
    minutes2 = read_help("../csv/minutes2.csv")

    return minutes1, minutes2

minutes1, minutes2 = read_minutes()
print(minutes1)
print(minutes2)

#task13
def create_minutes_set():
    min1 = set(minutes1["rows"])
    min2 = set(minutes2["rows"])
    minutes_set = min1.union(min2)
    return minutes_set

minutes_set = create_minutes_set()
print(minutes_set)

#task14
def create_minutes_list():
    lst = list(minutes_set)
    mapped = map(lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")),lst)
    result = list(mapped)
    return result

minutes_list = create_minutes_list()

#task15
def write_sorted_list():
    sorted_list = sorted(minutes_list, key=lambda x: x[1])
    mapped = map(lambda x: (x[0], x[1].strftime("%B %d, %Y")), sorted_list)
    result = list(mapped)

    with open("./minutes.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(minutes1["fields"])
        for row in result:
            writer.writerow(row)
        return result
sorted_minutes = write_sorted_list()
print(sorted_minutes)

