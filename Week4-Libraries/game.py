import random

ran = 0
level = 0
levelNum = True
while (levelNum):
    try:
        level = int(input("Level: "))
        if int(level):
            levelNum = False
            raise Exception
    except:
        if levelNum == False:
            break
ran = random.randint(1, 10)

guess = True
while guess:
    try:
        ans = int(input("Guess: "))
        if ans == ran:
            print("Just right!")
            guess = False
        elif ans > ran:
            print("Too large!")
        elif ans < ran:
            print("Too small!")
    except:
        if guess:
            pass
        else:
            break


