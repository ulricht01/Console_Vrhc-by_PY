import random, sys, os, json
rand = random.randint

class HerniDeska:
    def __init__(self):
        self.file_path = './file.json'
        check_file = os.path.isfile(self.file_path)
        """if(check_file):
            print('FILE EXIST!')
        else:
            print('FILE NOT EXIST!')"""
        
        self.token = rand(0,1)                                      # Vytvoření tokenu pro určování, kdo bude začínat
        barevny_seznam = ["Černý", "Bílý"]                          # Seznam barev hráčů 
        random.shuffle(barevny_seznam)                              # Přeházení pořadí (Kvůli random nastavení barvy)

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
            self.Hrac2 = AiHrac(hrac2, barevny_seznam[1])           # Základní nabídka pro tvorbu hry s hráčem/AI hráčem

        self.kostka = DvojKostka()
        self.barec = Bar()
        self.hozeno = 0                                             # Určuje jestli v kole již hráč hodil nebo ne, v případě, že hodil, nastaví se 1
        self.presuny = 0

        self.herni_pole = []                                        # Vytvoření seznamzu herního pole
        for cislo in range(1, 25):
            self.herni_pole.append(HerniPole(cislo))                # Přidání polí pro hrací plochu
        
    
    def vytvor_hraci_plochu(self):
        if self.Hrac1.barva == "Bílá":                              # Výpis pole na hrací ploše pro určení, kolik má hráč žetonů na baru
            pocet_zetonu_hrac1 = self.barec.pocet_zetonu_bila
            pocet_zetonu_hrac2 = self.barec.pocet_zetonu_cerna      
        else:
            pocet_zetonu_hrac1 = self.barec.pocet_zetonu_cerna
            pocet_zetonu_hrac2 = self.barec.pocet_zetonu_bila
        for i in range(0,24):
            self.herni_pole[i].barva_pole()                         # Nastavení barvy pole dle funkce barva_pole(), která určuje podle žetonů na daném zásobníku svou barvu

        plocha = f"""
        +------+------+------+------+------+------+-----+------+------+------+------+------+------+--------+
        |  13  |  14  |  15  |  16  |  17  |  18  | BAR |  19  |  20  |  21  |  22  |  23  |  24  |   CIL  |
        |  {self.herni_pole[12].barva}   |  {self.herni_pole[13].barva}   |  {self.herni_pole[14].barva}   |  {self.herni_pole[15].barva}   |  {self.herni_pole[16].barva}   |  {self.herni_pole[17].barva}   |     |  {self.herni_pole[18].barva}   |  {self.herni_pole[19].barva}   |  {self.herni_pole[20].barva}   |  {self.herni_pole[21].barva}   |  {self.herni_pole[22].barva}   |  {self.herni_pole[23].barva}   |        |
        |  {len(self.herni_pole[12].zasobnik)}   |  {len(self.herni_pole[13].zasobnik)}   |  {len(self.herni_pole[14].zasobnik)}   |  {len(self.herni_pole[15].zasobnik)}   |  {len(self.herni_pole[16].zasobnik)}   |  {len(self.herni_pole[17].zasobnik)}   |  {pocet_zetonu_hrac1}  |  {len(self.herni_pole[18].zasobnik)}   |  {len(self.herni_pole[19].zasobnik)}   |  {len(self.herni_pole[20].zasobnik)}   |  {len(self.herni_pole[21].zasobnik)}   |  {len(self.herni_pole[22].zasobnik)}   |  {len(self.herni_pole[23].zasobnik)}   |        | {hra.Hrac1.barva}
        +------+------+------+------+------+------+-----+------+------+------+------+------+------+--------+
        |  12  |  11  |  10  |   9  |   8  |   7  |     |   6  |   5  |   4  |   3  |   2  |   1  |        |
        |  {self.herni_pole[11].barva}   |  {self.herni_pole[10].barva}   |  {self.herni_pole[9].barva}   |  {self.herni_pole[8].barva}   |  {self.herni_pole[7].barva}   |  {self.herni_pole[6].barva}   |     |  {self.herni_pole[5].barva}   |  {self.herni_pole[4].barva}   |  {self.herni_pole[3].barva}   |  {self.herni_pole[2].barva}   |  {self.herni_pole[1].barva}   |  {self.herni_pole[0].barva}   |        |
        |  {len(self.herni_pole[11].zasobnik)}   |  {len(self.herni_pole[10].zasobnik)}   |  {len(self.herni_pole[9].zasobnik)}   |  {len(self.herni_pole[8].zasobnik)}   |  {len(self.herni_pole[7].zasobnik)}   |  {len(self.herni_pole[6].zasobnik)}   |  {pocet_zetonu_hrac2}  |  {len(self.herni_pole[5].zasobnik)}   |  {len(self.herni_pole[4].zasobnik)}   |  {len(self.herni_pole[3].zasobnik)}   |  {len(self.herni_pole[2].zasobnik)}   |  {len(self.herni_pole[1].zasobnik)}   |  {len(self.herni_pole[0].zasobnik)}   |        | {hra.Hrac2.barva}
        +------+------+------+------+------+------+-----+------+------+------+------+------+------+--------+
                                      +-----------------------------+
                                      |   Kostka 1   |   Kostka 2   |
                                      |      {self.kostka.kostka_1}       |      {self.kostka.kostka_2}       |
                                      +--------------+--------------+
                                           
        """                                                         # Výpis hrací plochy do konzole
        print(plocha)

    def priprav_hru(self):                                          # Vytvoření základního rozestavení žetonů
        for i in range(1,6):
            hra.barec.vytvor_start_bily(11)
            hra.barec.vytvor_start_bily(18)
            hra.barec.vytvor_start_cerny(12)
            hra.barec.vytvor_start_cerny(5)
        for i in range(1,4):
            hra.barec.vytvor_start_bily(16)
            hra.barec.vytvor_start_cerny(7)
        for i in range(1,3):
            hra.barec.vytvor_start_bily(0)
            hra.barec.vytvor_start_cerny(23)

    def Ulozit(self) -> None:
        data = {
            'Bily': self.bar.pocet_zetonu_bila_cil,
            'Cerny': self.bar.pocet_zetonu_cerna_cil,
            'Player1': {
                'Jmeno': self.Hrac1.jmeno,
                'Barva': self.Hrac1.barva,
                'Score': self.bar.pocet_zetonu_bila_cil,
            },
            'Player2': {
                'Jmeno': self.Hrac2.jmeno,
                'Barva': self.Hrac2.barva,
                'Score': self.bar.pocet_zetonu_cerna_cil,
            }
        }
        with open(self.file_path, 'w') as file:
            json.dump(data, file)
        print("Hra byla uložena.")

    def Nahrat(self) -> None:
        data = {
            'Bily': self.bar.pocet_zetonu_bila_cil,
            'Cerny': self.bar.pocet_zetonu_cerna_cil,
            'Player1': {
                'Jmeno': self.Hrac1.jmeno,
                'Barva': self.Hrac1.barva,
                'Score': self.bar.pocet_zetonu_bila_cil,
            },
            'Player2': {
                'Jmeno': self.Hrac2.jmeno,
                'Barva': self.Hrac2.barva,
                'Score': self.bar.pocet_zetonu_cerna_cil,
            }
        }
        with open(self.file_path, 'r') as file:
            json.load(file)
        print("Hra byla nahrána.")


