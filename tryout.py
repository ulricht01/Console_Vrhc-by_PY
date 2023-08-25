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
        self.cilove_pole_bila = []
        self.cilove_pole_cerna = []

        self.herni_pole = []                                        # Vytvoření seznamzu herního pole
        for cislo in range(1, 25):
            self.herni_pole.append(HerniPole(cislo))                # Přidání polí pro hrací plochu
        
    def vypis_hrace(self):
        print(self.Hrac1.jmeno, ' je ', self.Hrac1.barva)                      # Vypsání barev hráčů
        print(self.Hrac2.jmeno, ' je ', self.Hrac2.barva)
    
    def vytvor_hraci_plochu(self):
        if self.Hrac1.barva == "Bílý":                              # Výpis pole na hrací ploše pro určení, kolik má hráč žetonů na baru
            pocet_zetonu_hrac1 = len(self.barec.zetony_bila)
            pocet_zetonu_hrac2 = len(self.barec.zetony_cerna)     
        else:
            pocet_zetonu_hrac1 = len(self.barec.zetony_cerna)
            pocet_zetonu_hrac2 = len(self.barec.zetony_bila)
        for i in range(0,24):
            self.herni_pole[i].barva_pole()                         # Nastavení barvy pole dle funkce barva_pole(), která určuje podle žetonů na daném zásobníku svou barvu

        plocha = f"""
        +------+------+------+------+------+------+-----+------+------+------+------+------+------+-------+
        |  13  |  14  |  15  |  16  |  17  |  18  | BAR |  19  |  20  |  21  |  22  |  23  |  24  |  CIL  |
        |  {self.herni_pole[12].barva}   |  {self.herni_pole[13].barva}   |  {self.herni_pole[14].barva}   |  {self.herni_pole[15].barva}   |  {self.herni_pole[16].barva}   |  {self.herni_pole[17].barva}   |     |  {self.herni_pole[18].barva}   |  {self.herni_pole[19].barva}   |  {self.herni_pole[20].barva}   |  {self.herni_pole[21].barva}   |  {self.herni_pole[22].barva}   |  {self.herni_pole[23].barva}   |       |
        |  {len(self.herni_pole[12].zasobnik)}   |  {len(self.herni_pole[13].zasobnik)}   |  {len(self.herni_pole[14].zasobnik)}   |  {len(self.herni_pole[15].zasobnik)}   |  {len(self.herni_pole[16].zasobnik)}   |  {len(self.herni_pole[17].zasobnik)}   |  {pocet_zetonu_hrac1}  |  {len(self.herni_pole[18].zasobnik)}   |  {len(self.herni_pole[19].zasobnik)}   |  {len(self.herni_pole[20].zasobnik)}   |  {len(self.herni_pole[21].zasobnik)}   |  {len(self.herni_pole[22].zasobnik)}   |  {len(self.herni_pole[23].zasobnik)}   |   {len(self.cilove_pole_bila)}   | Bílá
        +------+------+------+------+------+------+-----+------+------+------+------+------+------+-------+
        |  12  |  11  |  10  |   9  |   8  |   7  |     |   6  |   5  |   4  |   3  |   2  |   1  |       |
        |  {self.herni_pole[11].barva}   |  {self.herni_pole[10].barva}   |  {self.herni_pole[9].barva}   |  {self.herni_pole[8].barva}   |  {self.herni_pole[7].barva}   |  {self.herni_pole[6].barva}   |     |  {self.herni_pole[5].barva}   |  {self.herni_pole[4].barva}   |  {self.herni_pole[3].barva}   |  {self.herni_pole[2].barva}   |  {self.herni_pole[1].barva}   |  {self.herni_pole[0].barva}   |       |
        |  {len(self.herni_pole[11].zasobnik)}   |  {len(self.herni_pole[10].zasobnik)}   |  {len(self.herni_pole[9].zasobnik)}   |  {len(self.herni_pole[8].zasobnik)}   |  {len(self.herni_pole[7].zasobnik)}   |  {len(self.herni_pole[6].zasobnik)}   |  {pocet_zetonu_hrac2}  |  {len(self.herni_pole[5].zasobnik)}   |  {len(self.herni_pole[4].zasobnik)}   |  {len(self.herni_pole[3].zasobnik)}   |  {len(self.herni_pole[2].zasobnik)}   |  {len(self.herni_pole[1].zasobnik)}   |  {len(self.herni_pole[0].zasobnik)}   |   {len(self.cilove_pole_cerna)}   | Černá
        +------+------+------+------+------+------+-----+------+------+------+------+------+------+-------+
                                      +-----------------------------+
                                      |   Kostka 1   |   Kostka 2   |
                                      |      {self.kostka.kostka_1}       |      {self.kostka.kostka_2}       |
                                      +--------------+--------------+
                                           
        """                                                         # Výpis hrací plochy do konzole
        print('---------------------------------------')                                                        
        self.vypis_hrace()
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

    def Ulozit(self):
        bar_data = {
            'zetony_bila': [[kamen.barva for kamen in pole] for pole in self.barec.zetony_bila],
            'zetony_cerna': [[kamen.barva for kamen in pole] for pole in self.barec.zetony_cerna]
        }
        data_1 = {
        'Jmeno': self.Hrac1.jmeno,
        'Barva': self.Hrac1.barva,
        'PlayerType': "KonzolovyHrac",
        'Score': self.barec.pocet_zetonu_bila,
        'Kostka_1': self.kostka.kostka_1,
        'Kostka_2': self.kostka.kostka_2,
        #'Bar': bar_bila_data,
        }
        data_2 = {
        'Jmeno': self.Hrac2.jmeno,
        'Barva': self.Hrac2.barva,
        'PlayerType': "KonzolovyHrac",
        'Score': self.barec.pocet_zetonu_cerna,
        'Kostka_1': self.kostka.kostka_1,
        'Kostka_2': self.kostka.kostka_2,
        #'Bar': bar_cerna_data,
        }

        herni_pole_data = []
        for pole in self.herni_pole:
            zasobnik_data = [{'barva': kamen.barva} for kamen in pole.zasobnik]
            pole_data = {
                'cislo_pole': pole.cislo_pole,
                'zasobnik': zasobnik_data,
                'barva': pole.barva,
            }
            herni_pole_data.append(pole_data)

        data = {
            'Player1': data_1,
            'Player2': data_2,
            'HerniPole': herni_pole_data,
            'Bar': bar_data

        }
                
        with open(self.file_path, 'w') as file:
            json.dump(data, file)
        print("Hra byla uložena.")

    def load_player_data(self, player_data):
        if player_data['PlayerType'] == "KonzolovyHrac":
            return KonzolovyHrac(player_data['Jmeno'], player_data['Barva'])
        elif player_data['PlayerType'] == "AiHrac":
            return AiHrac(player_data['Jmeno'], player_data['Barva'])
        else:
            return None

    def Nahrat(self):
        with open(self.file_path, 'r') as file:
            data = json.load(file)

        player1_data = data['Player1']
        player2_data = data['Player2']
        herni_pole_data = data['HerniPole']

        self.Hrac1 = self.load_player_data(player1_data)
        self.Hrac2 = self.load_player_data(player2_data)
        self.barec.pocet_zetonu_bila = player1_data['Score']
        self.barec.pocet_zetonu_cerna = player2_data['Score']

        self.kostka.kostka_1 = player1_data['Kostka_1']  # Načteme hodnotu první kostky
        self.kostka.kostka_2 = player1_data['Kostka_2']  # Načteme hodnotu druhé kostky

        bar_data = data['Bar']
        self.NacistBar(bar_data)

        for i, pole_data in enumerate(herni_pole_data):
            zasobnik_data = pole_data['zasobnik']
            zasobnik = [HerniKamen(kamen['barva']) for kamen in zasobnik_data]
            self.herni_pole[i].zasobnik = zasobnik
            self.herni_pole[i].barva = pole_data['barva']

        print("Hra byla nahrána.")

    def NacistBar(self, bar_data):
        self.barec.zetony_bila = []
        self.barec.zetony_cerna = []

        for radek in bar_data['zetony_bila']:
            radek_zetonu = []
            for barva in radek:
                kamen = HerniKamen(barva)
                radek_zetonu.append(kamen)
            self.barec.zetony_bila.append(radek_zetonu)

        for radek in bar_data['zetony_cerna']:
            radek_zetonu = []
            for barva in radek:
                kamen = HerniKamen(barva)
                radek_zetonu.append(kamen)
            self.barec.zetony_cerna.append(radek_zetonu)

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
    
    def vytvor_kamen_bily(self, x):                    # Vytovření bílého kamenu na cílový zásobník v případě nahazování z baru
        kamen = x
        cil = hra.herni_pole[int(input(""))].zasobnik
        cil = cil - 1
        cil.append(kamen)

    def vytvor_kamen_cerny(self, x):                  # Vytovření černého kamenu na cílový zásobník v případě nahazování z baru
        kamen = x
        cil = hra.herni_pole[int(input(""))-1].zasobnik
        cil = cil - 1
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
        if hra.Hrac1.barva == "Bílý" and len(self.zetony_bila) >= 1:
            x = self.zetony_bila.pop(-1)
            hra.barec.vytvor_kamen_bily(x)
        elif hra.Hrac1.barva == "Bílý" and len(self.zetony_bila) == 0:
            print("Na baru nemáš žádné žetony!")
        elif hra.Hrac1.barva == "Černý" and len(self.zetony_cerna) >= 1:
            x = self.zetony_cerna.pop(-1)
            hra.barec.vytvor_kamen_cerny(x)
        elif hra.Hrac1.barva == "Černý" and len(self.zetony_cerna) == 0:
            print(print("Na baru nemáš žádné žetony!"))

    def pridej_do_baru(self, cil = None):                         # Přidání žetonu na bar
        temp = []
        pole_cil = hra.herni_pole[cil]
        temp.append(pole_cil.zasobnik[0])
        hra.herni_pole[cil].zasobnik.pop(-1)
        if temp[0].barva == "Bílý":
            self.zetony_bila.append(temp)
            print("Do baru byl přidán bílý žeton!")
        elif temp[0].barva == "Černý":
            self.zetony_cerna.append(temp)
            print("Do baru byl přidán černý žeton!")


    

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
                if self.barva == 'Černý':
                    cil = start - hra.kostka.kostka_1
                else:
                    cil = start + hra.kostka.kostka_1
            elif inp == 2:
                if self.barva == 'Černý':
                    cil = start - hra.kostka.kostka_2
                else:
                    cil = start + hra.kostka.kostka_2                               # Možnost pohybu o druhou kostku
            elif inp == 3:
                if self.barva == 'Černý':
                    cil = start - hra.kostka.kostka_2
                else:
                    cil = start + hra.kostka.kostka_2                           # Možnost pohybu o součet obou kostek

            if self.barva == 'Černý':
                if start < 1 or start > 24 or cil < 1 or cil > 24 or cil > start:
                    print("Neplatné číslo pole!")
                    return
            else:
                if start < 1 or start > 24 or cil < 1 or cil > 24 or cil < start:
                    print("Neplatné číslo pole!")
                    return

            pole_start = hra.herni_pole[start - 1]
            pole_cil = hra.herni_pole[cil - 1]

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
                            hra.barec.pridej_do_baru(start+cil-1)
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
                        elif pole_cil.barva == pole_start.barva or pole_cil.barva == "N":
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

    def jedu_do_cile(self):
        kontrola_cerna = len(hra.herni_pole[0].zasobnik) + len(hra.herni_pole[1].zasobnik) + len(hra.herni_pole[2].zasobnik) + len(hra.herni_pole[3].zasobnik) + len(hra.herni_pole[4].zasobnik) + len(hra.herni_pole[5].zasobnik)
        vse_akt_zetony_cerna = 15 - hra.cilove_pole_cerna
        kontrola_bila = len(hra.herni_pole[18].zasobnik) + len(hra.herni_pole[19].zasobnik) + len(hra.herni_pole[20].zasobnik) + len(hra.herni_pole[21].zasobnik) + len(hra.herni_pole[22].zasobnik) + len(hra.herni_pole[23].zasobnik)
        vse_akt_zetony_bila = 15 - hra.cilove_pole_bila
        if hra.Hrac1.barva == "Černý" and kontrola_cerna == vse_akt_zetony_cerna or hra.Hrac1.barva == "Bílý" and kontrola_bila == vse_akt_zetony_bila:
            pass
        elif hra.Hrac2.barva == "Černý" and kontrola_cerna == vse_akt_zetony_cerna or hra.Hrac2.barva == "Bílý" and kontrola_bila == vse_akt_zetony_bila:
            pass

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
            hra.Ulozit()
        elif akce == 7:
            hra.Nahrat()
            

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
        print(f"Na tahu je hráč: {hra.Hrac1.jmeno} ({hra.Hrac1.barva})")
        print('------------------------')
        hra.Hrac1.nabidka()
    elif hra.token == 1:            # To co dělá hráč, zatím pro účely testování, pouze ukončí tah
        print(f"Na tahu je hráč: {hra.Hrac2.jmeno} ({hra.Hrac2.barva})")
        print('------------------------')
        hra.Hrac2.nabidka() 

    input("-----------------------------------------------------STISKNI ENTER---------------------------------------------------------------")  # Zastavení, aby si hráč mohl prohlédnout co se stalo, atd.
