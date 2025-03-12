def main():
    print(parse(input("HTML: ")))


def parse(s):
    st = 0
    url = ""
    if s[0] == "<" and s[len(s)-1] == ">":
        for i in range(len(s)):
            if s[i:i+18] == "youtube.com/embed/":
                st = i+18
                break
    if st != 0:
        while True:
            url += s[st]
            st += 1
            if s[st+1] == ">" or s[st+1] == " ":
                break
        return "https://youtu.be/" + url


if __name__ == "__main__":
    main()