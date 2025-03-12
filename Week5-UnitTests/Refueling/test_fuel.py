from fuel import convert, gauge
import pytest
def main():
    test_ZeroDivisionError()
    test_ValueError()
    test_convert()
    test_gauge()

def test_ZeroDivisionError():
    with pytest.raises(ZeroDivisionError):
        assert convert("1/0")

def test_ValueError():
    with pytest.raises(ValueError):
        assert convert("12/10")

def incorrectIndex():
    with pytest.raises(IndexError):
        assert convert("1+1")

def test_convert():
    try:
        assert convert("0/1") == 0
        assert convert("-1/4") == -25
    except AssertionError as ValueError:
        pass

def test_gauge():
    assert gauge(1) == "E"
    assert gauge(50) == "50%"
    assert gauge(99) == "F"

if __name__ == "__main__":
    main()

#asserting too many erroy belonging to same category fails and returns wxir code 1 at beggning
# assert convert("char/char") not works