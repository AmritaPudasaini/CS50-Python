from seasons import intoMinute

def test_minute():
    assert intoMinute("2000-01-01") == "Thirteen million, one hundred eighty-seven thousand, five hundred twenty minutes"
    assert intoMinute("1990-05-15") == "Eighteen million, two hundred fifty-three thousand, four hundred forty minutes"
