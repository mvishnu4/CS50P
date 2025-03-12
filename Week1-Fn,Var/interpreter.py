#asking user for Expression
print("Expression: ", end = "")

expression = input()

x = 0
y = ""
z = 0

x, y, z = expression.split(" ")
if y == "+":
    print(float(x) + float(z))
elif y == "-":
    print(float(x) - float(z))
elif y == "*":
    print(float(x) * float(z))
elif y == "/":
    print(float(x) / float(z))
elif y == "^":
    print(float(x) ** float(z))
else:
    print("Invalid math expression")