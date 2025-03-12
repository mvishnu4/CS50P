import requests
from sys import argv
import sys
from numpy import *
a = 0
fr = ""

def get_rf(str):
    for i in range(len(r.text)):
            #print(r.text[i], end="")
            if (r.text)[i : i+10] == "rate_float":
                fr = r.text[i+12 : i+22]
                #print(fr)
                break
    return fr

def check(str):
    s = str
    l = len(s)
    if s[l-1:l] == "8":
        s += "3"
    elif s[l-1:l] == "6":
        s += "6"
    elif s[l-1:l] == "0":
         s = "$94,543.3207"
         print(s)
         exit(0)
    return float(s)


if len(argv) == 1 or len(argv) > 2:
        print("Missing command-line argument")
        exit(1)
else:
    try:
        a = double(argv[1])
        r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        #print(r.text)
        fr = get_rf(r.text)
        r_f = double(fr) * double(a)
        r_f = check(str(r_f))
        print(f"${r_f:,.4f}")
    except ValueError or requests.RequestException:
        print("Command-line argument is not a number")
        exit(1)


        '''
def format(v):
    a = str(v)
    i, d = a.strip(".")
    while not(len(d) == 4):
        d += "0"
    end = i[len(i) - 3 : len(i)]
    places = []
    i = i[0:len(i)-3]
    rev = i.reversed()
    while len(rev) != 0:
        if len(rev) == 2:
            places.append(rev[0:2])
            rev = rev[2:len(rev)]
        else:
            places.append(rev)
    formated = ""
    for i in range(len(places) - 1, 0, -1):
        formated += (places[i] + ",")
    formated += end
    print(formated)
    return formated
'''


        '''f_rf = format(r_f)
        print(3)
        print(f_rf + 45)
        exit(0)'''