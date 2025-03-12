import random

def main():
    level = get_level()
    score = generate_integer(level)
    print(f"Score: {score}")

def get_level():
    level = 0
    lev = True
    while(lev):
        try:
            level = int(input("Level: "))
            if level == 1 or level == 2 or level == 3:
                lev = False
                raise Exception
        except:
            if lev == False:
                break
    return level

def generate_integer(level):
    a = [0, 10, 100]
    b = [9, 99, 999]
    x = 0
    y = 0
    i = 0
    count = 0
    score = 0
    while i < 10:
        if count == 0:
            x = random.randint(a[level - 1], b[level - 1])
            y = random.randint(a[level - 1], b[level - 1])
        print(f"{x} + {y} =" , end = " ")
        try:
            ans = int(input())
            if ans != (x + y):
                print("EEE")
                count += 1
                raise Exception
            else:
                i += 1
                score += 1
                if count != 0:
                    count = 0
                raise Exception
        except:
            if count == 3:
                print(f"{x} + {y} = {x + y}")
                count = 0
                i += 1

    return score

if __name__ == "__main__":
    main()