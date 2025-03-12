menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

cost = 0
run = True
while run:

    try:
        item = input("Item: ")
        found = False
        for i in menu.keys():
            if item.lower() == i.lower():
                cost += menu[i]
                print(f"${cost}" +"0")
                found = True
        if not(found):
            cost = float(cost)
            print(f"${cost}" + "0")
    except EOFError:
        print(f"${cost}" + "0")
        break

'''

try:
    item = input("Item: ")
except EOFError:


for i in menu.keys():
    if item.lower() == i.lower():
        cost += menu[i]
        print("Total: $" + str(cost))
        item = ""
        '''