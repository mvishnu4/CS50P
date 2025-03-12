from sys import argv
import sys

if len(argv) == 1:
    print("Too few command-line arguments")
    sys.exit(1)
elif len(argv) > 2:
    print("Too many command-line arguments")
    sys.exit(1)
else:
    file = argv[1]
    a = file.split(".")
    if len(a) == 2 and a[1] == "py":
        try:
            with open(file) as f:
                loc = 0
                for line in f:
                    line = line.lstrip()
                    if line.startswith("#"):
                        loc += 0 #lines of code excluding comments and white lines
                    elif line == "":
                        loc += 0
                    else:
                        loc += 1
                print(loc)
        except FileNotFoundError:
            print("File does not exist")
            sys.exit(1)
    else:
        print("Not a Python file")
        sys.exit(1)
