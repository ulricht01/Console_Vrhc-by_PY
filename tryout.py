import random, sys, os

rand = random.randint

class HerniDeska:
    def __init__(self):

        self.token = rand(0,1)
        barevny_seznam = ["Černý", "Bílý"]
        random.shuffle(barevny_seznam)

        volba = input("Budeš hrát s hráčem (1), nebo s AI (0)?")
        if volba == "1":
            hrac1 = input("Jméno hráče 1: ")
            self.Hrac1 = KonzolovyHrac(hrac1, barevny_seznam[0])
            hrac2 = input("Jméno hráče 2: ")
            self.Hrac2 = KonzolovyHrac(hrac2, barevny_seznam[1])
        elif volba == "0":
            hrac1 = input("Jméno hráče 1: ")
            self.Hrac1 = KonzolovyHrac(hrac1, barevny_seznam[0])
            hrac2 = input("Jméno Ai 1: ")
            self.Hrac2 = AiHrac(hrac2, barevny_seznam[1]) 

        self.kostka = DvojKostka()
        self.barec = Bar()

        self.herni_pole = []
        for cislo in range(1, 25):
            self.herni_pole.append(HerniPole(cislo))
        
    
    def vytvor_hraci_plochu(self):
        if self.Hrac1.barva == "Bílá":
            pocet_zetonu_hrac1 = self.barec.pocet_zetonu_bila
            pocet_zetonu_hrac2 = self.barec.pocet_zetonu_cerna
        else:
            pocet_zetonu_hrac1 = self.barec.pocet_zetonu_cerna
            pocet_zetonu_hrac2 = self.barec.pocet_zetonu_bila
        for i in range(0,24):
            self.herni_pole[i].barva_pole()

        plocha = f"""
        +------+------+------+------+------+------+-----+------+------+------+------+------+------+--------+
        |  24  |  23  |  22  |  21  |  20  |  19  | BAR |  18  |  17  |  16  |  15  |  14  |  13  |   CIL  |
        |  {self.herni_pole[23].barva}   |  {self.herni_pole[22].barva}   |  {self.herni_pole[21].barva}   |  {self.herni_pole[20].barva}   |  {self.herni_pole[19].barva}   |  {self.herni_pole[18].barva}   |     |  {self.herni_pole[17].barva}   |  {self.herni_pole[16].barva}   |  {self.herni_pole[15].barva}   |  {self.herni_pole[14].barva}   |  {self.herni_pole[13].barva}   |  {self.herni_pole[12].barva}   |        |
        |  {len(self.herni_pole[23].zasobnik)}   |  {len(self.herni_pole[22].zasobnik)}   |  {len(self.herni_pole[21].zasobnik)}   |  {len(self.herni_pole[20].zasobnik)}   |  {len(self.herni_pole[19].zasobnik)}   |  {len(self.herni_pole[18].zasobnik)}   |  {pocet_zetonu_hrac1}  |  {len(self.herni_pole[17].zasobnik)}   |  {len(self.herni_pole[16].zasobnik)}   |  {len(self.herni_pole[15].zasobnik)}   |  {len(self.herni_pole[14].zasobnik)}   |  {len(self.herni_pole[13].zasobnik)}   |  {len(self.herni_pole[12].zasobnik)}   |        | {hra.Hrac1.barva}
        +------+------+------+------+------+------+-----+------+------+------+------+------+------+--------+
        |  12  |  11  |  10  |   9  |   8  |   7  |     |   6  |   5  |   4  |   3  |   2  |   1  |        |
        |  {self.herni_pole[11].barva}   |  {self.herni_pole[10].barva}   |  {self.herni_pole[9].barva}   |  {self.herni_pole[8].barva}   |  {self.herni_pole[7].barva}   |  {self.herni_pole[6].barva}   |     |  {self.herni_pole[5].barva}   |  {self.herni_pole[4].barva}   |  {self.herni_pole[3].barva}   |  {self.herni_pole[2].barva}   |  {self.herni_pole[1].barva}   |  {self.herni_pole[0].barva}   |        |
        |  {len(self.herni_pole[11].zasobnik)}   |  {len(self.herni_pole[10].zasobnik)}   |  {len(self.herni_pole[9].zasobnik)}   |  {len(self.herni_pole[8].zasobnik)}   |  {len(self.herni_pole[7].zasobnik)}   |  {len(self.herni_pole[6].zasobnik)}   |  {pocet_zetonu_hrac2}  |  {len(self.herni_pole[5].zasobnik)}   |  {len(self.herni_pole[4].zasobnik)}   |  {len(self.herni_pole[3].zasobnik)}   |  {len(self.herni_pole[2].zasobnik)}   |  {len(self.herni_pole[1].zasobnik)}   |  {len(self.herni_pole[0].zasobnik)}   |        | {hra.Hrac2.barva}
        +------+------+------+------+------+------+-----+------+------+------+------+------+------+--------+
                                      +-----------------------------+
                                      |   Kostka 1   |   Kostka 2   |
                                      |      {self.kostka.kostka_1}       |      {self.kostka.kostka_2}       |
                                      +--------------+--------------+
                                           
        """
        print(plocha)

    def priprav_hru(self):
        for i in range(1,6):
            hra.barec.vytvor_start_bily(11)
            hra.barec.vytvor_start_bily(17)
            hra.barec.vytvor_start_cerny(23)
            hra.barec.vytvor_start_cerny(5)
        for i in range(1,4):
            hra.barec.vytvor_start_bily(19)
            hra.barec.vytvor_start_cerny(7)
        for i in range(1,3):
            hra.barec.vytvor_start_bily(0)
            hra.barec.vytvor_start_cerny(12)

