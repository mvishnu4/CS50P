fraction = input("Fraction: ")
a = ""
b = ""
y = ""
i = 0
d = ""
while i < len(fraction):
    if fraction[i] in ("/"):
        a = d
        y = fraction[i]
        d = ""
        i += 1
    elif fraction[i].isdigit:
        d += fraction[i]
        if i == len(fraction) - 1:
            b = d
        i += 1

bool = True

def ceil(num):
    if num - int(num) < 0.5:
        return int(num)
    else:
        return int(num) + 1

while bool:
    try:
        x = int(a)
        y = "/"
        z = int(b)

        if x <= z:
            percentage = (x / z) * 100
            if percentage >= 99:
                print("F")
                bool = False
            elif percentage <= 1:
                print("E")
                bool = False
            else:
                print(str(ceil(percentage)) + "%")
                bool = False
        else:
            continue
    except (ValueError, ZeroDivisionError):
        fraction = input("Fraction: ")
        i = 0
        d = ""
        while i < len(fraction):
            if fraction[i] in ("/"):
                a = d
                y = fraction[i]
                d = ""
                i += 1
            elif fraction[i].isdigit:
                d += fraction[i]
                if i == len(fraction) - 1:
                    b = d
                i += 1

