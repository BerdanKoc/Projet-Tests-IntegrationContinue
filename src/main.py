import random

class Personnage:
    def __init__(self, nom, endurance=0, force=0, niveau=0, arme=0, armure=0):
        self.nom = nom
        self.endurance = endurance
        self.force = force
        self.niveau = niveau
        self.arme = arme
        self.armure = armure
        self.hp = 10 + self.endurance + (self.niveau * 2)

    @property
    def est_vivant(self):
        return self.hp > 0

    def attaquer(self, cible):
        degats_max = 1 + self.force + (self.niveau * 2) + self.arme
        degats_infliges = random.randint(0, degats_max)
        cible.recevoir_degats(degats_infliges)

    def recevoir_degats(self, degats):
        degats_reels = degats - self.armure
        if degats_reels < 0:
            degats_reels = 0
            
        self.hp -= degats_reels
        if self.hp < 0:
            self.hp = 0

class Equipe:
    def __init__(self, nom, joueurs):
        self.nom = nom
        self.joueurs = joueurs

    @property
    def est_en_vie(self):
        return any(joueur.est_vivant for joueur in self.joueurs)