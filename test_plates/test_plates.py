from plates import is_valid

def test_len():
    assert is_valid("PUDA") == True
    assert is_valid("AmritaPu") == False
    assert is_valid("Amrita") == True

def test_zero():
    assert is_valid("CS50") == True
    assert is_valid("CS05") == False

def test_firstnum():
    assert is_valid("986735") == False
    assert is_valid("2mrita") == False

def test_punctuation():
    assert is_valid("Am.Ri") == False
def test_num():
    assert is_valid("0135689") == False
    assert is_valid("54321") == False

def test_alpnum():
    assert is_valid("8Amri") == False
    assert is_valid("Am20i") == False
    assert is_valid("Amit8") == True
    assert is_valid("Amit80") == True

def test_alphabet():
    assert is_valid("David") == True
    assert is_valid("DavidMalan") == False
