def main():
    print("What time is it? ", end = "")
    time = convert(input())
    if (time >= 7 and time <= 8):
        print("breakfast time")
    elif (time >= 12 and time <= 13):
        print("lunch time")
    elif (time >= 18 and time <= 19):
        print("dinner time")

def convert(time):
    sym = 0
    for i in range(len(time)):
        if time[i] == ":":
            sym = i
            break
    if "pm" in time:
        x = float(time[0:sym] + 12)
        y = float(time[sym+1:sym+3])/60
    else:
        x = float(time[0:sym])
        y = float(time[sym+1:sym+3])/60
    return (float(x + y))


if __name__ == "__main__":
    main()