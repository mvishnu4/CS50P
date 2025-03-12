def main():
    print(count(input("Text: ")))


def count(s):
    if s.lower() == "um":
        return 1
    coun = 0
    for i in range(len(s)):
        if s[i:i+2].lower() == "um" and (s[i+2] in [".", " "] or s[i+2:i+4] in [", ", "? "]) and not(s[i-1].isalpha()):
            print(s[i:i+4])
            coun += 1

    return coun

if __name__ == "__main__":
    main()