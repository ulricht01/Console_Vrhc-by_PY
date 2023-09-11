import random, sys, os, json
rand = random.randint

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
