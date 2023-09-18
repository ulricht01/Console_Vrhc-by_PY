import random, sys, os, json
rand = random.randint

from AiHrac import *
from KonzolovyHrac import *
from Bar import Bar
from HerniPole import *
from HerniKamen import *


class HerniDeska:
    def __init__(self):
        self.file_path = './file.json'
        check_file = os.path.isfile(self.file_path)
        self.token = rand(0,1)                                      # Vytvoření tokenu pro určování, kdo bude začínat
        self.status = True
        self.hraje_se = True
        barevny_seznam = ["Černý", "Bílý"]                          # Seznam barev hráčů 
        random.shuffle(barevny_seznam)                              # Přeházení pořadí (Kvůli random nastavení barvy)

        volba = input("Budeš hrát s hráčem (1), nebo s AI (0)?")
        if volba == "1":
            hrac1 = input("Jméno hráče 1: ")
            self.Hrac1 = KonzolovyHrac(hrac1, barevny_seznam[0], self)
            hrac2 = input("Jméno hráče 2: ")
            self.Hrac2 = KonzolovyHrac(hrac2, barevny_seznam[1], self)
        elif volba == "0":
            hrac1 = input("Jméno hráče 1: ")
            self.Hrac1 = KonzolovyHrac(hrac1, barevny_seznam[0], self)
            hrac2 = input("Jméno Ai 1: ")
            self.Hrac2 = AiHrac(hrac2, barevny_seznam[1], self)           # Základní nabídka pro tvorbu hry s hráčem/AI hráčem

        self.kostka = DvojKostka(self)
        self.barec = Bar(self)
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

    def ukonci_hru(self):
        self.status = False
    
    def vytvor_hraci_plochu(self):
        if self.Hrac1.barva == "Bílý":                              # Výpis pole na hrací ploše pro určení, kolik má hráč žetonů na baru
            self.pocet_zetonu_hrac1 = len(self.barec.zetony_bila)
            self.pocet_zetonu_hrac2 = len(self.barec.zetony_cerna)     
        else:
            self.pocet_zetonu_hrac1 = len(self.barec.zetony_cerna)
            self.pocet_zetonu_hrac2 = len(self.barec.zetony_bila)
        for i in range(0, 24):
            self.herni_pole[i].barva_pole()                         # Nastavení barvy pole dle funkce barva_pole(), která určuje podle žetonů na daném zásobníku svou barvu

        plocha = f"""
        +------+------+------+------+------+------+-----+------+------+------+------+------+------+-------+
        |  13  |  14  |  15  |  16  |  17  |  18  | BAR |  19  |  20  |  21  |  22  |  23  |  24  |  CIL  |
        |  {self.herni_pole[12].barva}   |  {self.herni_pole[13].barva}   |  {self.herni_pole[14].barva}   |  {self.herni_pole[15].barva}   |  {self.herni_pole[16].barva}   |  {self.herni_pole[17].barva}   |     |  {self.herni_pole[18].barva}   |  {self.herni_pole[19].barva}   |  {self.herni_pole[20].barva}   |  {self.herni_pole[21].barva}   |  {self.herni_pole[22].barva}   |  {self.herni_pole[23].barva}   |       |
        |  {len(self.herni_pole[12].zasobnik)}   |  {len(self.herni_pole[13].zasobnik)}   |  {len(self.herni_pole[14].zasobnik)}   |  {len(self.herni_pole[15].zasobnik)}   |  {len(self.herni_pole[16].zasobnik)}   |  {len(self.herni_pole[17].zasobnik)}   |  {len(self.barec.zetony_bila)}  |  {len(self.herni_pole[18].zasobnik)}   |  {len(self.herni_pole[19].zasobnik)}   |  {len(self.herni_pole[20].zasobnik)}   |  {len(self.herni_pole[21].zasobnik)}   |  {len(self.herni_pole[22].zasobnik)}   |  {len(self.herni_pole[23].zasobnik)}   |   {len(self.cilove_pole_bila)}   | Bílá
        +------+------+------+------+------+------+-----+------+------+------+------+------+------+-------+
        |  12  |  11  |  10  |   9  |   8  |   7  |     |   6  |   5  |   4  |   3  |   2  |   1  |       |
        |  {self.herni_pole[11].barva}   |  {self.herni_pole[10].barva}   |  {self.herni_pole[9].barva}   |  {self.herni_pole[8].barva}   |  {self.herni_pole[7].barva}   |  {self.herni_pole[6].barva}   |     |  {self.herni_pole[5].barva}   |  {self.herni_pole[4].barva}   |  {self.herni_pole[3].barva}   |  {self.herni_pole[2].barva}   |  {self.herni_pole[1].barva}   |  {self.herni_pole[0].barva}   |       |
        |  {len(self.herni_pole[11].zasobnik)}   |  {len(self.herni_pole[10].zasobnik)}   |  {len(self.herni_pole[9].zasobnik)}   |  {len(self.herni_pole[8].zasobnik)}   |  {len(self.herni_pole[7].zasobnik)}   |  {len(self.herni_pole[6].zasobnik)}   |  {len(self.barec.zetony_cerna)}  |  {len(self.herni_pole[5].zasobnik)}   |  {len(self.herni_pole[4].zasobnik)}   |  {len(self.herni_pole[3].zasobnik)}   |  {len(self.herni_pole[2].zasobnik)}   |  {len(self.herni_pole[1].zasobnik)}   |  {len(self.herni_pole[0].zasobnik)}   |   {len(self.cilove_pole_cerna)}   | Černá
        +------+------+------+------+------+------+-----+------+------+------+------+------+------+-------+
                             +-----------------------------+-----------------------------+
                             |   Kostka 1   |   Kostka 2   |   Double 1   |   Double 2   |
                             |      {self.kostka.kostka_1}       |      {self.kostka.kostka_2}       |      {self.kostka.kostka_3}       |      {self.kostka.kostka_4}       |
                             +--------------+--------------+--------------+--------------+
                                           
        """                                                         # Výpis hrací plochy do konzole
        print('---------------------------------------')                                                        
        self.vypis_hrace()
        print(plocha)

    def priprav_hru(self):                                          # Vytvoření základního rozestavení žetonů
        for i in range(1,6):
            self.barec.vytvor_start_bily(11)
            self.barec.vytvor_start_bily(18)
            self.barec.vytvor_start_cerny(12)
            self.barec.vytvor_start_cerny(5)
        for i in range(1,4):
            self.barec.vytvor_start_bily(16)
            self.barec.vytvor_start_cerny(7)
        for i in range(1,3):
            self.barec.vytvor_start_bily(0)
            self.barec.vytvor_start_cerny(23)

    def Ulozit(self):
        bar_data = {
            'zetony_bila': [[kamen.barva for kamen in pole] for pole in self.barec.zetony_bila],
            'zetony_cerna': [[kamen.barva for kamen in pole] for pole in self.barec.zetony_cerna]
        }
        data_1 = {
        'Jmeno': self.Hrac1.jmeno,
        'Barva': self.Hrac1.barva,
        'PlayerType': "KonzolovyHrac",
        'Cil': self.cilove_pole_bila,
        'Kostka_1': self.kostka.kostka_1,
        'Kostka_2': self.kostka.kostka_2,
        'Kostka_3': self.kostka.kostka_3,   
        'Kostka_4': self.kostka.kostka_4,   
        #'Bar': bar_bila_data,
        }
        data_2 = {
        'Jmeno': self.Hrac2.jmeno,
        'Barva': self.Hrac2.barva,
        'PlayerType': "KonzolovyHrac",
        'Cil': self.cilove_pole_cerna,
        'Kostka_1': self.kostka.kostka_1,
        'Kostka_2': self.kostka.kostka_2,
        'Kostka_3': self.kostka.kostka_3,   
        'Kostka_4': self.kostka.kostka_4,   
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
            json.dump(data, file, indent=4)
        print("Hra byla uložena.")

    
    def load_player_data(self, player_data):
        if player_data['PlayerType'] == "KonzolovyHrac":
            return KonzolovyHrac(player_data['Jmeno'], player_data['Barva'], self)
        elif player_data['PlayerType'] == "AiHrac":
            return AiHrac(player_data['Jmeno'], player_data['Barva'], self)
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
        self.barec.pocet_zetonu_bila = player1_data['Cil']
        self.barec.pocet_zetonu_cerna = player2_data['Cil']

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

    def rezignace_hry(self):
        if self.hraje_se:
            print("=============== KONEC HRY ===============")
            if self.token == 0:  # Pokud hráč 1 hraje, rezignoval hráč 1
                if self.Hrac1.barva == "Černý":
                    print(f"Vyhrál: {self.Hrac2.jmeno} ({self.Hrac2.barva}), Žetony na baru: {len(self.barec.zetony_bila)}, Žetony v cíli: {len(self.cilove_pole_bila)}")
                    print(f"Vzdal se: {self.Hrac1.jmeno} ({self.Hrac1.barva}), Žetony na baru: {len(self.barec.zetony_cerna)}, Žetony v cíli: {len(self.cilove_pole_cerna)}")  
                    print(f"Bar: Černá: {len(self.cilove_pole_cerna)}, Bílá: {len(self.cilove_pole_cerna)}") 
                elif self.Hrac1.barva == "Bílý":
                    print(f"Vyhrál: {self.Hrac2.jmeno} ({self.Hrac2.barva}), Žetony na baru: {len(self.barec.zetony_cerna)}, Žetony v cíli: {len(self.cilove_pole_cerna)}")  
                    print(f"Vzdal se: {self.Hrac1.jmeno} ({self.Hrac1.barva}), Žetony na baru: {len(self.barec.zetony_bila)}, Žetony v cíli: {len(self.cilove_pole_bila)}")
                    print(f"Bar: Černá: {len(self.cilove_pole_cerna)}, Bílá: {len(self.cilove_pole_cerna)}")  
                else:
                    print("CHYBA")    
            elif self.token == 1:  # Pokud hráč 2 hraje, rezignoval hráč 2
                if self.Hrac2.barva == "Černý":
                    print(f"Vyhrál: {self.Hrac1.jmeno} ({self.Hrac1.barva}), Žetony na baru: {len(self.barec.zetony_bila)}, Žetony v cíli: {len(self.cilove_pole_bila)}")
                    print(f"Vzdal se: {self.Hrac2.jmeno} ({self.Hrac2.barva}), Žetony na baru: {len(self.barec.zetony_cerna)}, Žetony v cíli: {len(self.cilove_pole_cerna)}") 
                    print(f"Bar: Černá: {len(self.cilove_pole_cerna)}, Bílá: {len(self.cilove_pole_cerna)}")      
                elif self.Hrac2.barva == "Bílý":
                    print(f"Vyhrál: {self.Hrac1.jmeno}, ({self.Hrac1.barva}), Žetony na baru: {len(self.barec.zetony_cerna)}, Žetony v cíli: {len(self.cilove_pole_cerna)}")
                    print(f"Vzdal se: {self.Hrac2.jmeno} ({self.Hrac2.barva}), Žetony na baru: {len(self.barec.zetony_bila)}, Žetony v cíli: {len(self.cilove_pole_bila)}")
                    print(f"Bar: Černá: {len(self.cilove_pole_cerna)}, Bílá: {len(self.cilove_pole_cerna)}")    
                else:
                    print("CHYBA")
            print("=========================================")
            self.ukonci_hru()
            
    def statistiky_konec_hry(self):
        print("Statistiky rezignace hry:")
        for hrac, pocet_vzdan in self.konec_hry_statistiky.items():
            print(f"{hrac}: {pocet_vzdan} vzdání")

    def vyhodnoceni(self):
        kontrola_bil = 0
        kontrola_cer = 0
        print("====== Statistika ======")
        self.Hrac1.vypis_konec()
        self.Hrac2.vypis_konec()
        for i in range(0,5):
            for zeton in self.herni_pole[i].zasobnik:
                if zeton.barva == "Bílý":
                    kontrola_bil +=1
        for i in range(18,23):
            for zeton in self.herni_pole[i].zasobnik:
                if zeton.barva == "Černý":
                    kontrola_cer +=1

        if len(self.cilove_pole_cerna) == 15 and len(self.cilove_pole_bila) == 0 and len(self.barec.zetony_bila) >= 0 or len(self.cilove_pole_cerna) == 15 and len(self.cilove_pole_bila) == 0 and kontrola_bil < 15:
            print("ČERNÁ: BACKGAMMON!")
        elif len(self.cilove_pole_bila) == 15 and len(self.cilove_pole_cerna) == 0 and len(self.barec.zetony_cerna) >= 0 or len(self.cilove_pole_bila) == 15 and len(self.cilove_pole_cerna) == 0 and kontrola_cer < 15:
            print("BÍLÁ: BACKGAMMON!")
        elif len(self.cilove_pole_cerna) == 15 and len(self.cilove_pole_bila) == 0 and kontrola_bil == 15:
            print("ČERNÁ: GAMMON!")
        elif len(self.cilove_pole_bila) == 15 and len(self.cilove_pole_cerna) == 0 and kontrola_cer == 15:
            print("BÍLÁ: GAMMON!")
        elif len(self.cilove_pole_cerna) == 15 and len(self.cilove_pole_bila) > 0:
            print("ČERNÁ: BĚŽNÁ VÝHRA!")
        elif len(self.cilove_pole_bila) == 15 and len(self.cilove_pole_cerna) > 0:
            print("BÍLÁ: BĚŽNÁ VÝHRA!")
        else:
            print("Předčasné ukončení!")
        self.ukonci_hru()