import csv #comma seperated value
import os

def write_csv(filename):
    data = [
        {"name":"Akshay","age":22,},
        {"name":"John snow","age":28}
    ]
    columnnames = ["name","age"]
    with open(filename, "w", newline="\n") as file:
        writer = csv.DictWriter(file, fieldnames=columnnames)
        writer.writeheader()
        writer.writerows(data)

def read_csv(filename):
    with open()

filename = 'myfile.csv'
# write_csv(filename)
