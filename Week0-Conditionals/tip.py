def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # removing special chharacter/ $ from cost
    return float(d[1 : len(d)])

def percent_to_float(p):
    # removing % symbol from given string
    return float(int(p[0 : (len(p) - 1)]) / 100)


main()