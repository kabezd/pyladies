import piskvorky

def test_zadani_na_spravnou_pozici():
    pole = piskvorky.tah('--------------------', 5, "x" )
    assert len(pole) == 20
    assert pole[5] == "x"
    assert pole.count('-') == 19

def test_tah_na_prazdne_pole():
    pole = piskvorky.tah_pocitace('--------------------')
    assert len(pole) == 20
    assert pole.count('o') == 1
    assert pole.count('-') == 19