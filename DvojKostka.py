import random, sys, os, json
rand = random.randint

from HerniDeska import *

class DvojKostka:                                                   # Třída kostky
    def __init__(self, hra):
        self.kostka_1 = 0
        self.kostka_2 = 0
        self.kostka_3 = 0
        self.kostka_4 = 0
        self.hra = hra

    def hod_kostkami(self):                                         # Metoda pro hod kostkami
        if self.hra.hozeno == 0:
            self.kostka_1 = rand(1, 6)
            self.kostka_2 = rand(1, 6)
            if self.kostka_1 == self.kostka_2:
                self.kostka_3 = self.kostka_1
                self.kostka_4 = self.kostka_2
                self.hra.hozeno = 1
                self.double = 2
                return self.kostka_1, self.kostka_2, self.kostka_3, self.kostka_4
            else:
                self.hra.hozeno = 1
                self.double = 0
                return self.kostka_1, self.kostka_2
        else:
            print("Už jsi házel!")
        
    def vynuluj(self):
        self.kostka_1 = 0
        self.kostka_2 = 0
        self.kostka_3 = 0
        self.kostka_4 = 0