from random import randrange


# ukol 9
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

# ukol 10
def tah(pole, cislo_policka, symbol):
    return pole[:cislo_policka] + symbol + pole[cislo_policka + 1:]

# ukol 11
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

#print("test tahu:",tah_hrace("------------------"))

# ukol 12
def tah_pocitace(pole):
    while(True):
        pozice = randrange(0,20)
        if(pole[pozice] == "-"):
            return tah(pole, pozice, "o")


# ukol 13
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


piskvorky1D()