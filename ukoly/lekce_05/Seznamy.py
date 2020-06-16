zviratka = ["pes", "kocka", "kralik", "had"]

print("1. kratsi nez 5")
for zvire in zviratka:
    if(len(zvire) < 5):
        print(zvire)

print("2. zacinaji na k")
for zvire in zviratka:
    if(zvire[0] == "k"):
        print(zvire)

print("4. mnoziny dvou seznamu")
list1 = ["pes", "kocka", "kralik"]
list2 = ["pes", "kocka", "had"]
oba = []
jen_prvni = []
jen_druhy = []

for prvni in list1:
    if(prvni in list2):
        oba.append(prvni)
    else:
        jen_prvni.append(prvni)

for druhy in list2:
    if druhy not in list1:
        jen_druhy.append(druhy)

print(list1)
print(list2)
print("V obou:")
print(oba)
print("Jen v prvnim:")
print(jen_prvni)
print("Jen ve druhem:")
print(jen_druhy)

# 6. ukol - razeni podle druheho pismenka ve slove
zviratka = ["pes", "kocka", "kralik", "had", "andulka"]
# jednoduche reseni dle stack overflow :)
#zviratka.sort(key=lambda zviratka:zviratka[1])

# reseni dle postupu

keys = []

for zvire in zviratka:
    keys.append(ord(zvire[1]))

dictionary = dict(zip(keys, zviratka))
#print(dictionary)
#print(sorted(dictionary))

serazena_zviratka = []
for k in sorted(dictionary):
   serazena_zviratka.append(dictionary[k])

print("Zviratka serazena podle druheho pismena:")
print(serazena_zviratka)
# sort_dict = dict(sorted(dictionary.items()))
# print(sort_dict)

# serazena_zviratka = dictionary.values()