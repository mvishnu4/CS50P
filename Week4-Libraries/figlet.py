from sys import argv
import sys
from pyfiglet import Figlet

figlet = Figlet()

if len(sys.argv) == 1:
    sent = input("Input: ")
    figlet.getFonts()
    f = "slant"
    figlet.setFont(font=f)
    print("Output: ")
    print(figlet.renderText(sent))
elif len(sys.argv) == 2:
    sys.exit(1)
elif len(sys.argv) == 3:
    if argv[1] == "-f":
        try:
            sent = input("Input: ")
            figlet.getFonts()
            f = figlet.setFont(font=argv[2])
            print("Output: ")
            print(figlet.renderText(sent))
        except:
         exit(1)
    else:
        exit(1)