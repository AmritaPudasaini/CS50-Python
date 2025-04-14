from twttr import shorten

def test_shorten():
    assert shorten("Amit")=="mt"
    assert shorten("Amrita")=="mrt"

def test_shorten_upper():
    assert shorten("AMRITA")=="MRT"
    assert shorten("AMIT")=="MT"

def test_shorten_lower():
    assert shorten("python")=="pythn"
    assert shorten("program")=="prgrm"

def test_shorten_punctuation():
    assert shorten("intro@duction")=="ntr@dctn"
    assert shorten("progra@#mm!ng")=="prgr@#mm!ng"

def test_shorten_number():
    assert shorten("eb15ost5")=="b15st5"


