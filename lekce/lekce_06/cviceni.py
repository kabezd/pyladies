from math import sin, pi
from random import randrange, uniform

#x = sin(1)
#print(x)
print(1, end = " ")
print(2,3,4, sep = ", ")
#int("8.9")

# vlastni funkce
# pozicni argumenty - zalezi na pozici ve ktere volame funkci
def obvod_obdelniku(sirka, vyska):
    "Optional documentation- info"
    "More documentation - not working"
    return 2 * (sirka + vyska)

print("Obvod obdelniku:", obvod_obdelniku(4,2))

# funkce, jednoznacne a male, maji delat jen jednu vec

# ne kazda funkce musi mit return
# def ano_nebo_ne -> hodi se na donuceni uzivatele odpovedet ano nebo ne na otazku
# kazda funkce defaultne vraci None i bez Return

def obsah_elipsy(a, b):
    "Vrati obsah elipsy danych rozmeru (delky os)"
    return pi*a*b

print("Obsah elipsy:", obsah_elipsy(10,3), "cm2")

def objem_eliptickeho_valce(a, b, vyska):
    "Vrati objem eliptickeho valce - vyuziva funkce obsah_elipsy"
    return obsah_elipsy(a,b)*vyska

print("Objem eliptickeho valce:", objem_eliptickeho_valce(5,3,10), "cm3")


# defaultni argumenty def funkce(a, b=20): -> b nemusi byt zadane, ale muze byt prepsane
# def funkce(a, b = 20, x = None) -> x je pojmenovany argument
