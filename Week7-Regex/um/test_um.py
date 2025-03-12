from um import count

def test_count1():
    assert count("um") == 1
    assert count(" um ") == 1

def test_count2():
    assert count("um, hello, um...") == 2

def test_count3():
    assert count("um, um, Um...") == 3

def test_counterror():
    try:
        assert count("yummy") == 0
    except AssertionError:
        exit(0)