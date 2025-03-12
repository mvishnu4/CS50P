string = input()
output = ""
stop = "..."
for i in range(len(string)):
    if string[i].isspace():
        output += stop
    elif string[i].isalpha:
        output += string[i]
print(output)
