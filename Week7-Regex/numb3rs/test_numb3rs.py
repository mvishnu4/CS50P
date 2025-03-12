from numb3rs import  validate

def test_numb():

    assert validate("1.10.100.0") == True
    assert validate("9.99.199.200") == True
    assert validate("256.1.1.1") == False
