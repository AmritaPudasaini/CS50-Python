from numb3rs import validate

def test_validate():
    assert validate("127.123.4.5")==True
    assert validate("127.123.4.545")==False
