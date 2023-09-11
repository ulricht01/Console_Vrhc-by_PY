import random, sys, os, json
rand = random.randint
from Hrac import *

class AiHrac(Hrac):
    def __init__(self, jmeno, barva, hra):
        super().__init__(jmeno, barva, hra)
        self.kontrola_bila = 0
        self.kontrola_cerna = 0

    def tah(self, temp=[]):
        start = 0
        start_pol = 0
        pohyby_start = []
        if self.hra.presuny < 2 and self.barva == "Černý" and len(self.hra.barec.zetony_cerna) == 0 and self.hra.hozeno == 1 and self.hra.kostka.double == 0 or self.hra.presuny < 2 and self.barva == "Bílý" and len(self.hra.barec.zetony_bila) == 0 and self.hra.hozeno == 1 and self.hra.kostka.double == 0 or \
           self.hra.presuny <= 2 and self.barva == "Černý" and len(self.hra.barec.zetony_cerna) == 0 and self.hra.hozeno == 1 and self.hra.kostka.double > 0 or self.hra.presuny <= 2 and self.barva == "Bílý" and len(self.hra.barec.zetony_bila) == 0 and self.hra.hozeno == 1 and self.hra.kostka.double > 0:
            print("Tvé možné pohyby jsou: ")
            
            self.kontrola_pohybu()
            if self.barva == "Bílý":
                for pole in self.hra.herni_pole:
                    if pole.cislo_pole + self.hra.kostka.kostka_1 <= 24 and pole.barva == "B" and self.hra.herni_pole[pole.cislo_pole + self.hra.kostka.kostka_1 - 1].barva != "Č" and self.hra.kostka.kostka_1 != 0 and len(self.hra.herni_pole[pole.cislo_pole + self.hra.kostka.kostka_1 - 1].zasobnik) < 5 or \
                       pole.cislo_pole + self.hra.kostka.kostka_1 <= 24 and pole.barva == "B" and self.hra.herni_pole[pole.cislo_pole + self.hra.kostka.kostka_1 - 1].barva == "Č" and len(self.hra.herni_pole[pole.cislo_pole + self.hra.kostka.kostka_1 - 1].zasobnik) == 1 and self.hra.kostka.kostka_1 != 0:
                        start = pole.cislo_pole
                        pohyby_start.append(start)
                    elif pole.cislo_pole + self.hra.kostka.kostka_2 <= 24 and pole.barva == "B" and self.hra.herni_pole[pole.cislo_pole + self.hra.kostka.kostka_2 - 1].barva != "Č" and self.hra.kostka.kostka_2 != 0 and len(self.hra.herni_pole[pole.cislo_pole + self.hra.kostka.kostka_2 - 1].zasobnik) < 5 or \
                       pole.cislo_pole + self.hra.kostka.kostka_2 <= 24 and pole.barva == "B" and self.hra.herni_pole[pole.cislo_pole + self.hra.kostka.kostka_2 - 1].barva == "Č" and len(self.hra.herni_pole[pole.cislo_pole + self.hra.kostka.kostka_2 - 1].zasobnik) == 1 and self.hra.kostka.kostka_2 != 0:
                        start = pole.cislo_pole
                        pohyby_start.append(start)

                    elif pole.cislo_pole + self.hra.kostka.kostka_3 <= 24 and pole.barva == "B" and self.hra.herni_pole[pole.cislo_pole + self.hra.kostka.kostka_3 - 1].barva != "Č" and self.hra.kostka.kostka_3 != 0 and len(self.hra.herni_pole[pole.cislo_pole + self.hra.kostka.kostka_3 - 1].zasobnik) < 5 or \
                       pole.cislo_pole + self.hra.kostka.kostka_3 <= 24 and pole.barva == "B" and self.hra.herni_pole[pole.cislo_pole + self.hra.kostka.kostka_3 - 1].barva == "Č" and len(self.hra.herni_pole[pole.cislo_pole + self.hra.kostka.kostka_3 - 1].zasobnik) == 1 and self.hra.kostka.kostka_3 != 0:
                        start = pole.cislo_pole
                        pohyby_start.append(start)

                    elif pole.cislo_pole + self.hra.kostka.kostka_4 <= 24 and pole.barva == "B" and self.hra.herni_pole[pole.cislo_pole + self.hra.kostka.kostka_4 - 1].barva != "Č" and self.hra.kostka.kostka_4 != 0 and len(self.hra.herni_pole[pole.cislo_pole + self.hra.kostka.kostka_4 - 1].zasobnik) < 5 or \
                       pole.cislo_pole + self.hra.kostka.kostka_4 <= 24 and pole.barva == "B" and self.hra.herni_pole[pole.cislo_pole + self.hra.kostka.kostka_4 - 1].barva == "Č" and len(self.hra.herni_pole[pole.cislo_pole + self.hra.kostka.kostka_4 - 1].zasobnik) == 1 and self.hra.kostka.kostka_4 != 0:
                        start = pole.cislo_pole
                        pohyby_start.append(start)
                        
            elif self.barva == "Černý":
                for pole in self.hra.herni_pole:
                    if pole.cislo_pole - self.hra.kostka.kostka_1 >= 1 and pole.barva == "Č" and self.hra.herni_pole[pole.cislo_pole - self.hra.kostka.kostka_1 - 1].barva != "B" and self.hra.kostka.kostka_1 != 0 and len(self.hra.herni_pole[pole.cislo_pole - self.hra.kostka.kostka_1 - 1].zasobnik) < 5 or \
                       pole.cislo_pole - self.hra.kostka.kostka_1 >= 1 and pole.barva == "Č" and self.hra.herni_pole[pole.cislo_pole - self.hra.kostka.kostka_1 - 1].barva == "B" and len(self.hra.herni_pole[pole.cislo_pole - self.hra.kostka.kostka_1 - 1].zasobnik) == 1 and self.hra.kostka.kostka_1 != 0:
                        start = pole.cislo_pole
                        pohyby_start.append(start)
                    if pole.cislo_pole - self.hra.kostka.kostka_2 >= 1 and pole.barva == "Č" and self.hra.herni_pole[pole.cislo_pole - self.hra.kostka.kostka_2 - 1].barva != "B" and self.hra.kostka.kostka_2 != 0 and len(self.hra.herni_pole[pole.cislo_pole - self.hra.kostka.kostka_2 - 1].zasobnik) < 5 or \
                       pole.cislo_pole - self.hra.kostka.kostka_2 >= 1 and pole.barva == "Č" and self.hra.herni_pole[pole.cislo_pole - self.hra.kostka.kostka_2 - 1].barva == "B" and len(self.hra.herni_pole[pole.cislo_pole - self.hra.kostka.kostka_2 - 1].zasobnik) == 1 and self.hra.kostka.kostka_2 != 0:
                        start = pole.cislo_pole
                        pohyby_start.append(start)
                    if pole.cislo_pole - self.hra.kostka.kostka_3 >= 1 and pole.barva == "Č" and self.hra.herni_pole[pole.cislo_pole - self.hra.kostka.kostka_3 - 1].barva != "B" and self.hra.kostka.kostka_3 != 0 and len(self.hra.herni_pole[pole.cislo_pole - self.hra.kostka.kostka_3 - 1].zasobnik) < 5 or \
                       pole.cislo_pole - self.hra.kostka.kostka_3 >= 1 and pole.barva == "Č" and self.hra.herni_pole[pole.cislo_pole - self.hra.kostka.kostka_3 - 1].barva == "B" and len(self.hra.herni_pole[pole.cislo_pole - self.hra.kostka.kostka_3 - 1].zasobnik) == 1 and self.hra.kostka.kostka_3 != 0:
                        start = pole.cislo_pole
                        pohyby_start.append(start)
                    if pole.cislo_pole - self.hra.kostka.kostka_4 >= 1 and pole.barva == "Č" and self.hra.herni_pole[pole.cislo_pole - self.hra.kostka.kostka_4 - 1].barva != "B" and self.hra.kostka.kostka_4 != 0 and len(self.hra.herni_pole[pole.cislo_pole - self.hra.kostka.kostka_4 - 1].zasobnik) < 5 or \
                       pole.cislo_pole - self.hra.kostka.kostka_4 >= 1 and pole.barva == "Č" and self.hra.herni_pole[pole.cislo_pole - self.hra.kostka.kostka_4 - 1].barva == "B" and len(self.hra.herni_pole[pole.cislo_pole - self.hra.kostka.kostka_4 - 1].zasobnik) == 1 and self.hra.kostka.kostka_4 != 0:
                        start = pole.cislo_pole
                        pohyby_start.append(start)

            if self.hra.kostka.double == 0 and self.hra.kostka.kostka_1 > 0 and self.hra.kostka.kostka_2 > 0:
                inp = rand(1,2)
            elif self.hra.kostka.double == 0 and self.hra.kostka.kostka_1 == 0 and self.hra.kostka.kostka_2 > 0:
                inp = 2
            elif self.hra.kostka.double == 0 and self.hra.kostka.kostka_1 > 0 and self.hra.kostka.kostka_2 == 0:
                inp = 1
            elif self.hra.kostka.double == 2 and self.hra.kostka.kostka_1 > 0 and self.hra.kostka.kostka_2 > 0:
                inp = rand(1,4)
            elif self.hra.kostka.double == 2 and self.hra.kostka.kostka_1 > 0 and self.hra.kostka.kostka_2 == 0:
                inp = 1
            elif self.hra.kostka.double == 2 and self.hra.kostka.kostka_1 == 0 and self.hra.kostka.kostka_2 > 0:
                inp = rand(2,4)
            elif self.hra.kostka.double == 2 and self.hra.kostka.kostka_1 == 0 and self.hra.kostka.kostka_2 == 0:
                inp = rand(3,4)
            elif self.hra.kostka.double == 1 and self.hra.kostka.kostka_3 == 0 and self.hra.kostka.kostka_4 > 0:
                inp = 4
            elif self.hra.kostka.double == 1 and self.hra.kostka.kostka_1 == 0 and self.hra.kostka.kostka_2 > 0:
                inp = 2
            elif self.hra.kostka.double == 1 and self.hra.kostka.kostka_1 > 0 and self.hra.kostka.kostka_2 == 0:
                inp = 1
            elif self.hra.kostka.double == 1 and self.hra.kostka.kostka_3 > 0 and self.hra.kostka.kostka_4 == 0:
                inp = 3

            if inp == 1:                                                
                if self.barva == 'Černý':
                    start_pol = pohyby_start[rand(0, len(pohyby_start)-1)]
                    cil = start_pol - self.hra.kostka.kostka_1
                    print(cil)
                else:
                    start_pol = pohyby_start[rand(0, len(pohyby_start)-1)]
                    cil = start_pol + self.hra.kostka.kostka_1
                    print(cil)
            elif inp == 2:
                if self.barva == 'Černý':
                    start_pol = pohyby_start[rand(0, len(pohyby_start)-1)]
                    cil = start_pol - self.hra.kostka.kostka_2
                    print(cil)
                else:
                    start_pol = pohyby_start[rand(0, len(pohyby_start)-1)]
                    cil = start_pol + self.hra.kostka.kostka_2
                    print(cil)                             
            elif inp == 3 and self.hra.kostka.kostka_1 == self.hra.kostka.kostka_2:
                if self.barva == 'Černý':
                    start_pol = pohyby_start[rand(0, len(pohyby_start)-1)]
                    cil = start_pol - self.hra.kostka.kostka_3
                    print(cil)
                else:
                    start_pol = pohyby_start[rand(0, len(pohyby_start)-1)]
                    cil = start_pol + self.hra.kostka.kostka_3
                    print(cil)                         # Možnost pohybu o součet obou kostek
            elif inp == 4 and self.hra.kostka.kostka_1 == self.hra.kostka.kostka_2:
                if self.barva == 'Černý':
                    start_pol = pohyby_start[rand(0, len(pohyby_start)-1)]
                    cil = start_pol - self.hra.kostka.kostka_4
                    print(cil)
                else:
                    start_pol = pohyby_start[rand(0, len(pohyby_start)-1)]
                    cil = start_pol + self.hra.kostka.kostka_4
                    print(cil)
            else:
                print("Špatné zadání!")
                return

            start = start_pol

            if self.barva == 'Černý':
                if start < 1 or start > 24 or cil < 1 or cil > 24 or cil > start:
                    print("Neplatné číslo pole!")
                    return
            else:
                if start < 1 or start > 24 or cil < 1 or cil > 24 or cil < start:
                    print("Neplatné číslo pole!")
                    return

            pole_start = self.hra.herni_pole[start - 1]
            pole_cil = self.hra.herni_pole[cil - 1]
            
            if self.barva == "Černý":
                vyhazovac = cil - 1
            if self.barva == "Bílý":
                vyhazovac = cil - 1 

            if len(pole_cil.zasobnik) == 5:                                     # Ošetření, aby zásobník, na který se přidává nebyl plný
                print("Tento zásobník je již plný!")
            else:
                if len(pole_start.zasobnik) > 0:                                # Pokud je prázdný, může se na něj přidat
                    temp =[]
                    temp.append(pole_start.zasobnik[0])

                    if pole_start.zasobnik[0].barva != self.barva:              # Ošetření, aby hráč přidával na svoje nebo prázdné pole
                        print("Na zadaném poli nemáte zetony vaší barvy!")
                    elif pole_cil.barva != pole_start.barva and pole_cil.barva != "N" and len(pole_cil.zasobnik) !=1:
                        print("Na poli nejsou tvé žetony!")
                    elif pole_cil.barva == pole_start.barva or pole_cil.barva == "N" or pole_cil.barva != pole_start.barva and len(pole_cil.zasobnik) == 1:
                        if pole_cil.barva != pole_start.barva and len(pole_cil.zasobnik) == 1:
                            self.hra.barec.pridej_do_baru(vyhazovac)
                            pole_start.zasobnik.remove(pole_start.zasobnik[0])
                            pole_cil.zasobnik.append(temp[0])
                            if inp == 1:                                            # Zde se nastavují hodnoty, podle toho co se hráč rozhodne udělat při přesunech žetonu o jednu, druhou nebo součet obou kostek
                                self.hra.presuny = self.hra.presuny + 1
                                self.hra.kostka.kostka_1 = 0
                            elif inp == 2:
                                self.hra.presuny = self.hra.presuny + 1
                                self.hra.kostka.kostka_2 = 0
                            elif inp == 3:
                                self.hra.kostka.kostka_3 = 0
                                self.hra.kostka.double -= 1
                            elif inp == 4:
                                self.hra.kostka.kostka_4 = 0
                                self.hra.kostka.double -= 1
                        elif pole_cil.barva == pole_start.barva or pole_cil.barva == "N":
                            pole_start.zasobnik.remove(pole_start.zasobnik[0])
                            pole_cil.zasobnik.append(temp[0])
                            if inp == 1:                                            # Zde se nastavují hodnoty, podle toho co se hráč rozhodne udělat při přesunech žetonu o jednu, druhou nebo součet obou kostek
                                self.hra.presuny = self.hra.presuny + 1
                                self.hra.kostka.kostka_1 = 0
                            elif inp == 2:
                                self.hra.presuny = self.hra.presuny + 1
                                self.hra.kostka.kostka_2 = 0
                            elif inp == 3:
                                self.hra.kostka.kostka_3 = 0
                                self.hra.kostka.double -= 1
                            elif inp == 4:
                                self.hra.kostka.kostka_4 = 0
                                self.hra.kostka.double -= 1
                else:
                    print("Pole ze kterého se snažíte brát, je prázdné!")
        elif self.hra.presuny == 2:
            print("Už jsi táhl za obě kostky!")
        elif self.hra.hozeno == 0:
            print("Nejdřív si hoď!")
        elif self.barva == "Černý" and len(self.hra.barec.zetony_cerna) > 0 or self.barva == "Bílý" and len(self.hra.barec.zetony_bila) >0:
            print("Nejdřív vyjeď z baru!")
                        

    def vyhod_z_baru(self):                                       
        if self.barva == "Bílý" and len(self.hra.barec.zetony_bila) >= 1:
            if len(self.hra.barec.zetony_bila) >= 1:
                x = self.hra.barec.zetony_bila.pop(-1)[0]
                self.hra.barec.vyjeti_z_baru_ai(x, "Bílý")
            else:
                pass
        elif self.barva == "Černý" and len(self.hra.barec.zetony_cerna) >= 1:
            if len(self.hra.barec.zetony_cerna) >= 1:
                x = self.hra.barec.zetony_cerna.pop(-1)[0]
                self.hra.barec.vyjeti_z_baru_ai(x, "Černý")
            else:
                pass
        else:
            pass

    def jedu_do_cile(self):
        start = 0
        start_pol = 0
        pohyby_start = []
        self.kontrola_cerna = 0
        self.kontrola_bila = 0
        for i in range(6):
            for objekt in self.hra.herni_pole[i].zasobnik:
                if objekt.barva == "Černý":
                    self.kontrola_cerna += 1

        for j in range(18,23):
            for objekt in self.hra.herni_pole[j].zasobnik:
                if objekt.barva == "Bílý":
                    self.kontrola_bila += 1

        vse_akt_zetony_cerna = 15 - len(self.hra.cilove_pole_cerna)
        vse_akt_zetony_bila = 15 - len(self.hra.cilove_pole_bila)
        
        if self.barva == "Černý" and self.kontrola_cerna == vse_akt_zetony_cerna or self.barva == "Bílý" and self.kontrola_bila == vse_akt_zetony_bila:
            if self.hra.presuny < 2:
                if self.barva == "Bílý":
                    for pole in self.hra.herni_pole:
                        if pole.cislo_pole + self.hra.kostka.kostka_1 <= 24 and pole.barva == "B" and self.hra.herni_pole[pole.cislo_pole + self.hra.kostka.kostka_1 - 1].barva != "Č" and self.hra.kostka.kostka_1 != 0 and len(self.hra.herni_pole[pole.cislo_pole + self.hra.kostka.kostka_1 - 1].zasobnik) < 5 or \
                        pole.cislo_pole + self.hra.kostka.kostka_1 <= 24 and pole.barva == "B" and self.hra.herni_pole[pole.cislo_pole + self.hra.kostka.kostka_1 - 1].barva == "Č" and len(self.hra.herni_pole[pole.cislo_pole + self.hra.kostka.kostka_1 - 1].zasobnik) == 1 and self.hra.kostka.kostka_1 != 0:
                            start = pole.cislo_pole
                            pohyby_start.append(start)
                        elif pole.cislo_pole + self.hra.kostka.kostka_2 <= 24 and pole.barva == "B" and self.hra.herni_pole[pole.cislo_pole + self.hra.kostka.kostka_2 - 1].barva != "Č" and self.hra.kostka.kostka_2 != 0 and len(self.hra.herni_pole[pole.cislo_pole + self.hra.kostka.kostka_2 - 1].zasobnik) < 5 or \
                        pole.cislo_pole + self.hra.kostka.kostka_2 <= 24 and pole.barva == "B" and self.hra.herni_pole[pole.cislo_pole + self.hra.kostka.kostka_2 - 1].barva == "Č" and len(self.hra.herni_pole[pole.cislo_pole + self.hra.kostka.kostka_2 - 1].zasobnik) == 1 and self.hra.kostka.kostka_2 != 0:
                            start = pole.cislo_pole
                            pohyby_start.append(start)

                        elif pole.cislo_pole + self.hra.kostka.kostka_3 <= 24 and pole.barva == "B" and self.hra.herni_pole[pole.cislo_pole + self.hra.kostka.kostka_3 - 1].barva != "Č" and self.hra.kostka.kostka_3 != 0 and len(self.hra.herni_pole[pole.cislo_pole + self.hra.kostka.kostka_3 - 1].zasobnik) < 5 or \
                        pole.cislo_pole + self.hra.kostka.kostka_3 <= 24 and pole.barva == "B" and self.hra.herni_pole[pole.cislo_pole + self.hra.kostka.kostka_3 - 1].barva == "Č" and len(self.hra.herni_pole[pole.cislo_pole + self.hra.kostka.kostka_3 - 1].zasobnik) == 1 and self.hra.kostka.kostka_3 != 0:
                            start = pole.cislo_pole
                            pohyby_start.append(start)

                        elif pole.cislo_pole + self.hra.kostka.kostka_4 <= 24 and pole.barva == "B" and self.hra.herni_pole[pole.cislo_pole + self.hra.kostka.kostka_4 - 1].barva != "Č" and self.hra.kostka.kostka_4 != 0 and len(self.hra.herni_pole[pole.cislo_pole + self.hra.kostka.kostka_4 - 1].zasobnik) < 5 or \
                        pole.cislo_pole + self.hra.kostka.kostka_4 <= 24 and pole.barva == "B" and self.hra.herni_pole[pole.cislo_pole + self.hra.kostka.kostka_4 - 1].barva == "Č" and len(self.hra.herni_pole[pole.cislo_pole + self.hra.kostka.kostka_4 - 1].zasobnik) == 1 and self.hra.kostka.kostka_4 != 0:
                            start = pole.cislo_pole
                            pohyby_start.append(start)
                            
                elif self.barva == "Černý":
                    for pole in self.hra.herni_pole:
                        if pole.cislo_pole - self.hra.kostka.kostka_1 >= 1 and pole.barva == "Č" and self.hra.herni_pole[pole.cislo_pole - self.hra.kostka.kostka_1 - 1].barva != "B" and self.hra.kostka.kostka_1 != 0 and len(self.hra.herni_pole[pole.cislo_pole - self.hra.kostka.kostka_1 - 1].zasobnik) < 5 or \
                        pole.cislo_pole - self.hra.kostka.kostka_1 >= 1 and pole.barva == "Č" and self.hra.herni_pole[pole.cislo_pole - self.hra.kostka.kostka_1 - 1].barva == "B" and len(self.hra.herni_pole[pole.cislo_pole - self.hra.kostka.kostka_1 - 1].zasobnik) == 1 and self.hra.kostka.kostka_1 != 0:
                            start = pole.cislo_pole
                            pohyby_start.append(start)
                        if pole.cislo_pole - self.hra.kostka.kostka_2 >= 1 and pole.barva == "Č" and self.hra.herni_pole[pole.cislo_pole - self.hra.kostka.kostka_2 - 1].barva != "B" and self.hra.kostka.kostka_2 != 0 and len(self.hra.herni_pole[pole.cislo_pole - self.hra.kostka.kostka_2 - 1].zasobnik) < 5 or \
                        pole.cislo_pole - self.hra.kostka.kostka_2 >= 1 and pole.barva == "Č" and self.hra.herni_pole[pole.cislo_pole - self.hra.kostka.kostka_2 - 1].barva == "B" and len(self.hra.herni_pole[pole.cislo_pole - self.hra.kostka.kostka_2 - 1].zasobnik) == 1 and self.hra.kostka.kostka_2 != 0:
                            start = pole.cislo_pole
                            pohyby_start.append(start)
                        if pole.cislo_pole - self.hra.kostka.kostka_3 >= 1 and pole.barva == "Č" and self.hra.herni_pole[pole.cislo_pole - self.hra.kostka.kostka_3 - 1].barva != "B" and self.hra.kostka.kostka_3 != 0 and len(self.hra.herni_pole[pole.cislo_pole - self.hra.kostka.kostka_3 - 1].zasobnik) < 5 or \
                        pole.cislo_pole - self.hra.kostka.kostka_3 >= 1 and pole.barva == "Č" and self.hra.herni_pole[pole.cislo_pole - self.hra.kostka.kostka_3 - 1].barva == "B" and len(self.hra.herni_pole[pole.cislo_pole - self.hra.kostka.kostka_3 - 1].zasobnik) == 1 and self.hra.kostka.kostka_3 != 0:
                            start = pole.cislo_pole
                            pohyby_start.append(start)
                        if pole.cislo_pole - self.hra.kostka.kostka_4 >= 1 and pole.barva == "Č" and self.hra.herni_pole[pole.cislo_pole - self.hra.kostka.kostka_4 - 1].barva != "B" and self.hra.kostka.kostka_4 != 0 and len(self.hra.herni_pole[pole.cislo_pole - self.hra.kostka.kostka_4 - 1].zasobnik) < 5 or \
                        pole.cislo_pole - self.hra.kostka.kostka_4 >= 1 and pole.barva == "Č" and self.hra.herni_pole[pole.cislo_pole - self.hra.kostka.kostka_4 - 1].barva == "B" and len(self.hra.herni_pole[pole.cislo_pole - self.hra.kostka.kostka_4 - 1].zasobnik) == 1 and self.hra.kostka.kostka_4 != 0:
                            start = pole.cislo_pole
                            pohyby_start.append(start)

                if self.hra.kostka.double == 0 and self.hra.kostka.kostka_1 > 0 and self.hra.kostka.kostka_2 > 0:
                    inp = rand(1,2)
                elif self.hra.kostka.double == 0 and self.hra.kostka.kostka_1 == 0 and self.hra.kostka.kostka_2 > 0:
                    inp = 2
                elif self.hra.kostka.double == 0 and self.hra.kostka.kostka_1 > 0 and self.hra.kostka.kostka_2 == 0:
                    inp = 1
                elif self.hra.kostka.double == 2 and self.hra.kostka.kostka_1 > 0 and self.hra.kostka.kostka_2 > 0:
                    inp = rand(1,4)
                elif self.hra.kostka.double == 2 and self.hra.kostka.kostka_1 > 0 and self.hra.kostka.kostka_2 == 0:
                    inp = 1
                elif self.hra.kostka.double == 2 and self.hra.kostka.kostka_1 == 0 and self.hra.kostka.kostka_2 > 0:
                    inp = rand(2,4)
                elif self.hra.kostka.double == 2 and self.hra.kostka.kostka_1 == 0 and self.hra.kostka.kostka_2 == 0:
                    inp = rand(3,4)
                elif self.hra.kostka.double == 1 and self.hra.kostka.kostka_3 == 0 and self.hra.kostka.kostka_4 > 0:
                    inp = 4
                elif self.hra.kostka.double == 1 and self.hra.kostka.kostka_1 == 0 and self.hra.kostka.kostka_2 > 0:
                    inp = 2
                elif self.hra.kostka.double == 1 and self.hra.kostka.kostka_1 > 0 and self.hra.kostka.kostka_2 == 0:
                    inp = 1
                elif self.hra.kostka.double == 1 and self.hra.kostka.kostka_3 > 0 and self.hra.kostka.kostka_4 == 0:
                    inp = 3

                if inp == 1:                                                
                    if self.barva == 'Černý':
                        start_pol = pohyby_start[rand(0, len(pohyby_start)-1)]
                        cil = start_pol - self.hra.kostka.kostka_1
                        print(cil)
                    else:
                        start_pol = pohyby_start[rand(0, len(pohyby_start)-1)]
                        cil = start_pol + self.hra.kostka.kostka_1
                        print(cil)
                elif inp == 2:
                    if self.barva == 'Černý':
                        start_pol = pohyby_start[rand(0, len(pohyby_start)-1)]
                        cil = start_pol - self.hra.kostka.kostka_2
                        print(cil)
                    else:
                        start_pol = pohyby_start[rand(0, len(pohyby_start)-1)]
                        cil = start_pol + self.hra.kostka.kostka_2
                        print(cil)                             
                elif inp == 3 and self.hra.kostka.kostka_1 == self.hra.kostka.kostka_2:
                    if self.barva == 'Černý':
                        start_pol = pohyby_start[rand(0, len(pohyby_start)-1)]
                        cil = start_pol - self.hra.kostka.kostka_3
                        print(cil)
                    else:
                        start_pol = pohyby_start[rand(0, len(pohyby_start)-1)]
                        cil = start_pol + self.hra.kostka.kostka_3
                        print(cil)                         
                elif inp == 4 and self.hra.kostka.kostka_1 == self.hra.kostka.kostka_2:
                    if self.barva == 'Černý':
                        start_pol = pohyby_start[rand(0, len(pohyby_start)-1)]
                        cil = start_pol - self.hra.kostka.kostka_4
                        print(cil)
                    else:
                        start_pol = pohyby_start[rand(0, len(pohyby_start)-1)]
                        cil = start_pol + self.hra.kostka.kostka_4
                        print(cil)
                else:
                    print("Špatné zadání!")
                    return

                start = start_pol


                        
                if self.barva == 'Černý':
                    if start > 6 or start < 0 and start != 0:
                        print("Neplatné číslo pole!")
                        return
                else:
                    if start < 19 or start > 24 and cil != 25:
                        print("Neplatné číslo pole!")
                        return

                pole_start = self.hra.herni_pole[start - 1]
                if self.barva == "Černý":
                    pole_cil = self.hra.cilove_pole_cerna
                elif self.barva == "Bílý":
                    pole_cil = self.hra.cilove_pole_bila

                if cil == 0 and self.barva == "Černý" or cil == 25 and self.barva == "Bílý":                                     # Ošetření, aby zásobník, na který se přidává nebyl plný
                    temp =[]
                    temp.append(pole_start.zasobnik[0])
                    pole_cil.append(temp[0])
                    pole_start.zasobnik.remove(pole_start.zasobnik[0])
                    if inp == 1:                                            # Zde se nastavují hodnoty, podle toho co se hráč rozhodne udělat při přesunech žetonu o jednu, druhou nebo součet obou kostek
                        self.hra.presuny = self.hra.presuny + 1
                        self.hra.kostka.kostka_1 = 0
                    elif inp == 2:
                        self.hra.presuny = self.hra.presuny + 1
                        self.hra.kostka.kostka_2 = 0
                    elif inp == 3:
                        self.hra.kostka.kostka_3 = 0
                    elif inp == 4:
                        self.hra.kostka.kostka_4 = 0
                else:
                    print(cil)
                    print("Něco se pokazilo")

            elif self.hra.presuny == 2:
                print("Už jsi táhl za obě kostky!")
        else:
            print("Nemáš všechny žetony na posledních polích!")

    def nabidka(self):
        if self.hra.hozeno == 0:
            self.hra.kostka.hod_kostkami()
        self.kontrola_pohybu()
        if self.barva == "Bílý" and self.kontrola_bila == 15 or self.barva == "Černý" and self.kontrola_cerna == 15:
            self.jedu_do_cile()
        if len(self.hra.barec.zetony_bila) == 0 and self.barva == "Bílý" or len(self.hra.barec.zetony_cerna) == 0 and self.barva == "Černý":
            self.tah()
        elif len(self.hra.barec.zetony_bila) > 0 and self.barva == "Bílý" or len(self.hra.barec.zetony_cerna) > 0 and self.barva == "Černý":
            self.vyhod_z_baru()
        self.prerus_tah()