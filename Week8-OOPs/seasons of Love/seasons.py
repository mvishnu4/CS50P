from datetime import date
import inflect
import sys

p = inflect.engine()
days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def sum(pm, pd):
    ds = 0
    for i in range(pm):
        ds += days[i]
    return ds + pd

def calc_day(m, d, tm, td):
    return sum(tm, td) - sum(m, d)

def leap(by, py, bm, pm):
    bm = int(bm)
    pm = int(pm)
    lpyrs = 0
    for i in range(int(by)+1, int(py)-1, 1):
        if i%4 == 0:
            lpyrs += 1
    if bm < 3 and int(by)/4 == 0:
        lpyrs += 1
    if pm > 2 and int(py)/4 == 0:
        lpyrs += 1
    return int(lpyrs)


def main():
    today = date.today()#date.fromisoformat("2001-01-01")
    dob = input("Date of Birth: ")
    try:
        y, m, d = dob.split("-")
    except:
        sys.exit(1)
    print(age(y, m, d, today))

def age(y, m, d, today):
    try:
        a = int(y)
        b = int(m)
        c = int(d)
    except AssertionError:
        sys.exit(1)
    if today.year >= int(y):
        m = int(m)
        d = int(d)
        yrs = 0
        lpyrs = leap(y, today.year, m, today.month)
        daysdiff = 0
        if len(y) == 4 and m <= 12 and d <= days[m-1]:
            yrs = today.year - int(y)
            #mnts = today.month - int(m)
            daysdiff = calc_day(int(m) - 1, int(d), today.month - 1, today.day)
        else:
            sys.exit()
        #print(yrs, daysdiff, lpyrs, sep = " ")
        time = (yrs * 365 * 24 * 60) + (daysdiff * 24 * 60) + (lpyrs * 24 * 60)
        min = p.number_to_words(time, andword="")

        return min[0].upper() + min[1:len(min)] + " minutes"
    else:
        sys.exit(1)

if __name__ == "__main__":
    main()

    