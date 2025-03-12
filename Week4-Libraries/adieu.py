import inflect

p = inflect.engine()
names = []
sep = ["and"]
start = "Adieu, adieu, to "
run = True
while True:
    try:
        name = input("Name: ")
        if name == "":
            raise Exception
        elif len(names) == 0:
            start += name
            names.append(name)
        elif len(names) == 1:
            start += (" and " + name)
            names.append(name)
        elif len(names) == 2:
            names.append(name)
            for i in range(len(start)):
                if start[i:i+5] == " and ":
                    a = start[0:i]
                    b = ", "
                    c = start[i+5:len(start)]
                    d = ", and "
                    e = name
                    break
            start = a+b+c+d+e
        else:
            for i in range(len(start)):
                if  start[i:i+6] == ", and ":
                    a = start[0:i]
                    b = ", "
                    c = start[i+6:len(start)]
                    d = ", and "
                    e = name
                    break
            start = a+b+c+d+e
    except:
        print(start)
        break

    '''start = start[0:len(start) - 1]
        for i in range(len(start) - 1, 0, -1):
            if start[i] == ",":
                a = start[0:i]
                b = "and "
                c = start[i+1:len(start)]
                break
        print()
        print(a+b+c)'''