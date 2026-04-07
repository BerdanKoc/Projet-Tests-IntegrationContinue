class Personnage:
    def __init__(self, nom, force=0):
        self.nom = nom
        self.force = force
        self.hp = 10

    @property
    def est_vivant(self):
        return self.hp > 0

    def attaquer(self, cible):
        degats = 1 + self.force
        cible.recevoir_degats(degats)

    def recevoir_degats(self, degats):
        self.hp -= degats
        if self.hp < 0:
            self.hp = 0