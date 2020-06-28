from ai import tah_pocitace
from util import tah

def vyhodnot(pole):
    "Vyhodnoti stav hry a urci viteze, remizu ci jestli hra pokracuje"
    if("xxx" in pole):
        return "x"
    elif("ooo" in pole):
        return "o"
    elif("-" not in pole):
        return "!"
    else:
        return "-"

def tah_hrace(pole):
    while(True):
        pozice = input("Na jakou pozici umistit znak? ")
        if(pozice.isdigit() and int(pozice) < 20 ):
            if(pole[int(pozice)] != "-"):
                print("Nelze hrat na obsazene pole!")
            else:
                return tah(pole, int(pozice), "x")
        else:
            print("Je treba zadat kladne cislo v rozmezi 0-19")



def piskvorky1D():
    print("Zacina hra:")
    pole = "--------------------"
    
    while(True):
        print("01234567890123456789")
        print(pole)
        pole = tah_hrace(pole)

        status = vyhodnot(pole)
        if(status != "-"):
            if(status == "!"):
                print("Remiza!")
                break
            elif(status == "x"):
                print("Vyhral hrac s krizky, gratuluji!")
                break

        pole = tah_pocitace(pole)

        print(pole)
        status = vyhodnot(pole)
        if(status != "-"):
            if(status == "!"):
                print("Remiza!")
                break
            elif(status == "o"):
                print("Vyhral pocitac!")
                break