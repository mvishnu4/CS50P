
months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
date = input("Date: ")
m = ""
d = ""
y = ""
a = ""
b = ""
count = 0
tmp = ""
for i in range(len(date)):
    if date[i] in ("/", " ", ",") and i != 0:
        if count == 0:
            a = date[i]
            m = tmp; tmp = ""
        elif count == 1:
            b = date[i]
            d = tmp; tmp = ""
        #elif count >= 2
        count += 1
    elif date[i].isalnum():
        tmp += date[i]
    if i == len(date) - 1:
        y = tmp; tmp = ""


def index(mn, monthsarr):
    for i in range(len(monthsarr)):
        if monthsarr[i] == mn:
            return str(i + 1)

running = True
while running:

    try:

        Y = (y.isdigit() and len(y) == 4)
        M = (m.isdigit() and int(m) <= 12 and int(m) > 0) or (m in months)
        D = (d.isdigit() and int(d) <= 31)
        #print(f"{y}{Y}{m}{M}{d}{D}")
        if D and Y and M:
                if len(m) == 1:
                    m = "0" + m
                elif len(m) == 2:
                    m = m
                elif m in months and count == 3:
                    m = index(m , months)
                    if len(m) == 1:
                        m = "0" + m
                else:
                    raise Exception

                if len(d) == 1:
                    d = "0" + d
                #print(2)
                print(y + "-" + m + "-" + d)
                running = False
                break
        else:
            #print(1)
            raise Exception
    except:
        if running:
            date = input("Date: ")
            m = ""
            d = ""
            y = ""
            count = 0
            tmp = ""
            for i in range(len(date)):
                if date[i] in ("/", " ", ",") and i != 0:
                    if count == 0:
                        m = tmp; tmp = ""
                    elif count == 1:
                        d = tmp; tmp = ""
                        #elif count >= 2
                    count += 1
                elif date[i].isalnum():
                    tmp += date[i]
                if i == len(date) - 1:
                    y = tmp; tmp = ""
        else:
            break