from math import ceil

def main():
    while True:
        try:
            fuel = input("Fraction: ").strip()
            fract = convert(fuel)
            print(gauge(fract))
            exit(0)
        except ZeroDivisionError:
            pass
        except ValueError:
            pass
        except IndexError:
            pass
        except EOFError:
            exit(0)
def convert(fraction):
    while i < len(fraction):
        if fraction[i] in ("/"):
            a = d.strip()
            y = fraction[i]
            d = ""
            i += 1
        elif fraction[i].isdigit:
            d += fraction[i]
            if i == len(fraction) - 1:
                b = d.strip()
            i += 1

    if len(a) < 1 or len(b) < 1 or len(y) < 1:
        raise ValueError
    elif (not(int(a)) or a == "0") and (not(int(b)) or b == "0"):
        raise ValueError
    else:
        x = int(a)
        y = "/"
        z = int(b)

        if x <= z:
           return int((x/z)*100)
        if z == 0:
            raise ZeroDivisionError
        elif x > z:
            raise ValueError

    if x == 0:
        return 0


def gauge(percentage):
    if ceil(percentage) >= 99:
        return "F"
    elif ceil(percentage) <= 1:
        return "E"
    else:
        return f"{ceil(percentage)}%"


if __name__ == "__main__":
    main()

