def main():
    sent = input("Input: ")
    substitute = shorten(sent)
    print(substitute)

def shorten(word):
    sub = ""
    for i in range(len(word)):
        if word[i] not in ["a", "A", "e", "E", "I", "i", "o", "O", "U", "u"]:#, "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", ",", "?", "!", ".", "@"]:
            sub += word[i]
        elif word[i] in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", ",", "?", "!", ".", "@"]:
            sub += word[i]
    print(sub)
    return sub

if __name__ == "__main__":
    main()