from random import randrange

pokracovat = "ano"
score = 0
#print("Zacinas s 0 body")

while(pokracovat == "ano"):
    print('Aktualni pocet bodu je: ', score, sep="")
    pokracovat = input('Chcete dale pokracovat? (ano/ne) ')
    if(pokracovat == "ano"):
        karta = randrange(2,10)
        print("Byla otocena karta s hodnotou", karta)
        score = score + karta
    if(score > 21):
        print("Prohravas")
        pokracovat = "ne"
    else:
        print("Neprohravas!")
