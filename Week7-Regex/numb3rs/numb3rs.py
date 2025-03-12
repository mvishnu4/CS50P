import re
import sys

def main():
    print(validate(input("IPv4 Address: ")))

def validate(iPv4):
    arr = iPv4.split(".")

    if len(arr) == 4:
        for i in range(4):
            #mt = re.search(r"^[0-9]{1,2}?$", arr[i]) or re.search(r"[1]{1}+[0-9]{1,2}?$", arr[i]) or re.search(r"[2]{1}+[0-5]{1,2}?$", arr[i])
            if int(arr[i]) > 255:
               return False

        return True
    else:
        return False

if __name__ == "__main__":
    main()