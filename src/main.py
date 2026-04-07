class Personnage:
    def __init__(self, nom, hp=10):
        self.nom = nom
        self.hp = hp

    @property
    def est_vivant(self):
        return self.hp > 0

    def attaquer(self, cible):
        cible.recevoir_degats(1)

    def recevoir_degats(self, degats):
        self.hp -= degats
        if self.hp < 0:
            self.hp = 0