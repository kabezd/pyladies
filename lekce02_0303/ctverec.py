#a = 356

a = float(input("Zadejte delku strany/polomeru: "))
if(a <= 0):
        print("Zadana hodnota musi byt kladna")
else:
    obvod_ctverce = 4*a
    obsah_ctverce= a**2
    obsah_kruhu = 3.14*a**2
    obvod_kruhu = 2*3.14*a

    print("Obvod ctverce se stranou ", a ," cm je " , obvod_ctverce , " cm")
    print("Obsah ctverce se stranou " , a , " cm je " , obsah_ctverce , " cm2")
    print("Obvod kruhu se stranou " , a , " cm je " , obvod_kruhu , " cm")
    print("Obsah kruhu se stranou " , a , " cm je " , obsah_kruhu , " cm2")



