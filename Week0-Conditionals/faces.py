# taking input from user
string = input()
output = ""
#loopin through input and replacig emoticons with coresponding emojis if emoticons are found
for i in range(len(string)):
    if string[i] == ":" and string[i+1] == ")":
        output += "🙂"
    elif string[i] == ":" and string[i+1] == "(":
        output += "🙁"
    elif string[i] == "(" or string[i] == ")" :
        output += ""
    else:
        output += string[i]

print(output)
