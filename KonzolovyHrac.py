from Hrac import *
from DvojKostka import *
from HerniDeska import *

import random, sys, os, json
rand = random.randint

class KonzolovyHrac(Hrac):              # Třída konzolového hráče
    def __init__(self, jmeno, barva, hra):
        super().__init__(jmeno, barva,hra)

    def tah(self, temp= []):                                            # Metoda pohybu žetonu hráče
        if self.hra.presuny < 2 and self.barva == "Černý" and len(self.hra.barec.zetony_cerna) == 0 and self.hra.hozeno == 1 and self.hra.kostka.double == 0 or self.hra.presuny < 2 and self.barva == "Bílý" and len(self.hra.barec.zetony_bila) == 0 and self.hra.hozeno == 1 and self.hra.kostka.double == 0 or \
           self.hra.presuny <= 2 and self.barva == "Černý" and len(self.hra.barec.zetony_cerna) == 0 and self.hra.hozeno == 1 and self.hra.kostka.double > 0 or self.hra.presuny <= 2 and self.barva == "Bílý" and len(self.hra.barec.zetony_bila) == 0 and self.hra.hozeno == 1 and self.hra.kostka.double > 0:
            print("Tvé možné pohyby jsou: ")
            
            self.kontrola_pohybu()

            start = int(input("Zadej číslo pole, odkud vybíráš: "))
            if self.hra.kostka.kostka_1 != self.hra.kostka.kostka_2:     
                print("1) O počet na 1. kostce")
                print("2) O počet na 2. kostce")
            elif self.hra.kostka.kostka_3 != 0 or self.hra.kostka.kostka_4 !=0:
                print("1) O počet na 1. kostce")
                print("2) O počet na 2. kostce")
                print("3) O počet na 1. double")
                print("4) O počet na 2. double")
            inp = int(input("Zadej: "))
            if inp == 1:                                                # Možnost pohybu o první kostku
                if self.barva == 'Černý':
                    cil = start - self.hra.kostka.kostka_1
                else:
                    cil = start + self.hra.kostka.kostka_1
            elif inp == 2:
                if self.barva == 'Černý':
                    cil = start - self.hra.kostka.kostka_2
                else:
                    cil = start + self.hra.kostka.kostka_2                               # Možnost pohybu o druhou kostku
            elif inp == 3 and self.hra.kostka.kostka_1 == self.hra.kostka.kostka_2:
                if self.barva == 'Černý':
                    cil = start - self.hra.kostka.kostka_3
                else:
                    cil = start + self.hra.kostka.kostka_3                          # Možnost pohybu o součet obou kostek
            elif inp == 4 and self.hra.kostka.kostka_1 == self.hra.kostka.kostka_2:
                if self.barva == 'Černý':
                    cil = start - self.hra.kostka.kostka_4
                else:
                    cil = start + self.hra.kostka.kostka_4
            else:
                print("Špatné zadání!")
                return

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

    def jedu_do_cile(self):
        kontrola_cerna = 0
        kontrola_bila = 0
        for i in range(6):
            for objekt in self.hra.herni_pole[i].zasobnik:
                if objekt.barva == "Černý":
                    kontrola_cerna += 1

        for j in range(18,23):
            for objekt in self.hra.herni_pole[j].zasobnik:
                if objekt.barva == "Bílý":
                    kontrola_bila += 1

        vse_akt_zetony_cerna = 15 - len(self.hra.cilove_pole_cerna)
        vse_akt_zetony_bila = 15 - len(self.hra.cilove_pole_bila)
        
        if self.barva == "Černý" and kontrola_cerna == vse_akt_zetony_cerna or self.barva == "Bílý" and kontrola_bila == vse_akt_zetony_bila:
            if self.hra.presuny < 2:
                start = int(input("Zadej číslo pole, odkud vybíráš: "))
                if self.hra.kostka.kostka_1 != self.hra.kostka.kostka_2:     
                    print("1) O počet na 1. kostce")
                    print("2) O počet na 2. kostce")
                elif self.hra.kostka.kostka_1 == self.hra.kostka.kostka_2:
                    print("1) O počet na 1. kostce")
                    print("2) O počet na 2. kostce")
                    print("3) O počet na 1. double")
                    print("4) O počet na 2. double")
                inp = int(input("Zadej: "))
                if inp == 1:                                                # Možnost pohybu o první kostku
                    if self.barva == 'Černý':
                        cil = start - self.hra.kostka.kostka_1
                    else:
                        cil = start + self.hra.kostka.kostka_1
                elif inp == 2:
                    if self.barva == 'Černý':
                        cil = start - self.hra.kostka.kostka_2
                    else:
                        cil = start + self.hra.kostka.kostka_2                               # Možnost pohybu o druhou kostku
                elif inp == 3 and self.hra.kostka.kostka_1 == self.hra.kostka.kostka_2:
                    if self.barva == 'Černý':
                        cil = start - self.hra.kostka.kostka_3
                    else:
                        cil = start + self.hra.kostka.kostka_3                          # Možnost pohybu o součet obou kostek
                elif inp == 4 and self.hra.kostka.kostka_1 == self.hra.kostka.kostka_2:
                    if self.barva == 'Černý':
                        cil = start - self.hra.kostka.kostka_4
                    else:
                        cil = start + self.hra.kostka.kostka_4
                else:
                    print("Špatné zadání!")
                    return


                        
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

    def vyhod_z_baru(self):                                       
        if self.barva == "Bílý" and len(self.hra.barec.zetony_bila) >= 1:
            if len(self.hra.barec.zetony_bila) >= 1:
                x = self.hra.barec.zetony_bila.pop(-1)[0]
                self.hra.barec.vyjeti_z_baru(x, "Bílý")
            else:
                print("Na baru nemáš žádné žetony!")
        elif self.barva == "Černý" and len(self.hra.barec.zetony_cerna) >= 1:
            if len(self.hra.barec.zetony_cerna) >= 1:
                x = self.hra.barec.zetony_cerna.pop(-1)[0]
                self.hra.barec.vyjeti_z_baru(x, "Černý")
            else:
                print("Na baru nemáš žádné žetony!")
        else:
            print("Na baru nejsou žádné žetony!")


    def nabidka(self):                                  # Nabídka pro hráče a jeho možné akce
            print("1) Hod kostkami!")
            print("2) Pohni s kameny!")
            print("3) Zobraz plochu!")
            print("4) Ukonči tah!")
            print("5) Vyjed z baru!")
            print("6) Jedu do cíle")
            print("7) Vzdát hru")
            print("8) Ostatní možnosti")
            
            try:
                akce = int(input("Zadej akci: "))
                if akce == 1 and self.hra.hozeno == 0:               # Zjišťování, jakou hráč zvolil akci á různé podmínky ohledně toho jestli házel, přesouval se, apod.
                    if self.hra.token == 0:                        
                        self.hra.kostka.hod_kostkami()
                        self.hra.vytvor_hraci_plochu()
                        self.kontrola_pohybu()
                        if self.hra.Hrac1.valid_moves == 0 and self.hra.token == 0:
                            self.hra.token = 1
                            self.hra.kostka.vynuluj()
                        else:
                            self.hra.hozeno = 1
                    else:                                       
                        self.hra.kostka.hod_kostkami()
                        self.hra.vytvor_hraci_plochu()
                        self.kontrola_pohybu()
                        if self.hra.Hrac2.valid_moves == 0 and self.hra.token == 1:
                            self.hra.token = 0
                            self.hra.kostka.vynuluj()
                        else:
                            self.hra.hozeno = 1
                elif akce == 2:
                    if self.hra.token == 0:
                        self.hra.Hrac1.tah()
                    else:
                        self.hra.Hrac2.tah()
                elif akce == 3:
                    self.hra.vytvor_hraci_plochu()
                elif akce == 4:
                    if self.hra.token == 0:
                        self.hra.Hrac1.prerus_tah()
                    else:
                        self.hra.Hrac2.prerus_tah()
                elif akce == 5:
                    if self.hra.token == 0:
                        self.hra.Hrac1.vyhod_z_baru()
                    elif self.hra.token == 1:
                        self.hra.Hrac2.vyhod_z_baru()
                elif akce == 6:
                    if self.hra.token == 0:
                        self.hra.Hrac1.jedu_do_cile()
                    else:
                        self.hra.Hrac2.jedu_do_cile()
                elif akce == 7:
                    self.hra.rezignace_hry()
                elif akce == 8:
                    print("1) Uložit hru")
                    print("2) Nahrát hru")
                    print("3) Ukončí hru")
                    akce_2 = int(input("Zadej svou akci:"))
                    if akce_2 == 1:
                        self.hra.Ulozit()
                    elif akce_2 == 2:
                        self.hra.Nahrat()
                    elif akce_2 == 3:
                        self.hra.vyhodnoceni()
                elif self.hra.hozeno == 1 and akce ==1:
                    print("Už jsi házel!")
                else:
                    print("Neplatná akce!")
            except:
                print("Neplatná akce")
