from random import randrange

cislo = randrange(3)

if cislo == 0:
    tah_pocitace = 'kámen'
elif cislo == 1:
    tah_pocitace = 'nůžky'
else:
    tah_pocitace = 'papír'

tah_cloveka = input('kámen, nůžky, nebo papír? ')
print('Tah pocitace: ', tah_pocitace,', tvuj tah: ', tah_cloveka , sep="")

if tah_pocitace == tah_cloveka:
     print('Plichta.')
elif (tah_pocitace == 'kámen' and tah_cloveka == 'papír') \
    or (tah_pocitace == 'papír' and tah_cloveka == 'nůžky' ) \
    or  (tah_pocitace == 'nůžky' and tah_cloveka == 'kámen' ):
     print('Vyhrála jsi!')
elif (tah_cloveka == 'kámen' and tah_pocitace == 'papír' ) \
    or  (tah_cloveka == 'papír' and tah_pocitace == 'nůžky' ) \
    or  (tah_cloveka == 'nůžky' and tah_pocitace == 'kámen' ):
     print('Počítač vyhrál.')
else:
     print('Nerozumím.')