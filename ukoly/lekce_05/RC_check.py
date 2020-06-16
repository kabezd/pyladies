cislo = input("Zadejte prosim rodne cislo: ")

#cislo = "199988/5430"
#cislo = "736028/5163"

# kontrola formatu
if(cislo[0:6].isdigit() and cislo[6] == "/" and cislo[7:].isdigit()):
    print("- format RC je spravny")

    # kontrola delitelnosti 11 (soucet na sudych pozicich - soucet na lichych pozicich % 11 = 0)
    bez_lomitka = cislo.replace("/", "")
    soucet_lich = 0
    soucet_sude = 0

    for i in range(len(bez_lomitka)):
        # sude
        if(i % 2 == 0):
            soucet_sude += int(bez_lomitka[i])
        else:
            soucet_lich += int(bez_lomitka[i])
    #print(soucet_sude)
    #print(soucet_lich)
    if((soucet_sude-soucet_lich)%11 ==0):
        print("- RC je delitelne 11")

        # datum narozeni + pohlavi
        rok = "19" + cislo[0:2]
        if(int(cislo[2:4]) > 12):
            pohlavi = "zena"
            mesic = str(int(cislo[2:4]) - 50)
        else:
            pohlavi = "muz"
            mesic = cislo[2:4]

        den = cislo[4:6]
        print()
        print("Dalsi informace na zaklade RC:")
        print("Datum narozeni: {}.{}.{}".format(den,mesic,rok))
        print("Pohlavi: {}".format(pohlavi))
        

    else:
        print("- RC neni delitelne 11")

else:
    print("- format RC neni spravny")




