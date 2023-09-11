import random, sys, os, json
rand = random.randint

from HerniDeska import *
from HerniPole import *
from HerniKamen import *



class Bar:                                                          # Třída baru
    def __init__(self, hra, zetony_bila = [], zetony_cerna = []):
        self.zetony_bila = []                                       # Seznam bílých žetonů na baru
        self.zetony_cerna = []                                      # Seznam černých žetonů na baru
        self.pocet_zetonu_bila = len(zetony_bila)                   # Počet bílých žetonů na baru
        self.pocet_zetonu_cerna = len(zetony_cerna)                 # Počet černých žetonů na baru
        self.hra = hra

    def vyjeti_z_baru(self, x, barva):                    # Vytovření bílého kamenu na cílový zásobník v případě nahazování z baru
        kostka = 0
        kamen = x
        print(f" Kostka 1: {self.hra.kostka.kostka_1} \n Kostka 2: {self.hra.kostka.kostka_2} \n Kostka 3: {self.hra.kostka.kostka_3} \n Kostka 4: {self.hra.kostka.kostka_4}")
        inp = int(input("Zadej kterou kostkou chceš vyjet: "))
        if inp == 1:
            kostka = self.hra.kostka.kostka_1
            if barva == "Bílý":
                cil = self.hra.herni_pole[kostka-1]
                if cil.barva == "B" or len(cil.zasobnik) == 0:
                    cil.zasobnik.append(kamen)
                    self.hra.kostka.kostka_1 = 0
                else:
                    print("Pole je obsazené!")
            elif barva == "Černý":
                cil = self.hra.herni_pole[23 - kostka -1]
                if cil.barva == "Č" or len(cil.zasobnik) == 0:
                    cil.zasobnik.append(kamen)
                    self.hra.kostka.kostka_1 = 0
                else:
                    print("Pole je obsazené!")
        elif inp == 2:
            kostka = self.hra.kostka.kostka_2
            if barva == "Bílý":
                cil = self.hra.herni_pole[kostka-1]
                if cil.barva == "B" or len(cil.zasobnik) == 0:
                    cil.zasobnik.append(kamen)
                    self.hra.kostka.kostka_2 = 0
                else:
                    print("Pole je obsazené!")
            elif barva == "Černý":
                cil = self.hra.herni_pole[23 - kostka -1]
                if cil.barva == "Č" or len(cil.zasobnik) == 0:
                    cil.zasobnik.append(kamen)
                    self.hra.kostka.kostka_2 = 0
                else:
                    print("Pole je obsazené!")
        elif inp == 3:
            kostka = self.hra.kostka.kostka_3
            if barva == "Bílý":
                cil = self.hra.herni_pole[kostka-1]
                if cil.barva == "B" or len(cil.zasobnik) == 0:
                    cil.zasobnik.append(kamen)
                    self.hra.kostka.kostka_3 = 0
                else:
                    print("Pole je obsazené!")
            elif barva == "Černý":
                cil = self.hra.herni_pole[23 - kostka -1]
                if cil.barva == "Č" or len(cil.zasobnik) == 0:
                    cil.zasobnik.append(kamen)
                    self.hra.kostka.kostka_3 = 0
                else:
                    print("Pole je obsazené!")
        elif inp == 4:
            kostka = self.hra.kostka.kostka_4
            if barva == "Bílý":
                cil = self.hra.herni_pole[kostka-1]
                if cil.barva == "B" or len(cil.zasobnik) == 0:
                    cil.zasobnik.append(kamen)
                    self.hra.kostka.kostka_4 = 0
                else:
                    print("Pole je obsazené!")
            elif barva == "Černý":
                cil = self.hra.herni_pole[23 - kostka -1].zasobnik
                if cil.barva == "Č" or len(cil.zasobnik) == 0:
                    cil.zasobnik.append(kamen)
                    self.hra.kostka.kostka_4 = 0
                else:
                    print("Pole je obsazené!")
    
    def vyjeti_z_baru_ai(self, x, barva):                    # Vytovření bílého kamenu na cílový zásobník v případě nahazování z baru
        kostka = 0
        kamen = x
        if self.hra.kostka.double == 2:
            inp = rand(1,4)
        else:
            inp = rand(1,2)
        if inp == 1:
            kostka = self.hra.kostka.kostka_1
            if barva == "Bílý":
                cil = self.hra.herni_pole[kostka-1]
                if cil.barva == "B" or len(cil.zasobnik) == 0:
                    cil.zasobnik.append(kamen)
                    self.hra.kostka.kostka_1 = 0
                else:
                    print("Pole je obsazené!")
            elif barva == "Černý":
                cil = self.hra.herni_pole[23 - kostka -1]
                if cil.barva == "Č" or len(cil.zasobnik) == 0:
                    cil.zasobnik.append(kamen)
                    self.hra.kostka.kostka_1 = 0
                else:
                    print("Pole je obsazené!")
        elif inp == 2:
            kostka = self.hra.kostka.kostka_2
            if barva == "Bílý":
                cil = self.hra.herni_pole[kostka-1]
                if cil.barva == "B" or len(cil.zasobnik) == 0:
                    cil.zasobnik.append(kamen)
                    self.hra.kostka.kostka_2 = 0
                else:
                    print("Pole je obsazené!")
            elif barva == "Černý":
                cil = self.hra.herni_pole[23 - kostka -1]
                if cil.barva == "Č" or len(cil.zasobnik) == 0:
                    cil.zasobnik.append(kamen)
                    self.hra.kostka.kostka_2 = 0
                else:
                    print("Pole je obsazené!")
        elif inp == 3:
            kostka = self.hra.kostka.kostka_3
            if barva == "Bílý":
                cil = self.hra.herni_pole[kostka-1]
                if cil.barva == "B" or len(cil.zasobnik) == 0:
                    cil.zasobnik.append(kamen)
                    self.hra.kostka.kostka_3 = 0
                else:
                    print("Pole je obsazené!")
            elif barva == "Černý":
                cil = self.hra.herni_pole[23 - kostka -1]
                if cil.barva == "Č" or len(cil.zasobnik) == 0:
                    cil.zasobnik.append(kamen)
                    self.hra.kostka.kostka_3 = 0
                else:
                    print("Pole je obsazené!")
        elif inp == 4:
            kostka = self.hra.kostka.kostka_4
            if barva == "Bílý":
                cil = self.hra.herni_pole[kostka-1]
                if cil.barva == "B" or len(cil.zasobnik) == 0:
                    cil.zasobnik.append(kamen)
                    self.hra.kostka.kostka_4 = 0
                else:
                    print("Pole je obsazené!")
            elif barva == "Černý":
                cil = self.hra.herni_pole[23 - kostka -1].zasobnik
                if cil.barva == "Č" or len(cil.zasobnik) == 0:
                    cil.zasobnik.append(kamen)
                    self.hra.kostka.kostka_4 = 0
                else:
                    print("Pole je obsazené!")

    def vytvor_start_bily(self, x, barva = "Bílý"):                 # Vytvoření startovních bílých žetonů
        kamen = HerniKamen(barva)
        cil = self.hra.herni_pole[x].zasobnik
        cil.append(kamen)

    def vytvor_start_cerny(self, x, barva = "Černý"):               # Vytvoření startovních černých žetonů
        kamen = HerniKamen(barva)
        cil = self.hra.herni_pole[x].zasobnik
        cil.append(kamen)

    def pridej_do_baru(self, cil):                         # Přidání žetonu na bar
        temp = []
        pole_cil = self.hra.herni_pole[cil]
        temp.append(pole_cil.zasobnik[0])
        self.hra.herni_pole[cil].zasobnik.pop(-1)
        if temp[0].barva == "Bílý":
            self.zetony_bila.append(temp)
            print("Do baru byl přidán bílý žeton!")
        elif temp[0].barva == "Černý":
            self.zetony_cerna.append(temp)
            print("Do baru byl přidán černý žeton!")


    
