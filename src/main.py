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
        degats = 1 + self.force + (self.niveau * 2)
        cible.recevoir_degats(degats)
        
    def recevoir_degats(self, degats):
        self.hp -= degats
        if self.hp < 0:
            self.hp = 0