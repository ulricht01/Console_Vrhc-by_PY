from HerniDeska import *
from Bar import *
from DvojKostka import *
from HerniPole import *
from HerniKamen import *
from Hrac import *
from AiHrac import *
from KonzolovyHrac import *

import random, sys, os, json
rand = random.randint

def main():
    hra = HerniDeska()                  # Vytvoření instance herní desky 
    hra.priprav_hru()                   # Připravení hry                     
    while hra.status == True:                         # Herní cyklus
        hra.vytvor_hraci_plochu()
        if hra.token == 0:              # Podmínka, která kontroluje, kdo je na řadě
            print(f"Na tahu je hráč: {hra.Hrac1.jmeno} ({hra.Hrac1.barva})")
            print('------------------------')
            hra.Hrac1.nabidka()
        elif hra.token == 1:          
            print(f"Na tahu je hráč: {hra.Hrac2.jmeno} ({hra.Hrac2.barva})")
            print('------------------------')
            hra.Hrac2.nabidka()

        input("-----------------------------------------------------STISKNI ENTER---------------------------------------------------------------")  # Zastavení, aby si hráč mohl prohlédnout co se stalo, atd.

if __name__ == "__main__":
    main()