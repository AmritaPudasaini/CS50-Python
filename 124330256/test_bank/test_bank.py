from bank import value

def test_1():
    assert value("hello") == 0
    assert value("HELLO") == 0
    assert value("HeLLo") == 0

def test_2():
    assert value("hi David") == 20
    assert value("HI David") == 20
    assert value("how are you David?") == 20
    assert value("HOW are you David?") == 20

def test_3():
    assert value("byee") == 100
    assert value("BYEE") == 100
    assert value("good david") == 100
    assert value("GOOD david") == 100
