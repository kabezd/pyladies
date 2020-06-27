from random import randrange


pocet_hracu = 4
vysledky = {} # prazdny slovnik, key = cislo hrace, value = pocet hodu


print("Zacina hra s", pocet_hracu, "hraci")

for i in range(1, pocet_hracu +1):
    print("Je na rade hrac cislo: ", i)
    pocet_hodu = 0
    while(True):
        hod = randrange(1,7)
        pocet_hodu += 1
        print("Hod cislo: ", pocet_hodu, "Padla hodnota: ", hod)
        if(hod ==6):
            vysledky[i] = pocet_hodu
            break

# seradit dle poctu hodu
serazene = sorted(vysledky.items(), key=lambda x: x[1], reverse=True)

# kontrola
print("serazene:", serazene)
print(" Vyhercem je hrac cislo: ", next(iter(serazene)))
print(" Vyhercem je hrac cislo: ", list(serazene)[0][0])