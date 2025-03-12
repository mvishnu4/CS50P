from plates import is_valid

def test_Zeroes():
    assert is_valid("CS50") == True
    assert is_valid("CS02") == False

def test_len():
    assert is_valid("A") == False
    assert is_valid("Assess1") == False

def test_minAlphabetsatBeggning():
    assert is_valid("1") == False
    assert is_valid("A5") == False
    assert is_valid("AA") == True
    assert is_valid("1w") == False
    assert is_valid("w1w") == False
    assert is_valid("12") == False

def test_specialchar():
    assert is_valid("Aa2,") == False

def numplacement():
    assert is_valid("AAA1") == True
    assert is_valid("AA1A") == False
    assert is_valid("AA1A1") == False
    assert is_valid("AA0A1") == False
    assert is_valid("AAA10") == True
