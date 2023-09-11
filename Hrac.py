import random, sys, os, json
rand = random.randint

from HerniDeska import *

class Hrac:                                                         # Třída hráče
    def __init__(self, jmeno, barva, hra):
        self.jmeno = jmeno
        self.barva = barva
        self.hra = hra

    def kontrola_pohybu(self):
        self.valid_moves = 0
        if self.barva == "Bílý":
                for pole in self.hra.herni_pole:
                    if pole.cislo_pole + self.hra.kostka.kostka_1 <= 24 and pole.barva == "B" and self.hra.herni_pole[pole.cislo_pole + self.hra.kostka.kostka_1 - 1].barva != "Č" and self.hra.kostka.kostka_1 != 0 and len(self.hra.herni_pole[pole.cislo_pole + self.hra.kostka.kostka_1 - 1].zasobnik) < 5 or \
                       pole.cislo_pole + self.hra.kostka.kostka_1 <= 24 and pole.barva == "B" and self.hra.herni_pole[pole.cislo_pole + self.hra.kostka.kostka_1 - 1].barva == "Č" and len(self.hra.herni_pole[pole.cislo_pole + self.hra.kostka.kostka_1 - 1].zasobnik) == 1 and self.hra.kostka.kostka_1 != 0:
                        print(f"{pole.cislo_pole}->{pole.cislo_pole + self.hra.kostka.kostka_1}")
                        self.valid_moves += 1
                    if pole.cislo_pole + self.hra.kostka.kostka_2 <= 24 and pole.barva == "B" and self.hra.herni_pole[pole.cislo_pole + self.hra.kostka.kostka_2 - 1].barva != "Č" and self.hra.kostka.kostka_2 != 0 and len(self.hra.herni_pole[pole.cislo_pole + self.hra.kostka.kostka_2 - 1].zasobnik) < 5 or \
                       pole.cislo_pole + self.hra.kostka.kostka_2 <= 24 and pole.barva == "B" and self.hra.herni_pole[pole.cislo_pole + self.hra.kostka.kostka_2 - 1].barva == "Č" and len(self.hra.herni_pole[pole.cislo_pole + self.hra.kostka.kostka_2 - 1].zasobnik) == 1 and self.hra.kostka.kostka_2 != 0:
                        print(f"{pole.cislo_pole}->{pole.cislo_pole + self.hra.kostka.kostka_2}")
                        self.valid_moves += 1
                    if pole.cislo_pole + self.hra.kostka.kostka_3 <= 24 and pole.barva == "B" and self.hra.herni_pole[pole.cislo_pole + self.hra.kostka.kostka_3 - 1].barva != "Č" and self.hra.kostka.kostka_3 != 0 and len(self.hra.herni_pole[pole.cislo_pole + self.hra.kostka.kostka_3 - 1].zasobnik) < 5 or \
                       pole.cislo_pole + self.hra.kostka.kostka_3 <= 24 and pole.barva == "B" and self.hra.herni_pole[pole.cislo_pole + self.hra.kostka.kostka_3 - 1].barva == "Č" and len(self.hra.herni_pole[pole.cislo_pole + self.hra.kostka.kostka_3 - 1].zasobnik) == 1 and self.hra.kostka.kostka_3 != 0:
                        print(f"{pole.cislo_pole}->{pole.cislo_pole + self.hra.kostka.kostka_3}")
                        self.valid_moves += 1
                    if pole.cislo_pole + self.hra.kostka.kostka_4 <= 24 and pole.barva == "B" and self.hra.herni_pole[pole.cislo_pole + self.hra.kostka.kostka_4 - 1].barva != "Č" and self.hra.kostka.kostka_4 != 0 and len(self.hra.herni_pole[pole.cislo_pole + self.hra.kostka.kostka_4 - 1].zasobnik) < 5 or \
                       pole.cislo_pole + self.hra.kostka.kostka_4 <= 24 and pole.barva == "B" and self.hra.herni_pole[pole.cislo_pole + self.hra.kostka.kostka_4 - 1].barva == "Č" and len(self.hra.herni_pole[pole.cislo_pole + self.hra.kostka.kostka_4 - 1].zasobnik) == 1 and self.hra.kostka.kostka_4 != 0:
                        print(f"{pole.cislo_pole}->{pole.cislo_pole + self.hra.kostka.kostka_4}")
                        self.valid_moves += 1
                return self.valid_moves
                       
        if self.barva == "Černý":
                for pole in self.hra.herni_pole:
                    if pole.cislo_pole - self.hra.kostka.kostka_1 >= 1 and pole.barva == "Č" and self.hra.herni_pole[pole.cislo_pole - self.hra.kostka.kostka_1 - 1].barva != "B" and self.hra.kostka.kostka_1 != 0 and len(self.hra.herni_pole[pole.cislo_pole - self.hra.kostka.kostka_1 - 1].zasobnik) < 5 or \
                       pole.cislo_pole - self.hra.kostka.kostka_1 >= 1 and pole.barva == "Č" and self.hra.herni_pole[pole.cislo_pole - self.hra.kostka.kostka_1 - 1].barva == "B" and len(self.hra.herni_pole[pole.cislo_pole - self.hra.kostka.kostka_1 - 1].zasobnik) == 1 and self.hra.kostka.kostka_1 != 0:
                        print(f"{pole.cislo_pole}->{pole.cislo_pole - self.hra.kostka.kostka_1}")
                        self.valid_moves += 1
                    if pole.cislo_pole - self.hra.kostka.kostka_2 >= 1 and pole.barva == "Č" and self.hra.herni_pole[pole.cislo_pole - self.hra.kostka.kostka_2 - 1].barva != "B" and self.hra.kostka.kostka_2 != 0 and len(self.hra.herni_pole[pole.cislo_pole - self.hra.kostka.kostka_2 - 1].zasobnik) < 5 or \
                       pole.cislo_pole - self.hra.kostka.kostka_2 >= 1 and pole.barva == "Č" and self.hra.herni_pole[pole.cislo_pole - self.hra.kostka.kostka_2 - 1].barva == "B" and len(self.hra.herni_pole[pole.cislo_pole - self.hra.kostka.kostka_2 - 1].zasobnik) == 1 and self.hra.kostka.kostka_2 != 0:
                        print(f"{pole.cislo_pole}->{pole.cislo_pole - self.hra.kostka.kostka_2}")
                        self.valid_moves += 1
                    if pole.cislo_pole - self.hra.kostka.kostka_3 >= 1 and pole.barva == "Č" and self.hra.herni_pole[pole.cislo_pole - self.hra.kostka.kostka_3 - 1].barva != "B" and self.hra.kostka.kostka_3 != 0 and len(self.hra.herni_pole[pole.cislo_pole - self.hra.kostka.kostka_3 - 1].zasobnik) < 5 or \
                       pole.cislo_pole - self.hra.kostka.kostka_3 >= 1 and pole.barva == "Č" and self.hra.herni_pole[pole.cislo_pole - self.hra.kostka.kostka_3 - 1].barva == "B" and len(self.hra.herni_pole[pole.cislo_pole - self.hra.kostka.kostka_3 - 1].zasobnik) == 1 and self.hra.kostka.kostka_3 != 0:
                        print(f"{pole.cislo_pole}->{pole.cislo_pole - self.hra.kostka.kostka_3}")
                        self.valid_moves += 1
                    if pole.cislo_pole - self.hra.kostka.kostka_4 >= 1 and pole.barva == "Č" and self.hra.herni_pole[pole.cislo_pole - self.hra.kostka.kostka_4 - 1].barva != "B" and self.hra.kostka.kostka_4 != 0 and len(self.hra.herni_pole[pole.cislo_pole - self.hra.kostka.kostka_4 - 1].zasobnik) < 5 or \
                       pole.cislo_pole - self.hra.kostka.kostka_4 >= 1 and pole.barva == "Č" and self.hra.herni_pole[pole.cislo_pole - self.hra.kostka.kostka_4 - 1].barva == "B" and len(self.hra.herni_pole[pole.cislo_pole - self.hra.kostka.kostka_4 - 1].zasobnik) == 1 and self.hra.kostka.kostka_4 != 0:
                        print(f"{pole.cislo_pole}->{pole.cislo_pole - self.hra.kostka.kostka_4}")
                        self.valid_moves += 1
                return self.valid_moves
        
    def prerus_tah(self):                                           # Metoda pro přerušení kola
        if self.hra.token == 0:
            self.kontrola_pohybu()
            if self.valid_moves == 0 and self.hra.hozeno == 1 or self.valid_moves > 0 and self.hra.kostka.kostka_1 == 0 and self.hra.kostka.kostka_2 == 0 and self.hra.kostka.kostka_3 == 0 and self.hra.kostka.kostka_4 == 0:
                self.hra.token = 1
                self.hra.kostka.vynuluj()
                self.hra.hozeno = 0
                self.hra.presuny =0
            else:
                print("Stále můžeš táhnout!")
        else:
            self.kontrola_pohybu()
            if self.valid_moves == 0 and self.hra.hozeno == 1 or self.valid_moves > 0 and self.hra.kostka.kostka_1 == 0 and self.hra.kostka.kostka_2 == 0 and self.hra.kostka.kostka_3 == 0 and self.hra.kostka.kostka_4 == 0 and self.hra.hozeno == 1:
                self.hra.token = 0
                self.hra.kostka.vynuluj()
                self.hra.hozeno = 0
                self.hra.presuny =0
            else:
                print("Stále můžeš táhnout!")

    def vypis_konec(self):
        i = 0
        pocet_ve_hre = 0
        jmeno = self.jmeno
        barva = self.barva
        if self.barva == "Bílý":
            pocet_na_baru = len(self.hra.barec.zetony_bila)
            cilove_pole = len(self.hra.cilove_pole_bila)
            for i in range(0, 24):
                for zeton in self.hra.herni_pole[i].zasobnik:
                    if zeton.barva == "Bílý":
                        pocet_ve_hre += 1
                        i+=1
        elif self.barva == "Černý":
            pocet_na_baru = len(self.hra.barec.zetony_cerna)
            cilove_pole = len(self.hra.cilove_pole_cerna)
            for i in range(0, 24):
                for zeton in self.hra.herni_pole[i].zasobnik:
                    if zeton.barva == "Černý":
                        pocet_ve_hre += 1
                        i+=1

        print(f"{barva} hráč {jmeno}| Žetony na baru: {pocet_na_baru} | Žetony v cíli: {cilove_pole} | Žetony ve hře: {pocet_ve_hre}")
