from um import count

def test_um():
    assert count("um")==1
    assert count('um, amrita')==1
    assert count('Um, amit good boy um, aluminium')==2
