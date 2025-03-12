def main():
    greeting = input().lower().strip()
    dollars = value(greeting)
    print("$" + str(dollars))

def value(greeting):
    try :
        greeting = greeting.lower().strip()
        if greeting.startswith("hello"):
            return 0
        elif greeting.startswith("h"):
            return 20
        else:
            return 100
    except AssertionError:
        exit(1)

if __name__ == "__main__":
    main()