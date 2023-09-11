import random, sys, os, json
rand = random.randint


class HerniKamen:                                                   # Třída herního kamene
    def __init__(self, barva):
        self.barva = barva