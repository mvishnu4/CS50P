import sys
from sys import argv
import csv
from csv import DictWriter
columns = []
column = []
keys = []
if len(argv) <= 2 or len(argv) >3:
    sys.exit(1)
else:
    file1 = argv[1].split(".")
    file2 = argv[2].split(".")
    if file1[1] == "csv" and file2[1] == "csv":
        try:
            count = 0
            with open(argv[1]) as f1:
                reader = csv.DictReader(f1)
                for row in reader:
                    if count == 0:
                        for key in row:
                            keys.append(key)
                            count += 1

                    sep = row[keys[0]].split(", ")
                    #row[keys[0]] = sep[0] + " " +sep[1]
                    column.append(sep[0])
                    column.append(sep[1])
                    column.append(row[keys[1]])
                    columns.append(column)
                    column = []
        except FileNotFoundError:
            sys.exit(1)
        with open(argv[2], "w") as f2:
            writter = csv.DictWriter(f2, fieldnames = ["first", "last", "house"])
            #writter.writerow({"first":"first", "last":"last", "house":"house"})
            for column in columns:
                writter.writerow({"first":column[0], "last":column[1], "house":column[2]})

    else:
        print("Not a csv file to read")
        sys.exit(1)