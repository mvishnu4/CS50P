from sys import argv
import sys
from tabulate import tabulate
import csv

columns = []
if len(argv) == 1:
    print("Too few command-line arguments")
    sys.exit(1)
elif len(argv) > 2:
    print("Too many command-line arguments")
    sys.exit(1)
else:
    file = argv[1]
    a = file.split(".")
    if len(a) == 2 and a[1] == "csv":
        try:
            with open(file) as f:
                reader = csv.DictReader(f)
                count = 0
                key = []
                for row in reader:
                    column = []
                    if count == 0:
                        for keys in row:
                            column.append(keys)
                            count +=1
                        key = column
                        column = []

                    column.append(row[key[0]])
                    column.append(row[key[1]])
                    column.append(row[key[2]])
                    columns.append(column)

            #print(columns)
            print(tabulate(columns, key, tablefmt="grid"))
        except FileNotFoundError:
            print("File does not exist")
            sys.exit(1)
    else:
        print("Not a CSV file")
        sys.exit(1)
