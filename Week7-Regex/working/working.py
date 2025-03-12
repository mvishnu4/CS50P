def main():
    print(convert(input("Hours: ")))

def convert(s):
    start = ""
    end = ""
    format = s.split(" ")
    if len(format) == 5:
        if format[2] == "to":
            if len(format[0]) == 5 or len(format[0]) == 4:
                h, m = format[0].split(":")
                if int(h) <= 12 and int(m) < 60:
                    if format[1] == "AM":
                        if len(h) == 1:
                            h = "0" + h
                        if int(h) == 12:
                            h = "00"
                        start += (h+":"+m)
                    elif format[1] == "PM":
                        h = int(h)
                        h += 12
                        if h == 24:
                            h -= 12
                        elif h < 10:
                            h = str(h)
                            h = "0" + h
                        start += (str(h)+":"+m)
                else:
                    raise ValueError
            elif len(format[0]) <= 2:
                h = format[0]
                if int(h) <= 12:
                    if format[1] == "AM":
                        if len(h) == 1:
                            h = "0" + h
                        if int(h) == 12:
                            h = "00"
                        start += (str(h)+":"+"00")
                    elif format[1] == "PM":
                        h = int(h)
                        h += 12
                        if h == 24:
                            h -= 12
                        elif h < 10:
                            h = str(h)
                            h = "0" + h
                        start += (str(h)+":"+"00")
                else:
                    raise ValueError
            #print(start)

            if len(format[3]) == 5 or len(format[3]) == 4:
                h, m = format[3].split(":")
                if int(h) <= 12 and int(m) < 60:
                    if format[4] == "AM":
                        if len(h) == 1:
                            h = "0" + h
                        if int(h) == 12:
                            h = "00"
                        end += (str(h)+":"+m)
                    elif format[4] == "PM":
                        h = int(h)
                        h += 12
                        if h == 24:
                            h -= 12
                        elif h < 10:
                            h = str(h)
                            h = "0" + h
                        end += (str(h)+":"+m)
                else:
                    raise ValueError
            elif len(format[3]) <= 2:
                h = format[3]
                if int(h) <= 12:
                    if format[4] == "AM":
                        if len(h) == 1:
                            h = "0" + h
                        if int(h) == 12:
                            h = "00"
                        end += (str(h)+":"+"00")
                    elif format[4] == "PM":
                        h = int(h)
                        h += 12
                        if h == 24:
                            h -= 12
                        elif h < 10:
                            h = str(h)
                            h = "0" + h
                        end += (str(h)+":"+"00")
                else:
                    raise ValueError
                #print(end)
            return start + " to " + end
        else:
            raise ValueError
    else:
        raise ValueError


if __name__ == "__main__":
    main()