class HerniPole:
    def __init__(self, cislo_pole, zasobnik = None):
        self.cislo_pole = cislo_pole
        self.zasobnik = zasobnik if zasobnik is not None else []
        if len(self.zasobnik) == 0:
            self.barva = "N"
        elif self.zasobnik[0].barva == "Bílý":
            self.barva = "B"
        elif self.zasobnik[0].barva == "Černý":
            self.barva = "Č"
        
    def barva_pole(self):
        if len(self.zasobnik) == 0:
            self.barva = "N"
        elif self.zasobnik[0].barva == "Bílý":
            self.barva = "B"
        elif self.zasobnik[0].barva == "Černý":
            self.barva = "Č"


class DvojKostka:
    def __init__(self):
        self.kostka_1 = 0
        self.kostka_2 = 0

    def hod_kostkami(self):
        self.kostka_1 = rand(1, 6)
        self.kostka_2 = rand(1, 6)
        return self.kostka_1, self.kostka_2

class Bar:
    def __init__(self, zetony_bila = [], zetony_cerna = []):
        self.pocet_zetonu_bila = len(zetony_bila)
        self.pocet_zetonu_cerna = len(zetony_cerna)
        kamen = None
    
    def vytvor_kamen_bily(self, barva = "Bílý"):
        kamen = HerniKamen(barva)
        cil = hra.herni_pole[int(input(""))].zasobnik
        cil.append(kamen)

    def vytvor_kamen_cerny(self, barva = "Černý"):
        kamen = HerniKamen(barva)
        cil = hra.herni_pole[int(input(""))].zasobnik
        cil.append(kamen)

    def vytvor_start_bily(self, x, barva = "Bílý"):
        kamen = HerniKamen(barva)
        cil = hra.herni_pole[x].zasobnik
        cil.append(kamen)

    def vytvor_start_cerny(self, x, barva = "Černý"):
        kamen = HerniKamen(barva)
        cil = hra.herni_pole[x].zasobnik
        cil.append(kamen)

    def vyhod_z_baru(self):
        pass

    def pridej_do_baru(self):
        pass
    

class HerniKamen:
    def __init__(self, barva):
        self.barva = barva

class Hrac:
    def __init__(self, jmeno, barva):
        self.jmeno = jmeno
        self.barva = barva 

class KonzolovyHrac(Hrac):
    def tah(self, temp= []):
        start = int(input("Zadej číslo pole, odkud vybíráš: "))
        cil = int(input("Zadej číslo pole, kam chceš dát zetony: "))

        if start < 1 or start > 24 or cil < 1 or cil > 24:
            print("Neplatné číslo pole!")
            return

        pole_start = hra.herni_pole[start - 1]
        pole_cil = hra.herni_pole[cil - 1]
        if len(pole_cil.zasobnik) == 5:
            print("Tento zásobník je již plný!")
        else:
            if len(pole_start.zasobnik) > 0:
                temp =[]
                temp.append(pole_start.zasobnik[0])

                if pole_start.zasobnik[0].barva != self.barva:
                    print("Na zadaném poli nemáte zetony vaší barvy!")
                elif pole_cil.barva != pole_start.barva and pole_cil.barva != "N":
                    print("Na poli nejsou tvé žetony!")
                else:
                    pole_start.zasobnik.remove(pole_start.zasobnik[0])
                    pole_cil.zasobnik.append(temp[0])
            else:
                print("Pole ze kterého se snažíte brát, je prázdné!")

    def prerus_tah(self):
        if hra.token == 0:
            hra.token = 1
        else:
            hra.token = 0

    def nabidka(self):
        print("1) Pohni s kameny!")
        print("2) Zobraz plochu!")
        print("3) Ukonči tah!")
        akce = int(input("Zadej akci: "))

        if akce == 1:
            if hra.token == 0:
                hra.Hrac1.tah()
            else:
                hra.Hrac2.tah()
        elif akce == 2:
            hra.vytvor_hraci_plochu()
        elif akce == 3:
            if hra.token == 0:
                hra.Hrac1.prerus_tah()
            else:
                hra.Hrac2.prerus_tah()
        else:
            print("Neplatná akce!")
            
        



class AiHrac(Hrac):
    pass

hra = HerniDeska()
hra.priprav_hru()
while True:
    hra.vytvor_hraci_plochu()
    if hra.token == 0:
        hra.Hrac1.nabidka()
    elif hra.token == 1:
        hra.Hrac2.prerus_tah()


    input("")
