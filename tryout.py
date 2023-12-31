import random, sys, os, json
rand = random.randint

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
        'Cil': self.cilove_pole_bila,
        'Kostka_1': self.kostka.kostka_1,
        'Kostka_2': self.kostka.kostka_2,
        'Kostka_3': self.kostka.kostka_3,   #zbytecnost????????
        'Kostka_4': self.kostka.kostka_4,   #zbytecnost????????
        #'Bar': bar_bila_data,
        }
        data_2 = {
        'Jmeno': self.Hrac2.jmeno,
        'Barva': self.Hrac2.barva,
        'PlayerType': "KonzolovyHrac",
        'Cil': self.cilove_pole_cerna,
        'Kostka_1': self.kostka.kostka_1,
        'Kostka_2': self.kostka.kostka_2,
        'Kostka_3': self.kostka.kostka_3,   #zbytecnost????????
        'Kostka_4': self.kostka.kostka_4,   #zbytecnost????????
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
                    print(f"Vyhrál: {self.Hrac2.jmeno} ({self.Hrac2.barva}), Žetony na baru: {len(hra.barec.zetony_bila)}, Žetony v cíli: {len(self.cilove_pole_bila)}")
                    print(f"Vzdal se: {self.Hrac1.jmeno} ({self.Hrac1.barva}), Žetony na baru: {len(hra.barec.zetony_cerna)}, Žetony v cíli: {len(self.cilove_pole_cerna)}")  
                    print(f"Bar: Černá: {len(self.cilove_pole_cerna)}, Bílá: {len(self.cilove_pole_cerna)}") 
                elif self.Hrac1.barva == "Bílý":
                    print(f"Vyhrál: {self.Hrac2.jmeno} ({self.Hrac2.barva}), Žetony na baru: {len(hra.barec.zetony_cerna)}, Žetony v cíli: {len(self.cilove_pole_cerna)}")  
                    print(f"Vzdal se: {self.Hrac1.jmeno} ({self.Hrac1.barva}), Žetony na baru: {len(hra.barec.zetony_bila)}, Žetony v cíli: {len(self.cilove_pole_bila)}")
                    print(f"Bar: Černá: {len(self.cilove_pole_cerna)}, Bílá: {len(self.cilove_pole_cerna)}")  
                else:
                    print("CHYBA")    
            elif self.token == 1:  # Pokud hráč 2 hraje, rezignoval hráč 2
                if self.Hrac2.barva == "Černý":
                    print(f"Vyhrál: {self.Hrac1.jmeno} ({self.Hrac1.barva}), Žetony na baru: {len(hra.barec.zetony_bila)}, Žetony v cíli: {len(self.cilove_pole_bila)}")
                    print(f"Vzdal se: {self.Hrac2.jmeno} ({self.Hrac2.barva}), Žetony na baru: {len(hra.barec.zetony_cerna)}, Žetony v cíli: {len(self.cilove_pole_cerna)}") 
                    print(f"Bar: Černá: {len(self.cilove_pole_cerna)}, Bílá: {len(self.cilove_pole_cerna)}")      
                elif self.Hrac2.barva == "Bílý":
                    print(f"Vyhrál: {self.Hrac1.jmeno}, ({self.Hrac1.barva}), Žetony na baru: {len(hra.barec.zetony_cerna)}, Žetony v cíli: {len(self.cilove_pole_cerna)}")
                    print(f"Vzdal se: {self.Hrac2.jmeno} ({self.Hrac2.barva}), Žetony na baru: {len(hra.barec.zetony_bila)}, Žetony v cíli: {len(self.cilove_pole_bila)}")
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
        hra.Hrac1.vypis_konec()
        hra.Hrac2.vypis_konec()
        for i in range(0,5):
            for zeton in hra.herni_pole[i].zasobnik:
                if zeton.barva == "Bílý":
                    kontrola_bil +=1
        for i in range(18,23):
            for zeton in hra.herni_pole[i].zasobnik:
                if zeton.barva == "Černý":
                    kontrola_cer +=1

        if len(hra.cilove_pole_cerna) == 15 and len(hra.cilove_pole_bila) == 0 and len(hra.barec.zetony_bila) >= 0 or len(hra.cilove_pole_cerna) == 15 and len(hra.cilove_pole_bila) == 0 and kontrola_bil < 15:
            print("ČERNÁ: BACKGAMMON!")
        elif len(hra.cilove_pole_bila) == 15 and len(hra.cilove_pole_cerna) == 0 and len(hra.barec.zetony_cerna) >= 0 or len(hra.cilove_pole_bila) == 15 and len(hra.cilove_pole_cerna) == 0 and kontrola_cer < 15:
            print("BÍLÁ: BACKGAMMON!")
        elif len(hra.cilove_pole_cerna) == 15 and len(hra.cilove_pole_bila) == 0 and kontrola_bil == 15:
            print("ČERNÁ: GAMMON!")
        elif len(hra.cilove_pole_bila) == 15 and len(hra.cilove_pole_cerna) == 0 and kontrola_cer == 15:
            print("BÍLÁ: GAMMON!")
        elif len(hra.cilove_pole_cerna) == 15 and len(hra.cilove_pole_bila) > 0:
            print("ČERNÁ: BĚŽNÁ VÝHRA!")
        elif len(hra.cilove_pole_bila) == 15 and len(hra.cilove_pole_cerna) > 0:
            print("BÍLÁ: BĚŽNÁ VÝHRA!")
        else:
            print("Předčasné ukončení!")
        hra.ukonci_hru()
        
        
         
    

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
        self.kostka_3 = 0
        self.kostka_4 = 0

    def hod_kostkami(self):                                         # Metoda pro hod kostkami
        if hra.hozeno == 0:
            self.kostka_1 = rand(1, 6)
            self.kostka_2 = rand(1, 6)
            if self.kostka_1 == self.kostka_2:
                self.kostka_3 = self.kostka_1
                self.kostka_4 = self.kostka_2
                hra.hozeno = 1
                self.double = 2
                return self.kostka_1, self.kostka_2, self.kostka_3, self.kostka_4
            else:
                hra.hozeno = 1
                self.double = 0
                return self.kostka_1, self.kostka_2
        else:
            print("Už jsi házel!")
        
    def vynuluj(self):
        self.kostka_1 = 0
        self.kostka_2 = 0
        self.kostka_3 = 0
        self.kostka_4 = 0

class Bar:                                                          # Třída baru
    def __init__(self, zetony_bila = [], zetony_cerna = []):
        self.zetony_bila = []                                       # Seznam bílých žetonů na baru
        self.zetony_cerna = []                                      # Seznam černých žetonů na baru
        self.pocet_zetonu_bila = len(zetony_bila)                   # Počet bílých žetonů na baru
        self.pocet_zetonu_cerna = len(zetony_cerna)                 # Počet černých žetonů na baru

    def vyjeti_z_baru(self, x, barva):                    # Vytovření bílého kamenu na cílový zásobník v případě nahazování z baru
        kostka = 0
        kamen = x
        print(f" Kostka 1: {hra.kostka.kostka_1} \n Kostka 2: {hra.kostka.kostka_2} \n Kostka 3: {hra.kostka.kostka_3} \n Kostka 4: {hra.kostka.kostka_4}")
        inp = int(input("Zadej kterou kostkou chceš vyjet: "))
        if inp == 1:
            kostka = hra.kostka.kostka_1
            if barva == "Bílý":
                cil = hra.herni_pole[kostka-1]
                if cil.barva == "B" or len(cil.zasobnik) == 0:
                    cil.zasobnik.append(kamen)
                    hra.kostka.kostka_1 = 0
                else:
                    print("Pole je obsazené!")
            elif barva == "Černý":
                cil = hra.herni_pole[23 - kostka -1]
                if cil.barva == "Č" or len(cil.zasobnik) == 0:
                    cil.zasobnik.append(kamen)
                    hra.kostka.kostka_1 = 0
                else:
                    print("Pole je obsazené!")
        elif inp == 2:
            kostka = hra.kostka.kostka_2
            if barva == "Bílý":
                cil = hra.herni_pole[kostka-1]
                if cil.barva == "B" or len(cil.zasobnik) == 0:
                    cil.zasobnik.append(kamen)
                    hra.kostka.kostka_2 = 0
                else:
                    print("Pole je obsazené!")
            elif barva == "Černý":
                cil = hra.herni_pole[23 - kostka -1]
                if cil.barva == "Č" or len(cil.zasobnik) == 0:
                    cil.zasobnik.append(kamen)
                    hra.kostka.kostka_2 = 0
                else:
                    print("Pole je obsazené!")
        elif inp == 3:
            kostka = hra.kostka.kostka_3
            if barva == "Bílý":
                cil = hra.herni_pole[kostka-1]
                if cil.barva == "B" or len(cil.zasobnik) == 0:
                    cil.zasobnik.append(kamen)
                    hra.kostka.kostka_3 = 0
                else:
                    print("Pole je obsazené!")
            elif barva == "Černý":
                cil = hra.herni_pole[23 - kostka -1]
                if cil.barva == "Č" or len(cil.zasobnik) == 0:
                    cil.zasobnik.append(kamen)
                    hra.kostka.kostka_3 = 0
                else:
                    print("Pole je obsazené!")
        elif inp == 4:
            kostka = hra.kostka.kostka_4
            if barva == "Bílý":
                cil = hra.herni_pole[kostka-1]
                if cil.barva == "B" or len(cil.zasobnik) == 0:
                    cil.zasobnik.append(kamen)
                    hra.kostka.kostka_4 = 0
                else:
                    print("Pole je obsazené!")
            elif barva == "Černý":
                cil = hra.herni_pole[23 - kostka -1].zasobnik
                if cil.barva == "Č" or len(cil.zasobnik) == 0:
                    cil.zasobnik.append(kamen)
                    hra.kostka.kostka_4 = 0
                else:
                    print("Pole je obsazené!")
    
    def vyjeti_z_baru_ai(self, x, barva):                    # Vytovření bílého kamenu na cílový zásobník v případě nahazování z baru
        kostka = 0
        kamen = x
        if hra.kostka.double == 2:
            inp = rand(1,4)
        else:
            inp = rand(1,2)
        if inp == 1:
            kostka = hra.kostka.kostka_1
            if barva == "Bílý":
                cil = hra.herni_pole[kostka-1]
                if cil.barva == "B" or len(cil.zasobnik) == 0:
                    cil.zasobnik.append(kamen)
                    hra.kostka.kostka_1 = 0
                else:
                    print("Pole je obsazené!")
            elif barva == "Černý":
                cil = hra.herni_pole[23 - kostka -1]
                if cil.barva == "Č" or len(cil.zasobnik) == 0:
                    cil.zasobnik.append(kamen)
                    hra.kostka.kostka_1 = 0
                else:
                    print("Pole je obsazené!")
        elif inp == 2:
            kostka = hra.kostka.kostka_2
            if barva == "Bílý":
                cil = hra.herni_pole[kostka-1]
                if cil.barva == "B" or len(cil.zasobnik) == 0:
                    cil.zasobnik.append(kamen)
                    hra.kostka.kostka_2 = 0
                else:
                    print("Pole je obsazené!")
            elif barva == "Černý":
                cil = hra.herni_pole[23 - kostka -1]
                if cil.barva == "Č" or len(cil.zasobnik) == 0:
                    cil.zasobnik.append(kamen)
                    hra.kostka.kostka_2 = 0
                else:
                    print("Pole je obsazené!")
        elif inp == 3:
            kostka = hra.kostka.kostka_3
            if barva == "Bílý":
                cil = hra.herni_pole[kostka-1]
                if cil.barva == "B" or len(cil.zasobnik) == 0:
                    cil.zasobnik.append(kamen)
                    hra.kostka.kostka_3 = 0
                else:
                    print("Pole je obsazené!")
            elif barva == "Černý":
                cil = hra.herni_pole[23 - kostka -1]
                if cil.barva == "Č" or len(cil.zasobnik) == 0:
                    cil.zasobnik.append(kamen)
                    hra.kostka.kostka_3 = 0
                else:
                    print("Pole je obsazené!")
        elif inp == 4:
            kostka = hra.kostka.kostka_4
            if barva == "Bílý":
                cil = hra.herni_pole[kostka-1]
                if cil.barva == "B" or len(cil.zasobnik) == 0:
                    cil.zasobnik.append(kamen)
                    hra.kostka.kostka_4 = 0
                else:
                    print("Pole je obsazené!")
            elif barva == "Černý":
                cil = hra.herni_pole[23 - kostka -1].zasobnik
                if cil.barva == "Č" or len(cil.zasobnik) == 0:
                    cil.zasobnik.append(kamen)
                    hra.kostka.kostka_4 = 0
                else:
                    print("Pole je obsazené!")

    def vytvor_start_bily(self, x, barva = "Bílý"):                 # Vytvoření startovních bílých žetonů
        kamen = HerniKamen(barva)
        cil = hra.herni_pole[x].zasobnik
        cil.append(kamen)

    def vytvor_start_cerny(self, x, barva = "Černý"):               # Vytvoření startovních černých žetonů
        kamen = HerniKamen(barva)
        cil = hra.herni_pole[x].zasobnik
        cil.append(kamen)

    def pridej_do_baru(self, cil):                         # Přidání žetonu na bar
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

    def kontrola_pohybu(self):
        self.valid_moves = 0
        if self.barva == "Bílý":
                for pole in hra.herni_pole:
                    if pole.cislo_pole + hra.kostka.kostka_1 <= 24 and pole.barva == "B" and hra.herni_pole[pole.cislo_pole + hra.kostka.kostka_1 - 1].barva != "Č" and hra.kostka.kostka_1 != 0 and len(hra.herni_pole[pole.cislo_pole + hra.kostka.kostka_1 - 1].zasobnik) < 5 or \
                       pole.cislo_pole + hra.kostka.kostka_1 <= 24 and pole.barva == "B" and hra.herni_pole[pole.cislo_pole + hra.kostka.kostka_1 - 1].barva == "Č" and len(hra.herni_pole[pole.cislo_pole + hra.kostka.kostka_1 - 1].zasobnik) == 1 and hra.kostka.kostka_1 != 0:
                        print(f"{pole.cislo_pole}->{pole.cislo_pole + hra.kostka.kostka_1}")
                        self.valid_moves += 1
                    if pole.cislo_pole + hra.kostka.kostka_2 <= 24 and pole.barva == "B" and hra.herni_pole[pole.cislo_pole + hra.kostka.kostka_2 - 1].barva != "Č" and hra.kostka.kostka_2 != 0 and len(hra.herni_pole[pole.cislo_pole + hra.kostka.kostka_2 - 1].zasobnik) < 5 or \
                       pole.cislo_pole + hra.kostka.kostka_2 <= 24 and pole.barva == "B" and hra.herni_pole[pole.cislo_pole + hra.kostka.kostka_2 - 1].barva == "Č" and len(hra.herni_pole[pole.cislo_pole + hra.kostka.kostka_2 - 1].zasobnik) == 1 and hra.kostka.kostka_2 != 0:
                        print(f"{pole.cislo_pole}->{pole.cislo_pole + hra.kostka.kostka_2}")
                        self.valid_moves += 1
                    if pole.cislo_pole + hra.kostka.kostka_3 <= 24 and pole.barva == "B" and hra.herni_pole[pole.cislo_pole + hra.kostka.kostka_3 - 1].barva != "Č" and hra.kostka.kostka_3 != 0 and len(hra.herni_pole[pole.cislo_pole + hra.kostka.kostka_3 - 1].zasobnik) < 5 or \
                       pole.cislo_pole + hra.kostka.kostka_3 <= 24 and pole.barva == "B" and hra.herni_pole[pole.cislo_pole + hra.kostka.kostka_3 - 1].barva == "Č" and len(hra.herni_pole[pole.cislo_pole + hra.kostka.kostka_3 - 1].zasobnik) == 1 and hra.kostka.kostka_3 != 0:
                        print(f"{pole.cislo_pole}->{pole.cislo_pole + hra.kostka.kostka_3}")
                        self.valid_moves += 1
                    if pole.cislo_pole + hra.kostka.kostka_4 <= 24 and pole.barva == "B" and hra.herni_pole[pole.cislo_pole + hra.kostka.kostka_4 - 1].barva != "Č" and hra.kostka.kostka_4 != 0 and len(hra.herni_pole[pole.cislo_pole + hra.kostka.kostka_4 - 1].zasobnik) < 5 or \
                       pole.cislo_pole + hra.kostka.kostka_4 <= 24 and pole.barva == "B" and hra.herni_pole[pole.cislo_pole + hra.kostka.kostka_4 - 1].barva == "Č" and len(hra.herni_pole[pole.cislo_pole + hra.kostka.kostka_4 - 1].zasobnik) == 1 and hra.kostka.kostka_4 != 0:
                        print(f"{pole.cislo_pole}->{pole.cislo_pole + hra.kostka.kostka_4}")
                        self.valid_moves += 1
                return self.valid_moves
                       
        if self.barva == "Černý":
                for pole in hra.herni_pole:
                    if pole.cislo_pole - hra.kostka.kostka_1 >= 1 and pole.barva == "Č" and hra.herni_pole[pole.cislo_pole - hra.kostka.kostka_1 - 1].barva != "B" and hra.kostka.kostka_1 != 0 and len(hra.herni_pole[pole.cislo_pole - hra.kostka.kostka_1 - 1].zasobnik) < 5 or \
                       pole.cislo_pole - hra.kostka.kostka_1 >= 1 and pole.barva == "Č" and hra.herni_pole[pole.cislo_pole - hra.kostka.kostka_1 - 1].barva == "B" and len(hra.herni_pole[pole.cislo_pole - hra.kostka.kostka_1 - 1].zasobnik) == 1 and hra.kostka.kostka_1 != 0:
                        print(f"{pole.cislo_pole}->{pole.cislo_pole - hra.kostka.kostka_1}")
                        self.valid_moves += 1
                    if pole.cislo_pole - hra.kostka.kostka_2 >= 1 and pole.barva == "Č" and hra.herni_pole[pole.cislo_pole - hra.kostka.kostka_2 - 1].barva != "B" and hra.kostka.kostka_2 != 0 and len(hra.herni_pole[pole.cislo_pole - hra.kostka.kostka_2 - 1].zasobnik) < 5 or \
                       pole.cislo_pole - hra.kostka.kostka_2 >= 1 and pole.barva == "Č" and hra.herni_pole[pole.cislo_pole - hra.kostka.kostka_2 - 1].barva == "B" and len(hra.herni_pole[pole.cislo_pole - hra.kostka.kostka_2 - 1].zasobnik) == 1 and hra.kostka.kostka_2 != 0:
                        print(f"{pole.cislo_pole}->{pole.cislo_pole - hra.kostka.kostka_2}")
                        self.valid_moves += 1
                    if pole.cislo_pole - hra.kostka.kostka_3 >= 1 and pole.barva == "Č" and hra.herni_pole[pole.cislo_pole - hra.kostka.kostka_3 - 1].barva != "B" and hra.kostka.kostka_3 != 0 and len(hra.herni_pole[pole.cislo_pole - hra.kostka.kostka_3 - 1].zasobnik) < 5 or \
                       pole.cislo_pole - hra.kostka.kostka_3 >= 1 and pole.barva == "Č" and hra.herni_pole[pole.cislo_pole - hra.kostka.kostka_3 - 1].barva == "B" and len(hra.herni_pole[pole.cislo_pole - hra.kostka.kostka_3 - 1].zasobnik) == 1 and hra.kostka.kostka_3 != 0:
                        print(f"{pole.cislo_pole}->{pole.cislo_pole - hra.kostka.kostka_3}")
                        self.valid_moves += 1
                    if pole.cislo_pole - hra.kostka.kostka_4 >= 1 and pole.barva == "Č" and hra.herni_pole[pole.cislo_pole - hra.kostka.kostka_4 - 1].barva != "B" and hra.kostka.kostka_4 != 0 and len(hra.herni_pole[pole.cislo_pole - hra.kostka.kostka_4 - 1].zasobnik) < 5 or \
                       pole.cislo_pole - hra.kostka.kostka_4 >= 1 and pole.barva == "Č" and hra.herni_pole[pole.cislo_pole - hra.kostka.kostka_4 - 1].barva == "B" and len(hra.herni_pole[pole.cislo_pole - hra.kostka.kostka_4 - 1].zasobnik) == 1 and hra.kostka.kostka_4 != 0:
                        print(f"{pole.cislo_pole}->{pole.cislo_pole - hra.kostka.kostka_4}")
                        self.valid_moves += 1
                return self.valid_moves
        
    def prerus_tah(self):                                           # Metoda pro přerušení kola
        if hra.token == 0:
            self.kontrola_pohybu()
            if self.valid_moves == 0 and hra.hozeno == 1 or self.valid_moves > 0 and hra.kostka.kostka_1 == 0 and hra.kostka.kostka_2 == 0 and hra.kostka.kostka_3 == 0 and hra.kostka.kostka_4 == 0:
                hra.token = 1
                hra.kostka.vynuluj()
                hra.hozeno = 0
                hra.presuny =0
            else:
                print("Stále můžeš táhnout!")
        else:
            self.kontrola_pohybu()
            if self.valid_moves == 0 and hra.hozeno == 1 or self.valid_moves > 0 and hra.kostka.kostka_1 == 0 and hra.kostka.kostka_2 == 0 and hra.kostka.kostka_3 == 0 and hra.kostka.kostka_4 == 0 and hra.hozeno == 1:
                hra.token = 0
                hra.kostka.vynuluj()
                hra.hozeno = 0
                hra.presuny =0
            else:
                print("Stále můžeš táhnout!")

    def vypis_konec(self):
        i = 0
        pocet_ve_hre = 0
        jmeno = self.jmeno
        barva = self.barva
        if self.barva == "Bílý":
            pocet_na_baru = len(hra.barec.zetony_bila)
            cilove_pole = len(hra.cilove_pole_bila)
            for i in range(0, 24):
                for zeton in hra.herni_pole[i].zasobnik:
                    if zeton.barva == "Bílý":
                        pocet_ve_hre += 1
                        i+=1
        elif self.barva == "Černý":
            pocet_na_baru = len(hra.barec.zetony_cerna)
            cilove_pole = len(hra.cilove_pole_cerna)
            for i in range(0, 24):
                for zeton in hra.herni_pole[i].zasobnik:
                    if zeton.barva == "Černý":
                        pocet_ve_hre += 1
                        i+=1

        print(f"{barva} hráč {jmeno}| Žetony na baru: {pocet_na_baru} | Žetony v cíli: {cilove_pole} | Žetony ve hře: {pocet_ve_hre}")

class KonzolovyHrac(Hrac):              # Třída konzolového hráče
    def __init__(self, jmeno, barva):
        super().__init__(jmeno, barva)

    def tah(self, temp= []):                                            # Metoda pohybu žetonu hráče
        if hra.presuny < 2 and self.barva == "Černý" and len(hra.barec.zetony_cerna) == 0 and hra.hozeno == 1 and hra.kostka.double == 0 or hra.presuny < 2 and self.barva == "Bílý" and len(hra.barec.zetony_bila) == 0 and hra.hozeno == 1 and hra.kostka.double == 0 or \
           hra.presuny <= 2 and self.barva == "Černý" and len(hra.barec.zetony_cerna) == 0 and hra.hozeno == 1 and hra.kostka.double > 0 or hra.presuny <= 2 and self.barva == "Bílý" and len(hra.barec.zetony_bila) == 0 and hra.hozeno == 1 and hra.kostka.double > 0:
            print("Tvé možné pohyby jsou: ")
            
            self.kontrola_pohybu()

            start = int(input("Zadej číslo pole, odkud vybíráš: "))
            if hra.kostka.kostka_1 != hra.kostka.kostka_2:     
                print("1) O počet na 1. kostce")
                print("2) O počet na 2. kostce")
            elif hra.kostka.kostka_3 != 0 or hra.kostka.kostka_4 !=0:
                print("1) O počet na 1. kostce")
                print("2) O počet na 2. kostce")
                print("3) O počet na 1. double")
                print("4) O počet na 2. double")
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
            elif inp == 3 and hra.kostka.kostka_1 == hra.kostka.kostka_2:
                if self.barva == 'Černý':
                    cil = start - hra.kostka.kostka_3
                else:
                    cil = start + hra.kostka.kostka_3                          # Možnost pohybu o součet obou kostek
            elif inp == 4 and hra.kostka.kostka_1 == hra.kostka.kostka_2:
                if self.barva == 'Černý':
                    cil = start - hra.kostka.kostka_4
                else:
                    cil = start + hra.kostka.kostka_4
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

            pole_start = hra.herni_pole[start - 1]
            pole_cil = hra.herni_pole[cil - 1]
            
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
                            hra.barec.pridej_do_baru(vyhazovac)
                            pole_start.zasobnik.remove(pole_start.zasobnik[0])
                            pole_cil.zasobnik.append(temp[0])
                            if inp == 1:                                            # Zde se nastavují hodnoty, podle toho co se hráč rozhodne udělat při přesunech žetonu o jednu, druhou nebo součet obou kostek
                                hra.presuny = hra.presuny + 1
                                hra.kostka.kostka_1 = 0
                            elif inp == 2:
                                hra.presuny = hra.presuny + 1
                                hra.kostka.kostka_2 = 0
                            elif inp == 3:
                                hra.kostka.kostka_3 = 0
                                hra.kostka.double -= 1
                            elif inp == 4:
                                hra.kostka.kostka_4 = 0
                                hra.kostka.double -= 1
                        elif pole_cil.barva == pole_start.barva or pole_cil.barva == "N":
                            pole_start.zasobnik.remove(pole_start.zasobnik[0])
                            pole_cil.zasobnik.append(temp[0])
                            if inp == 1:                                            # Zde se nastavují hodnoty, podle toho co se hráč rozhodne udělat při přesunech žetonu o jednu, druhou nebo součet obou kostek
                                hra.presuny = hra.presuny + 1
                                hra.kostka.kostka_1 = 0
                            elif inp == 2:
                                hra.presuny = hra.presuny + 1
                                hra.kostka.kostka_2 = 0
                            elif inp == 3:
                                hra.kostka.kostka_3 = 0
                                hra.kostka.double -= 1
                            elif inp == 4:
                                hra.kostka.kostka_4 = 0
                                hra.kostka.double -= 1

                else:
                    print("Pole ze kterého se snažíte brát, je prázdné!")
        elif hra.presuny == 2:
            print("Už jsi táhl za obě kostky!")
        elif hra.hozeno == 0:
            print("Nejdřív si hoď!")
        elif self.barva == "Černý" and len(hra.barec.zetony_cerna) > 0 or self.barva == "Bílý" and len(hra.barec.zetony_bila) >0:
            print("Nejdřív vyjeď z baru!")

    def jedu_do_cile(self):
        kontrola_cerna = 0
        kontrola_bila = 0
        for i in range(6):
            for objekt in hra.herni_pole[i].zasobnik:
                if objekt.barva == "Černý":
                    kontrola_cerna += 1

        for j in range(18,23):
            for objekt in hra.herni_pole[j].zasobnik:
                if objekt.barva == "Bílý":
                    kontrola_bila += 1

        vse_akt_zetony_cerna = 15 - len(hra.cilove_pole_cerna)
        vse_akt_zetony_bila = 15 - len(hra.cilove_pole_bila)
        
        if self.barva == "Černý" and kontrola_cerna == vse_akt_zetony_cerna or self.barva == "Bílý" and kontrola_bila == vse_akt_zetony_bila:
            if hra.presuny < 2:
                start = int(input("Zadej číslo pole, odkud vybíráš: "))
                if hra.kostka.kostka_1 != hra.kostka.kostka_2:     
                    print("1) O počet na 1. kostce")
                    print("2) O počet na 2. kostce")
                elif hra.kostka.kostka_1 == hra.kostka.kostka_2:
                    print("1) O počet na 1. kostce")
                    print("2) O počet na 2. kostce")
                    print("3) O počet na 1. double")
                    print("4) O počet na 2. double")
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
                elif inp == 3 and hra.kostka.kostka_1 == hra.kostka.kostka_2:
                    if self.barva == 'Černý':
                        cil = start - hra.kostka.kostka_3
                    else:
                        cil = start + hra.kostka.kostka_3                          # Možnost pohybu o součet obou kostek
                elif inp == 4 and hra.kostka.kostka_1 == hra.kostka.kostka_2:
                    if self.barva == 'Černý':
                        cil = start - hra.kostka.kostka_4
                    else:
                        cil = start + hra.kostka.kostka_4
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

                pole_start = hra.herni_pole[start - 1]
                if self.barva == "Černý":
                    pole_cil = hra.cilove_pole_cerna
                elif self.barva == "Bílý":
                    pole_cil = hra.cilove_pole_bila

                if cil == 0 and self.barva == "Černý" or cil == 25 and self.barva == "Bílý":                                     # Ošetření, aby zásobník, na který se přidává nebyl plný
                    temp =[]
                    temp.append(pole_start.zasobnik[0])
                    pole_cil.append(temp[0])
                    pole_start.zasobnik.remove(pole_start.zasobnik[0])
                    if inp == 1:                                            # Zde se nastavují hodnoty, podle toho co se hráč rozhodne udělat při přesunech žetonu o jednu, druhou nebo součet obou kostek
                        hra.presuny = hra.presuny + 1
                        hra.kostka.kostka_1 = 0
                    elif inp == 2:
                        hra.presuny = hra.presuny + 1
                        hra.kostka.kostka_2 = 0
                    elif inp == 3:
                        hra.kostka.kostka_3 = 0
                    elif inp == 4:
                        hra.kostka.kostka_4 = 0
                else:
                    print(cil)
                    print("Něco se pokazilo")

            elif hra.presuny == 2:
                print("Už jsi táhl za obě kostky!")
        else:
            print("Nemáš všechny žetony na posledních polích!")

    def vyhod_z_baru(self):                                       
        if self.barva == "Bílý" and len(hra.barec.zetony_bila) >= 1:
            if len(hra.barec.zetony_bila) >= 1:
                x = hra.barec.zetony_bila.pop(-1)[0]
                hra.barec.vyjeti_z_baru(x, "Bílý")
            else:
                print("Na baru nemáš žádné žetony!")
        elif self.barva == "Černý" and len(hra.barec.zetony_cerna) >= 1:
            if len(hra.barec.zetony_cerna) >= 1:
                x = hra.barec.zetony_cerna.pop(-1)[0]
                hra.barec.vyjeti_z_baru(x, "Černý")
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
            
            akce = int(input("Zadej akci: "))
            if akce == 1 and hra.hozeno == 0:               # Zjišťování, jakou hráč zvolil akci á různé podmínky ohledně toho jestli házel, přesouval se, apod.
                if hra.token == 0:                        
                    hra.kostka.hod_kostkami()
                    hra.vytvor_hraci_plochu()
                    self.kontrola_pohybu()
                    if hra.Hrac1.valid_moves == 0 and hra.token == 0:
                        hra.token = 1
                        hra.kostka.vynuluj()
                    else:
                        hra.hozeno = 1
                else:                                       
                    hra.kostka.hod_kostkami()
                    hra.vytvor_hraci_plochu()
                    self.kontrola_pohybu()
                    if hra.Hrac2.valid_moves == 0 and hra.token == 1:
                        hra.token = 0
                        hra.kostka.vynuluj()
                    else:
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
                else:
                    hra.Hrac2.prerus_tah()
            elif akce == 5:
                if hra.token == 0:
                    hra.Hrac1.vyhod_z_baru()
                elif hra.token == 1:
                    hra.Hrac2.vyhod_z_baru()
            elif akce == 6:
                if hra.token == 0:
                    hra.Hrac1.jedu_do_cile()
                else:
                    hra.Hrac2.jedu_do_cile()
            elif akce == 7:
                hra.rezignace_hry()
            elif akce == 8:
                print("1) Uložit hru")
                print("2) Nahrát hru")
                print("3) Ukončí hru")
                akce_2 = int(input("Zadej svou akci:"))
                if akce_2 == 1:
                    hra.Ulozit()
                elif akce_2 == 2:
                    hra.Nahrat()
                elif akce_2 == 3:
                    hra.vyhodnoceni()
            elif hra.hozeno == 1 and akce ==1:
                print("Už jsi házel!")
            else:
                print("Neplatná akce!")

class AiHrac(Hrac):
    def __init__(self, jmeno, barva):
        super().__init__(jmeno, barva)
        self.kontrola_bila = 0
        self.kontrola_cerna = 0

    def tah(self, temp=[]):
        start = 0
        start_pol = 0
        pohyby_start = []
        if hra.presuny < 2 and self.barva == "Černý" and len(hra.barec.zetony_cerna) == 0 and hra.hozeno == 1 and hra.kostka.double == 0 or hra.presuny < 2 and self.barva == "Bílý" and len(hra.barec.zetony_bila) == 0 and hra.hozeno == 1 and hra.kostka.double == 0 or \
           hra.presuny <= 2 and self.barva == "Černý" and len(hra.barec.zetony_cerna) == 0 and hra.hozeno == 1 and hra.kostka.double > 0 or hra.presuny <= 2 and self.barva == "Bílý" and len(hra.barec.zetony_bila) == 0 and hra.hozeno == 1 and hra.kostka.double > 0:
            print("Tvé možné pohyby jsou: ")
            
            self.kontrola_pohybu()
            if self.barva == "Bílý":
                for pole in hra.herni_pole:
                    if pole.cislo_pole + hra.kostka.kostka_1 <= 24 and pole.barva == "B" and hra.herni_pole[pole.cislo_pole + hra.kostka.kostka_1 - 1].barva != "Č" and hra.kostka.kostka_1 != 0 and len(hra.herni_pole[pole.cislo_pole + hra.kostka.kostka_1 - 1].zasobnik) < 5 or \
                       pole.cislo_pole + hra.kostka.kostka_1 <= 24 and pole.barva == "B" and hra.herni_pole[pole.cislo_pole + hra.kostka.kostka_1 - 1].barva == "Č" and len(hra.herni_pole[pole.cislo_pole + hra.kostka.kostka_1 - 1].zasobnik) == 1 and hra.kostka.kostka_1 != 0:
                        start = pole.cislo_pole
                        pohyby_start.append(start)
                    elif pole.cislo_pole + hra.kostka.kostka_2 <= 24 and pole.barva == "B" and hra.herni_pole[pole.cislo_pole + hra.kostka.kostka_2 - 1].barva != "Č" and hra.kostka.kostka_2 != 0 and len(hra.herni_pole[pole.cislo_pole + hra.kostka.kostka_2 - 1].zasobnik) < 5 or \
                       pole.cislo_pole + hra.kostka.kostka_2 <= 24 and pole.barva == "B" and hra.herni_pole[pole.cislo_pole + hra.kostka.kostka_2 - 1].barva == "Č" and len(hra.herni_pole[pole.cislo_pole + hra.kostka.kostka_2 - 1].zasobnik) == 1 and hra.kostka.kostka_2 != 0:
                        start = pole.cislo_pole
                        pohyby_start.append(start)

                    elif pole.cislo_pole + hra.kostka.kostka_3 <= 24 and pole.barva == "B" and hra.herni_pole[pole.cislo_pole + hra.kostka.kostka_3 - 1].barva != "Č" and hra.kostka.kostka_3 != 0 and len(hra.herni_pole[pole.cislo_pole + hra.kostka.kostka_3 - 1].zasobnik) < 5 or \
                       pole.cislo_pole + hra.kostka.kostka_3 <= 24 and pole.barva == "B" and hra.herni_pole[pole.cislo_pole + hra.kostka.kostka_3 - 1].barva == "Č" and len(hra.herni_pole[pole.cislo_pole + hra.kostka.kostka_3 - 1].zasobnik) == 1 and hra.kostka.kostka_3 != 0:
                        start = pole.cislo_pole
                        pohyby_start.append(start)

                    elif pole.cislo_pole + hra.kostka.kostka_4 <= 24 and pole.barva == "B" and hra.herni_pole[pole.cislo_pole + hra.kostka.kostka_4 - 1].barva != "Č" and hra.kostka.kostka_4 != 0 and len(hra.herni_pole[pole.cislo_pole + hra.kostka.kostka_4 - 1].zasobnik) < 5 or \
                       pole.cislo_pole + hra.kostka.kostka_4 <= 24 and pole.barva == "B" and hra.herni_pole[pole.cislo_pole + hra.kostka.kostka_4 - 1].barva == "Č" and len(hra.herni_pole[pole.cislo_pole + hra.kostka.kostka_4 - 1].zasobnik) == 1 and hra.kostka.kostka_4 != 0:
                        start = pole.cislo_pole
                        pohyby_start.append(start)
                        
            elif self.barva == "Černý":
                for pole in hra.herni_pole:
                    if pole.cislo_pole - hra.kostka.kostka_1 >= 1 and pole.barva == "Č" and hra.herni_pole[pole.cislo_pole - hra.kostka.kostka_1 - 1].barva != "B" and hra.kostka.kostka_1 != 0 and len(hra.herni_pole[pole.cislo_pole - hra.kostka.kostka_1 - 1].zasobnik) < 5 or \
                       pole.cislo_pole - hra.kostka.kostka_1 >= 1 and pole.barva == "Č" and hra.herni_pole[pole.cislo_pole - hra.kostka.kostka_1 - 1].barva == "B" and len(hra.herni_pole[pole.cislo_pole - hra.kostka.kostka_1 - 1].zasobnik) == 1 and hra.kostka.kostka_1 != 0:
                        start = pole.cislo_pole
                        pohyby_start.append(start)
                    if pole.cislo_pole - hra.kostka.kostka_2 >= 1 and pole.barva == "Č" and hra.herni_pole[pole.cislo_pole - hra.kostka.kostka_2 - 1].barva != "B" and hra.kostka.kostka_2 != 0 and len(hra.herni_pole[pole.cislo_pole - hra.kostka.kostka_2 - 1].zasobnik) < 5 or \
                       pole.cislo_pole - hra.kostka.kostka_2 >= 1 and pole.barva == "Č" and hra.herni_pole[pole.cislo_pole - hra.kostka.kostka_2 - 1].barva == "B" and len(hra.herni_pole[pole.cislo_pole - hra.kostka.kostka_2 - 1].zasobnik) == 1 and hra.kostka.kostka_2 != 0:
                        start = pole.cislo_pole
                        pohyby_start.append(start)
                    if pole.cislo_pole - hra.kostka.kostka_3 >= 1 and pole.barva == "Č" and hra.herni_pole[pole.cislo_pole - hra.kostka.kostka_3 - 1].barva != "B" and hra.kostka.kostka_3 != 0 and len(hra.herni_pole[pole.cislo_pole - hra.kostka.kostka_3 - 1].zasobnik) < 5 or \
                       pole.cislo_pole - hra.kostka.kostka_3 >= 1 and pole.barva == "Č" and hra.herni_pole[pole.cislo_pole - hra.kostka.kostka_3 - 1].barva == "B" and len(hra.herni_pole[pole.cislo_pole - hra.kostka.kostka_3 - 1].zasobnik) == 1 and hra.kostka.kostka_3 != 0:
                        start = pole.cislo_pole
                        pohyby_start.append(start)
                    if pole.cislo_pole - hra.kostka.kostka_4 >= 1 and pole.barva == "Č" and hra.herni_pole[pole.cislo_pole - hra.kostka.kostka_4 - 1].barva != "B" and hra.kostka.kostka_4 != 0 and len(hra.herni_pole[pole.cislo_pole - hra.kostka.kostka_4 - 1].zasobnik) < 5 or \
                       pole.cislo_pole - hra.kostka.kostka_4 >= 1 and pole.barva == "Č" and hra.herni_pole[pole.cislo_pole - hra.kostka.kostka_4 - 1].barva == "B" and len(hra.herni_pole[pole.cislo_pole - hra.kostka.kostka_4 - 1].zasobnik) == 1 and hra.kostka.kostka_4 != 0:
                        start = pole.cislo_pole
                        pohyby_start.append(start)

            if hra.kostka.double == 0 and hra.kostka.kostka_1 > 0 and hra.kostka.kostka_2 > 0:
                inp = rand(1,2)
            elif hra.kostka.double == 0 and hra.kostka.kostka_1 == 0 and hra.kostka.kostka_2 > 0:
                inp = 2
            elif hra.kostka.double == 0 and hra.kostka.kostka_1 > 0 and hra.kostka.kostka_2 == 0:
                inp = 1
            elif hra.kostka.double == 2 and hra.kostka.kostka_1 > 0 and hra.kostka.kostka_2 > 0:
                inp = rand(1,4)
            elif hra.kostka.double == 2 and hra.kostka.kostka_1 > 0 and hra.kostka.kostka_2 == 0:
                inp = 1
            elif hra.kostka.double == 2 and hra.kostka.kostka_1 == 0 and hra.kostka.kostka_2 > 0:
                inp = rand(2,4)
            elif hra.kostka.double == 2 and hra.kostka.kostka_1 == 0 and hra.kostka.kostka_2 == 0:
                inp = rand(3,4)
            elif hra.kostka.double == 1 and hra.kostka.kostka_3 == 0 and hra.kostka.kostka_4 > 0:
                inp = 4
            elif hra.kostka.double == 1 and hra.kostka.kostka_1 == 0 and hra.kostka.kostka_2 > 0:
                inp = 2
            elif hra.kostka.double == 1 and hra.kostka.kostka_1 > 0 and hra.kostka.kostka_2 == 0:
                inp = 1
            elif hra.kostka.double == 1 and hra.kostka.kostka_3 > 0 and hra.kostka.kostka_4 == 0:
                inp = 3

            if inp == 1:                                                
                if self.barva == 'Černý':
                    start_pol = pohyby_start[rand(0, len(pohyby_start)-1)]
                    cil = start_pol - hra.kostka.kostka_1
                    print(cil)
                else:
                    start_pol = pohyby_start[rand(0, len(pohyby_start)-1)]
                    cil = start_pol + hra.kostka.kostka_1
                    print(cil)
            elif inp == 2:
                if self.barva == 'Černý':
                    start_pol = pohyby_start[rand(0, len(pohyby_start)-1)]
                    cil = start_pol - hra.kostka.kostka_2
                    print(cil)
                else:
                    start_pol = pohyby_start[rand(0, len(pohyby_start)-1)]
                    cil = start_pol + hra.kostka.kostka_2
                    print(cil)                             
            elif inp == 3 and hra.kostka.kostka_1 == hra.kostka.kostka_2:
                if self.barva == 'Černý':
                    start_pol = pohyby_start[rand(0, len(pohyby_start)-1)]
                    cil = start_pol - hra.kostka.kostka_3
                    print(cil)
                else:
                    start_pol = pohyby_start[rand(0, len(pohyby_start)-1)]
                    cil = start_pol + hra.kostka.kostka_3
                    print(cil)                         # Možnost pohybu o součet obou kostek
            elif inp == 4 and hra.kostka.kostka_1 == hra.kostka.kostka_2:
                if self.barva == 'Černý':
                    start_pol = pohyby_start[rand(0, len(pohyby_start)-1)]
                    cil = start_pol - hra.kostka.kostka_4
                    print(cil)
                else:
                    start_pol = pohyby_start[rand(0, len(pohyby_start)-1)]
                    cil = start_pol + hra.kostka.kostka_4
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

            pole_start = hra.herni_pole[start - 1]
            pole_cil = hra.herni_pole[cil - 1]
            
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
                            hra.barec.pridej_do_baru(vyhazovac)
                            pole_start.zasobnik.remove(pole_start.zasobnik[0])
                            pole_cil.zasobnik.append(temp[0])
                            if inp == 1:                                            # Zde se nastavují hodnoty, podle toho co se hráč rozhodne udělat při přesunech žetonu o jednu, druhou nebo součet obou kostek
                                hra.presuny = hra.presuny + 1
                                hra.kostka.kostka_1 = 0
                            elif inp == 2:
                                hra.presuny = hra.presuny + 1
                                hra.kostka.kostka_2 = 0
                            elif inp == 3:
                                hra.kostka.kostka_3 = 0
                                hra.kostka.double -= 1
                            elif inp == 4:
                                hra.kostka.kostka_4 = 0
                                hra.kostka.double -= 1
                        elif pole_cil.barva == pole_start.barva or pole_cil.barva == "N":
                            pole_start.zasobnik.remove(pole_start.zasobnik[0])
                            pole_cil.zasobnik.append(temp[0])
                            if inp == 1:                                            # Zde se nastavují hodnoty, podle toho co se hráč rozhodne udělat při přesunech žetonu o jednu, druhou nebo součet obou kostek
                                hra.presuny = hra.presuny + 1
                                hra.kostka.kostka_1 = 0
                            elif inp == 2:
                                hra.presuny = hra.presuny + 1
                                hra.kostka.kostka_2 = 0
                            elif inp == 3:
                                hra.kostka.kostka_3 = 0
                                hra.kostka.double -= 1
                            elif inp == 4:
                                hra.kostka.kostka_4 = 0
                                hra.kostka.double -= 1
                else:
                    print("Pole ze kterého se snažíte brát, je prázdné!")
        elif hra.presuny == 2:
            print("Už jsi táhl za obě kostky!")
        elif hra.hozeno == 0:
            print("Nejdřív si hoď!")
        elif self.barva == "Černý" and len(hra.barec.zetony_cerna) > 0 or self.barva == "Bílý" and len(hra.barec.zetony_bila) >0:
            print("Nejdřív vyjeď z baru!")
                        

    def vyhod_z_baru(self):                                       
        if self.barva == "Bílý" and len(hra.barec.zetony_bila) >= 1:
            if len(hra.barec.zetony_bila) >= 1:
                x = hra.barec.zetony_bila.pop(-1)[0]
                hra.barec.vyjeti_z_baru_ai(x, "Bílý")
            else:
                pass
        elif self.barva == "Černý" and len(hra.barec.zetony_cerna) >= 1:
            if len(hra.barec.zetony_cerna) >= 1:
                x = hra.barec.zetony_cerna.pop(-1)[0]
                hra.barec.vyjeti_z_baru_ai(x, "Černý")
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
            for objekt in hra.herni_pole[i].zasobnik:
                if objekt.barva == "Černý":
                    self.kontrola_cerna += 1

        for j in range(18,23):
            for objekt in hra.herni_pole[j].zasobnik:
                if objekt.barva == "Bílý":
                    self.kontrola_bila += 1

        vse_akt_zetony_cerna = 15 - len(hra.cilove_pole_cerna)
        vse_akt_zetony_bila = 15 - len(hra.cilove_pole_bila)
        
        if self.barva == "Černý" and self.kontrola_cerna == vse_akt_zetony_cerna or self.barva == "Bílý" and self.kontrola_bila == vse_akt_zetony_bila:
            if hra.presuny < 2:
                if self.barva == "Bílý":
                    for pole in hra.herni_pole:
                        if pole.cislo_pole + hra.kostka.kostka_1 <= 24 and pole.barva == "B" and hra.herni_pole[pole.cislo_pole + hra.kostka.kostka_1 - 1].barva != "Č" and hra.kostka.kostka_1 != 0 and len(hra.herni_pole[pole.cislo_pole + hra.kostka.kostka_1 - 1].zasobnik) < 5 or \
                        pole.cislo_pole + hra.kostka.kostka_1 <= 24 and pole.barva == "B" and hra.herni_pole[pole.cislo_pole + hra.kostka.kostka_1 - 1].barva == "Č" and len(hra.herni_pole[pole.cislo_pole + hra.kostka.kostka_1 - 1].zasobnik) == 1 and hra.kostka.kostka_1 != 0:
                            start = pole.cislo_pole
                            pohyby_start.append(start)
                        elif pole.cislo_pole + hra.kostka.kostka_2 <= 24 and pole.barva == "B" and hra.herni_pole[pole.cislo_pole + hra.kostka.kostka_2 - 1].barva != "Č" and hra.kostka.kostka_2 != 0 and len(hra.herni_pole[pole.cislo_pole + hra.kostka.kostka_2 - 1].zasobnik) < 5 or \
                        pole.cislo_pole + hra.kostka.kostka_2 <= 24 and pole.barva == "B" and hra.herni_pole[pole.cislo_pole + hra.kostka.kostka_2 - 1].barva == "Č" and len(hra.herni_pole[pole.cislo_pole + hra.kostka.kostka_2 - 1].zasobnik) == 1 and hra.kostka.kostka_2 != 0:
                            start = pole.cislo_pole
                            pohyby_start.append(start)

                        elif pole.cislo_pole + hra.kostka.kostka_3 <= 24 and pole.barva == "B" and hra.herni_pole[pole.cislo_pole + hra.kostka.kostka_3 - 1].barva != "Č" and hra.kostka.kostka_3 != 0 and len(hra.herni_pole[pole.cislo_pole + hra.kostka.kostka_3 - 1].zasobnik) < 5 or \
                        pole.cislo_pole + hra.kostka.kostka_3 <= 24 and pole.barva == "B" and hra.herni_pole[pole.cislo_pole + hra.kostka.kostka_3 - 1].barva == "Č" and len(hra.herni_pole[pole.cislo_pole + hra.kostka.kostka_3 - 1].zasobnik) == 1 and hra.kostka.kostka_3 != 0:
                            start = pole.cislo_pole
                            pohyby_start.append(start)

                        elif pole.cislo_pole + hra.kostka.kostka_4 <= 24 and pole.barva == "B" and hra.herni_pole[pole.cislo_pole + hra.kostka.kostka_4 - 1].barva != "Č" and hra.kostka.kostka_4 != 0 and len(hra.herni_pole[pole.cislo_pole + hra.kostka.kostka_4 - 1].zasobnik) < 5 or \
                        pole.cislo_pole + hra.kostka.kostka_4 <= 24 and pole.barva == "B" and hra.herni_pole[pole.cislo_pole + hra.kostka.kostka_4 - 1].barva == "Č" and len(hra.herni_pole[pole.cislo_pole + hra.kostka.kostka_4 - 1].zasobnik) == 1 and hra.kostka.kostka_4 != 0:
                            start = pole.cislo_pole
                            pohyby_start.append(start)
                            
                elif self.barva == "Černý":
                    for pole in hra.herni_pole:
                        if pole.cislo_pole - hra.kostka.kostka_1 >= 1 and pole.barva == "Č" and hra.herni_pole[pole.cislo_pole - hra.kostka.kostka_1 - 1].barva != "B" and hra.kostka.kostka_1 != 0 and len(hra.herni_pole[pole.cislo_pole - hra.kostka.kostka_1 - 1].zasobnik) < 5 or \
                        pole.cislo_pole - hra.kostka.kostka_1 >= 1 and pole.barva == "Č" and hra.herni_pole[pole.cislo_pole - hra.kostka.kostka_1 - 1].barva == "B" and len(hra.herni_pole[pole.cislo_pole - hra.kostka.kostka_1 - 1].zasobnik) == 1 and hra.kostka.kostka_1 != 0:
                            start = pole.cislo_pole
                            pohyby_start.append(start)
                        if pole.cislo_pole - hra.kostka.kostka_2 >= 1 and pole.barva == "Č" and hra.herni_pole[pole.cislo_pole - hra.kostka.kostka_2 - 1].barva != "B" and hra.kostka.kostka_2 != 0 and len(hra.herni_pole[pole.cislo_pole - hra.kostka.kostka_2 - 1].zasobnik) < 5 or \
                        pole.cislo_pole - hra.kostka.kostka_2 >= 1 and pole.barva == "Č" and hra.herni_pole[pole.cislo_pole - hra.kostka.kostka_2 - 1].barva == "B" and len(hra.herni_pole[pole.cislo_pole - hra.kostka.kostka_2 - 1].zasobnik) == 1 and hra.kostka.kostka_2 != 0:
                            start = pole.cislo_pole
                            pohyby_start.append(start)
                        if pole.cislo_pole - hra.kostka.kostka_3 >= 1 and pole.barva == "Č" and hra.herni_pole[pole.cislo_pole - hra.kostka.kostka_3 - 1].barva != "B" and hra.kostka.kostka_3 != 0 and len(hra.herni_pole[pole.cislo_pole - hra.kostka.kostka_3 - 1].zasobnik) < 5 or \
                        pole.cislo_pole - hra.kostka.kostka_3 >= 1 and pole.barva == "Č" and hra.herni_pole[pole.cislo_pole - hra.kostka.kostka_3 - 1].barva == "B" and len(hra.herni_pole[pole.cislo_pole - hra.kostka.kostka_3 - 1].zasobnik) == 1 and hra.kostka.kostka_3 != 0:
                            start = pole.cislo_pole
                            pohyby_start.append(start)
                        if pole.cislo_pole - hra.kostka.kostka_4 >= 1 and pole.barva == "Č" and hra.herni_pole[pole.cislo_pole - hra.kostka.kostka_4 - 1].barva != "B" and hra.kostka.kostka_4 != 0 and len(hra.herni_pole[pole.cislo_pole - hra.kostka.kostka_4 - 1].zasobnik) < 5 or \
                        pole.cislo_pole - hra.kostka.kostka_4 >= 1 and pole.barva == "Č" and hra.herni_pole[pole.cislo_pole - hra.kostka.kostka_4 - 1].barva == "B" and len(hra.herni_pole[pole.cislo_pole - hra.kostka.kostka_4 - 1].zasobnik) == 1 and hra.kostka.kostka_4 != 0:
                            start = pole.cislo_pole
                            pohyby_start.append(start)

                if hra.kostka.double == 0 and hra.kostka.kostka_1 > 0 and hra.kostka.kostka_2 > 0:
                    inp = rand(1,2)
                elif hra.kostka.double == 0 and hra.kostka.kostka_1 == 0 and hra.kostka.kostka_2 > 0:
                    inp = 2
                elif hra.kostka.double == 0 and hra.kostka.kostka_1 > 0 and hra.kostka.kostka_2 == 0:
                    inp = 1
                elif hra.kostka.double == 2 and hra.kostka.kostka_1 > 0 and hra.kostka.kostka_2 > 0:
                    inp = rand(1,4)
                elif hra.kostka.double == 2 and hra.kostka.kostka_1 > 0 and hra.kostka.kostka_2 == 0:
                    inp = 1
                elif hra.kostka.double == 2 and hra.kostka.kostka_1 == 0 and hra.kostka.kostka_2 > 0:
                    inp = rand(2,4)
                elif hra.kostka.double == 2 and hra.kostka.kostka_1 == 0 and hra.kostka.kostka_2 == 0:
                    inp = rand(3,4)
                elif hra.kostka.double == 1 and hra.kostka.kostka_3 == 0 and hra.kostka.kostka_4 > 0:
                    inp = 4
                elif hra.kostka.double == 1 and hra.kostka.kostka_1 == 0 and hra.kostka.kostka_2 > 0:
                    inp = 2
                elif hra.kostka.double == 1 and hra.kostka.kostka_1 > 0 and hra.kostka.kostka_2 == 0:
                    inp = 1
                elif hra.kostka.double == 1 and hra.kostka.kostka_3 > 0 and hra.kostka.kostka_4 == 0:
                    inp = 3

                if inp == 1:                                                
                    if self.barva == 'Černý':
                        start_pol = pohyby_start[rand(0, len(pohyby_start)-1)]
                        cil = start_pol - hra.kostka.kostka_1
                        print(cil)
                    else:
                        start_pol = pohyby_start[rand(0, len(pohyby_start)-1)]
                        cil = start_pol + hra.kostka.kostka_1
                        print(cil)
                elif inp == 2:
                    if self.barva == 'Černý':
                        start_pol = pohyby_start[rand(0, len(pohyby_start)-1)]
                        cil = start_pol - hra.kostka.kostka_2
                        print(cil)
                    else:
                        start_pol = pohyby_start[rand(0, len(pohyby_start)-1)]
                        cil = start_pol + hra.kostka.kostka_2
                        print(cil)                             
                elif inp == 3 and hra.kostka.kostka_1 == hra.kostka.kostka_2:
                    if self.barva == 'Černý':
                        start_pol = pohyby_start[rand(0, len(pohyby_start)-1)]
                        cil = start_pol - hra.kostka.kostka_3
                        print(cil)
                    else:
                        start_pol = pohyby_start[rand(0, len(pohyby_start)-1)]
                        cil = start_pol + hra.kostka.kostka_3
                        print(cil)                         
                elif inp == 4 and hra.kostka.kostka_1 == hra.kostka.kostka_2:
                    if self.barva == 'Černý':
                        start_pol = pohyby_start[rand(0, len(pohyby_start)-1)]
                        cil = start_pol - hra.kostka.kostka_4
                        print(cil)
                    else:
                        start_pol = pohyby_start[rand(0, len(pohyby_start)-1)]
                        cil = start_pol + hra.kostka.kostka_4
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

                pole_start = hra.herni_pole[start - 1]
                if self.barva == "Černý":
                    pole_cil = hra.cilove_pole_cerna
                elif self.barva == "Bílý":
                    pole_cil = hra.cilove_pole_bila

                if cil == 0 and self.barva == "Černý" or cil == 25 and self.barva == "Bílý":                                     # Ošetření, aby zásobník, na který se přidává nebyl plný
                    temp =[]
                    temp.append(pole_start.zasobnik[0])
                    pole_cil.append(temp[0])
                    pole_start.zasobnik.remove(pole_start.zasobnik[0])
                    if inp == 1:                                            # Zde se nastavují hodnoty, podle toho co se hráč rozhodne udělat při přesunech žetonu o jednu, druhou nebo součet obou kostek
                        hra.presuny = hra.presuny + 1
                        hra.kostka.kostka_1 = 0
                    elif inp == 2:
                        hra.presuny = hra.presuny + 1
                        hra.kostka.kostka_2 = 0
                    elif inp == 3:
                        hra.kostka.kostka_3 = 0
                    elif inp == 4:
                        hra.kostka.kostka_4 = 0
                else:
                    print(cil)
                    print("Něco se pokazilo")

            elif hra.presuny == 2:
                print("Už jsi táhl za obě kostky!")
        else:
            print("Nemáš všechny žetony na posledních polích!")

    def nabidka(self):
        if hra.hozeno == 0:
            hra.kostka.hod_kostkami()
        self.kontrola_pohybu()
        if self.barva == "Bílý" and self.kontrola_bila == 15 or self.barva == "Černý" and self.kontrola_cerna == 15:
            self.jedu_do_cile()
        if len(hra.barec.zetony_bila) == 0 and self.barva == "Bílý" or len(hra.barec.zetony_cerna) == 0 and self.barva == "Černý":
            self.tah()
        elif len(hra.barec.zetony_bila) > 0 and self.barva == "Bílý" or len(hra.barec.zetony_cerna) > 0 and self.barva == "Černý":
            self.vyhod_z_baru()
        self.prerus_tah()

        


hra = HerniDeska()                  # Vytvoření instance herní desky 
hra.priprav_hru()                   # Připravení hry                     
#hra.statistiky_rezignace_hry()


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