class HerniPole:                                                    # Třída hracího pole/zásobníku
    def __init__(self, cislo_pole, zasobnik = None):                
        self.cislo_pole = cislo_pole
        self.zasobnik = zasobnik if zasobnik is not None else []
        if len(self.zasobnik) == 0:                                 # Nastavení barvy zásobníku podle daných podmínek
            self.barva = "N"
        elif self.zasobnik[0].barva == "Bílý":
            self.barva = "B"
        elif self.zasobnik[0].barva == "Černý":
            self.barva = "Č"
        
    def barva_pole(self):                                           # Metoda, která je volána při tvorbě a aktualizaci hracího pole, která aktualizuje barvu zásobníku
        if len(self.zasobnik) == 0:
            self.barva = "N"
        elif self.zasobnik[0].barva == "Bílý":
            self.barva = "B"
        elif self.zasobnik[0].barva == "Černý":
            self.barva = "Č"


class DvojKostka:                                                   # Třída kostky
    def __init__(self):
        self.kostka_1 = 0
        self.kostka_2 = 0

    def hod_kostkami(self):                                         # Metoda pro hod kostkami
        self.kostka_1 = rand(1, 6)
        self.kostka_2 = rand(1, 6)
        return self.kostka_1, self.kostka_2

class Bar:                                                          # Třída baru
    def __init__(self, zetony_bila = [], zetony_cerna = []):
        self.zetony_bila = []                                       # Seznam bílých žetonů na baru
        self.zetony_cerna = []                                      # Seznam černých žetonů na baru
        self.pocet_zetonu_bila = len(zetony_bila)                   # Počet bílých žetonů na baru
        self.pocet_zetonu_cerna = len(zetony_cerna)                 # Počet černých žetonů na baru
    
    def vytvor_kamen_bily(self, barva = "Bílý"):                    # Vytovření bílého kamenu na cílový zásobník v případě nahazování z baru
        kamen = HerniKamen(barva)
        cil = hra.herni_pole[int(input(""))].zasobnik
        cil.append(kamen)

    def vytvor_kamen_cerny(self, barva = "Černý"):                  # Vytovření černého kamenu na cílový zásobník v případě nahazování z baru
        kamen = HerniKamen(barva)
        cil = hra.herni_pole[int(input(""))].zasobnik
        cil.append(kamen)

    def vytvor_start_bily(self, x, barva = "Bílý"):                 # Vytvoření startovních bílých žetonů
        kamen = HerniKamen(barva)
        cil = hra.herni_pole[x].zasobnik
        cil.append(kamen)

    def vytvor_start_cerny(self, x, barva = "Černý"):               # Vytvoření startovních černých žetonů
        kamen = HerniKamen(barva)
        cil = hra.herni_pole[x].zasobnik
        cil.append(kamen)

    def vyhod_z_baru(self):                                         # Metoda, která bude sloužit pro odečtení žetonu ze seznamu zetonu z baru
        pass
        

    def pridej_do_baru(self, start = None):                         # Přidání žetonu na bar
        temp = []
        pole_start = hra.herni_pole[start - 1]
        temp.append(pole_start.zasobnik[0])
        if temp[0].barva == "Bílý":
            self.pocet_zetonu_bila.append(temp)
        elif temp[0].barva == "Černý":
            self.pocet_zetonu_cerna.append(temp)

    

