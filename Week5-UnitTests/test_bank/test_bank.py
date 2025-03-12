from bank import value

def test_a():
    assert value("Hello") == 0

def test_b():
    assert value("hellO") == 0

def test_c():
    assert value("how") == 20

def test_d():
    assert value("Here") == 20

def test_f():
    assert value("who") == 100

def test_g():
    assert value("what") == 100

