import random

class Personnage:
    def __init__(self, nom, endurance=0, force=0, niveau=0, arme=0, armure=0, agilite=0):
        self.nom = nom
        self.endurance = endurance
        self.force = force
        self.niveau = niveau
        self.arme = arme
        self.armure = armure
        self.agilite = agilite
        
        self.hp_max = 10 + self.endurance + (self.niveau * 2)
        self.hp = self.hp_max

    @property
    def est_vivant(self):
        return self.hp > 0

    def attaquer(self, cible):
        degats_max = 1 + self.force + (self.niveau * 2) + self.arme
        degats_infliges = random.randint(0, degats_max)
        cible.recevoir_degats(degats_infliges)
        
        if not cible.est_vivant and degats_infliges > 0:
            self.evoluer()

    def recevoir_degats(self, degats):
        degats_reels = max(0, degats - self.armure)
        self.hp = max(0, self.hp - degats_reels)

    def evoluer(self):
        stats = ['endurance', 'force', 'niveau', 'agilite']
        stat_choisie = random.choice(stats)
        setattr(self, stat_choisie, getattr(self, stat_choisie) + 1)

        if stat_choisie in ['endurance', 'niveau']:
            self.hp_max = 10 + self.endurance + (self.niveau * 2)

class Equipe:
    def __init__(self, nom, joueurs):
        self.nom = nom
        self.joueurs = joueurs

    @property
    def est_en_vie(self):
        return any(joueur.est_vivant for joueur in self.joueurs)

    def obtenir_cible_prioritaire(self):
        cibles_vivantes = [j for j in self.joueurs if j.est_vivant]
        if not cibles_vivantes:
            return None
        
        cibles_faibles = [j for j in cibles_vivantes if j.hp < (0.3 * j.hp_max)]
        if cibles_faibles:
            return cibles_faibles[0]
            
        return random.choice(cibles_vivantes)

def resoudre_duel(perso1, perso2):
    premier = perso1 if perso1.agilite >= perso2.agilite else perso2
    second = perso2 if premier == perso1 else perso1
    
    premier.attaquer(second)
    if second.est_vivant:
        second.attaquer(premier)
        
    return premier