class HerniKamen:                                                   # Třída herního kamene
    def __init__(self, barva):
        self.barva = barva

class Hrac:                                                         # Třída hráče
    def __init__(self, jmeno, barva):
        self.jmeno = jmeno
        self.barva = barva 
    
    def prerus_tah(self):                                           # Metoda pro přerušení kola
        if hra.token == 0:
            hra.token = 1
        else:
            hra.token = 0

class KonzolovyHrac(Hrac):                                              # Třída konzolového hráče
    def tah(self, temp= []):                                            # Metoda pohybu žetonu hráče
        if hra.presuny < 2:
            start = int(input("Zadej číslo pole, odkud vybíráš: "))     
            print("1) O počet na 1. kostce")
            print("2) O počet na 2. kostce")
            print("3) O počet na obou kostkách")
            inp = int(input("Zadej: "))
            if inp == 1:                                                # Možnost pohybu o první kostku
                cil = hra.kostka.kostka_1
            elif inp == 2:
                cil = hra.kostka.kostka_2                               # Možnost pohybu o druhou kostku
            elif inp == 3:
                cil = hra.kostka.kostka_1 + hra.kostka.kostka_2         # Možnost pohybu o součet obou kostek

            if start < 1 or start > 24 or cil < 1 or cil > 24:                  # Ošetření, aby hráč nevybral neexistující pole
                print("Neplatné číslo pole!")
                return

            pole_start = hra.herni_pole[start - 1]                              
            pole_cil = hra.herni_pole[start+cil - 1]

            if len(pole_cil.zasobnik) == 5:                                     # Ošetření, aby zásobník, na který se přidává nebyl plný
                print("Tento zásobník je již plný!")
            else:
                if len(pole_start.zasobnik) > 0:                                # Pokud je prázdný, může se na něj přidat
                    temp =[]
                    temp.append(pole_start.zasobnik[0])

                    if pole_start.zasobnik[0].barva != self.barva:              # Ošetření, aby hráč přidával na svoje nebo práždní pole
                        print("Na zadaném poli nemáte zetony vaší barvy!")
                    elif pole_cil.barva != pole_start.barva and pole_cil.barva != "N":
                        print("Na poli nejsou tvé žetony!")
                    else:
                        pole_start.zasobnik.remove(pole_start.zasobnik[0])
                        pole_cil.zasobnik.append(temp[0])
                        if inp == 1:                                            # Zde se nastavují hodnoty, podle toho co se hráč rozhodne udělat při přesunech žetonu o jednu, druhou nebo součet obou kostek
                            hra.presuny = hra.presuny + 1
                            print(hra.presuny)
                            hra.kostka.kostka_1 = 0
                        elif inp == 2:
                            hra.presuny = hra.presuny + 1
                            print(hra.presuny)
                            hra.kostka.kostka_2 = 0
                        elif inp == 3:
                            hra.presuny = 2
                            hra.kostka.kostka_1 = 0
                            hra.kostka.kostka_2 = 0
                else:
                    print("Pole ze kterého se snažíte brát, je prázdné!")
        elif hra.presuny == 2:
            print("Už jsi táhl za obě kostky!")

    def nabidka(self):                                  # Nabídka pro hráče a jeho možné akce
        print("1) Hod kostkami!")
        print("2) Pohni s kameny!")
        print("3) Zobraz plochu!")
        print("4) Ukonči tah!")
        print("5) Vyjed z baru!")
        print("6) Uložit hru")
        print("7) Nahrát hru")
        akce = int(input("Zadej akci: "))
        if akce == 1 and hra.hozeno == 0:               # Zjišťování, jakou hráč zvolil akci á různé podmínky ohledně toho jestli házel, přesouval se, apod.
            if hra.token == 0:                        
                hra.kostka.hod_kostkami()
                hra.vytvor_hraci_plochu()
                hra.hozeno = 1
            else:                                       
                hra.kostka.hod_kostkami()
                hra.vytvor_hraci_plochu()
                hra.hozeno = 1
        elif akce == 2:
            if hra.token == 0:
                hra.Hrac1.tah()
            else:
                hra.Hrac2.tah()
        elif akce == 3:
            hra.vytvor_hraci_plochu()
        elif akce == 4:
            if hra.token == 0:
                hra.Hrac1.prerus_tah()
                hra.hozeno = 0
                hra.presuny =0
            else:
                hra.Hrac2.prerus_tah()
                hra.hozeno = 0
                hra.presuny = 0
        elif akce == 5:
            hra.barec.vyhod_z_baru()
        elif akce == 6:
            hra.Ulozit
        elif akce == 7:
            hra.Nahrat

        elif hra.hozeno == 1:
            print("Už jsi házel!")
        else:
            print("Neplatná akce!")
   
            
class AiHrac(Hrac):                    # Třída AI hráče
    pass
hra = HerniDeska()                  # Vytvoření instance herní desky 
hra.priprav_hru()                   # Připravení hry
while True:                         # Herní cyklus
    hra.vytvor_hraci_plochu()
    if hra.token == 0:              # Podmínka, která kontroluje, kdo je na řadě
        hra.Hrac1.nabidka()
    elif hra.token == 1:            # To co dělá hráč, zatím pro účely testování, pouze ukončí tah
        hra.Hrac2.prerus_tah() 
    input("-----------------------------------------------------STISKNI ENTER---------------------------------------------------------------")  # Zastavení, aby si hráč mohl prohlédnout co se stalo, atd.
