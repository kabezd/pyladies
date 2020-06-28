from random import randrange
from util import tah

def tah_pocitace(pole):
    while(True):
        pozice = randrange(0,20)
        if(pole[pozice] == "-"):
            return tah(pole, pozice, "o")