print("What is the Answer to the Great Question of Life, the Universe and Everything? ")
ans = input()

if ans == "forty-two" or ans.lower() == "forty two":
    print("Yes")
elif len(ans) == 2 and ans == "42":
    print("Yes")
else:
    print("No")
