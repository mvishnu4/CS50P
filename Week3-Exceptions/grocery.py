list = {}
names = []
keys = []
running = True

while running:
    try:
        item = input()
        if item != "":
            if item not in list:
                list[item.lower()] = 1
                names.append(item.upper())
            else:
                for i in list.keys():
                    if i == item.lower():
                        list[item] += 1
        else:
            names.sort()
            j = 0
            for i in list.keys():
                keys.append(i)
            keys.sort()
            for k in keys:
                print(f"{list[k]} {names[j]}")
                j += 1
            break
    except EOFError:
        names.sort()
        j = 0
        for i in list.keys():
            keys.append(i)
        keys.sort()
        for k in keys:
            print(f"{list[k]} {names[j]}")
            j += 1
        running = False
        break

'''
j = 0
        for i in list.keys():
                fruit = i.upper()
                print(f"{list[i]} {names[j]}")
                j += 1
                '''