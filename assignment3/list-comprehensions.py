#task 3
import csv

with open("../csv/employees.csv", newline="") as file:
    reader = csv.reader(file)
    data = list(reader)

rows = data[1:]

names = [row[1] + " " + row[2] for row in rows]

names_e = [name for name in names if "e" in name]

print(names)
print(names_e)