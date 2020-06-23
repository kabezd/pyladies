# kontrola RC pomoci jednotlivych funkci
def kontrola_formatu(rc):
    if(rc[0:6].isdigit() and rc[6] == "/" and rc[7:].isdigit()):
        return True
    else:
        return False

def kontrola_delitelnosti(rc):
    bez_lomitka = rc.replace("/", "")
    soucet_lich = 0
    soucet_sude = 0

    for i in range(len(bez_lomitka)):
        # sude
        if(i % 2 == 0):
            soucet_sude += int(bez_lomitka[i])
        else:
            soucet_lich += int(bez_lomitka[i])

    if((soucet_sude-soucet_lich)%11 ==0):
        return True
    else:
        return False

def zjisti_datum_narozeni(rc):
    rok = "19" + rc[0:2]
    if(int(rc[2:4]) > 12):
        mesic = str(int(rc[2:4]) - 50)
    else:
        mesic = rc[2:4]
    den = rc[4:6]

    return(den, mesic, rok)

def zjisti_pohlavi(rc):
    if(int(cislo[2:4]) > 12):
        return "zena"
    else:
        return "muz"

cislo = input("Zadejte prosim rodne cislo: ")

if(kontrola_formatu(cislo)):
    print("Format RC je spravny")

    if(kontrola_delitelnosti(cislo)):
        print("RC je delitelne 11")

        datum = zjisti_datum_narozeni(cislo)
        print(datum)

        pohlavi = zjisti_pohlavi(cislo)
        print(pohlavi)

    else:
        print("RC neni delitelne 11")
else:
    print("RC je zadano ve spatnem formatu")

        # print()
        # print("Dalsi informace na zaklade RC:")
        # print("Datum narozeni: {}.{}.{}".format(den,mesic,rok))
        # print("Pohlavi: {}".format(pohlavi))
        




