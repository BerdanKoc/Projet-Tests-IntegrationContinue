import random

class Personnage:
    def __init__(self, nom, endurance=0, force=0, niveau=0):
        self.nom = nom
        self.endurance = endurance
        self.force = force
        self.niveau = niveau
        self.hp = 10 + self.endurance + (self.niveau * 2)

    @property
    def est_vivant(self):
        return self.hp > 0

    def attaquer(self, cible):
        degats_max = 1 + self.force + (self.niveau * 2)
        degats_infliges = random.randint(0, degats_max)
        cible.recevoir_degats(degats_infliges)

    def recevoir_degats(self, degats):
        self.hp -= degats
        if self.hp < 0:
            self.hp = 0