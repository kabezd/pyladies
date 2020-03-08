print('Klasifikuji dle BMI:')
vyska = int(input('Kolik měříš? (v cm) '))
vaha = int(input('Kolik vážíš? (v kg) '))

if (vyska < 0) or (vaha < 0):
    print('Vážně?')
else:
    bmi = int(vaha / ((vyska/100)**2))
    if (bmi < 18.5):
        klasifikace = 'podváha, měla bys více jíst!'
    elif (bmi < 25):
        klasifikace = 'optimální váha, gratuluji!'
    elif (bmi < 35):
        klasifikace = 'obezita prvního stupně, pár dřepů by neuškodilo ;)'
    elif (bmi < 40):
        klasifikace = 'obezita druhého stupně, vážně by to chtělo omezit ty brambůrky!'
    elif (bmi >= 40):
        klasifikace = 'obezita třetího stupně, to už není žádná sranda, fakt!'

print('Tvé BMI je: ' , bmi, '. To je ', klasifikace, sep = '')