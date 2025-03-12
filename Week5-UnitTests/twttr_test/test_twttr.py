import twttr
from twttr import shorten, main

def main():
    test_twttr()

def omit(pn):
    str = ""
    for i in range(len(pn)):
        if pn[i] not in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", ",", "?", "!", ".", "@"]:
                str += pn[i]
    print(str)
    return str

def test_twttr():
    try:
        assert shorten("Hello") == "Hll"
    except AssertionError:
        exit(1)
    try:
        assert shorten("Twitter") == "Twttr"
    except AssertionError:
        exit(1)
    try:
        assert shorten("Anvil") == "nvl"
    except AssertionError:
        exit(1)
    try:
        assert shorten(omit("1?Av")) == "v"
    except AssertionError:
        exit(1)

if __name__ == "__main__":
    main()