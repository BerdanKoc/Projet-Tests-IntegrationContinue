from pytest_bdd import scenarios, given, when, then
from src.main import Personnage, Equipe, resoudre_duel
from unittest.mock import patch
import pytest

scenarios('../features/combat.feature')

@pytest.fixture
def contexte():
    return {}

# --- Scénario 1 ---
@given('un personnage nommé "Hero"')
def create_hero(contexte):
    contexte['hero'] = Personnage("Hero")

@then('le personnage a 10 points de vie')
def check_hp(contexte):
    assert contexte['hero'].hp == 10

@then('le personnage est vivant')
def check_alive(contexte):
    assert contexte['hero'].est_vivant is True

# --- Scénario 2 ---
@given('un personnage nommé "Attaquant"')
def create_attacker(contexte):
    contexte['attaquant'] = Personnage("Attaquant")

@given('un second personnage nommé "Cible"')
def create_target(contexte):
    contexte['cible'] = Personnage("Cible")

@when('l\'attaquant attaque la cible')
def attack(contexte):
    contexte['attaquant'].attaquer(contexte['cible'])

@then('la cible a entre 9 et 10 points de vie')
def check_target_hp_range(contexte):
    assert contexte['cible'].hp in [9, 10]

# --- Scénario 3 ---
@given('une victime avec 1 point de vie')
def create_victim(contexte):
    perso = Personnage("Victime")
    perso.hp = 1 
    contexte['hero'] = perso

@when('la victime subit 1 degat')
def take_damage_1(contexte):
    contexte['hero'].recevoir_degats(1)

@then('le personnage est mort')
def check_dead(contexte):
    assert contexte['hero'].est_vivant is False

# --- Scénario 4 : Armure ---
@given('une cible avec 2 points d\'armure')
def create_armored_target(contexte):
    perso = Personnage("Tank", armure=2)
    contexte['cible_armure'] = perso

@when('la cible subit 5 degats')
def take_damage_5(contexte):
    contexte['cible_armure'].recevoir_degats(5)

@then('la cible perd seulement 3 points de vie')
def check_armored_hp(contexte):
    assert contexte['cible_armure'].hp == 7

# --- Scénario 5 : 2v2 ---
@given('une equipe "Rouge" avec 2 joueurs')
def create_team_red(contexte):
    contexte['equipe_rouge'] = Equipe("Rouge", [Personnage("R1"), Personnage("R2")])

@given('une equipe "Bleue" avec 2 joueurs')
def create_team_blue(contexte):
    contexte['equipe_bleue'] = Equipe("Bleue", [Personnage("B1"), Personnage("B2")])

@when('l\'equipe Rouge et Bleue s\'affrontent')
def team_fight(contexte):
    contexte['equipe_rouge'].joueurs[0].attaquer(contexte['equipe_bleue'].joueurs[0])

@then('au moins un joueur a perdu des points de vie')
def check_team_fight(contexte):
    b1_hp = contexte['equipe_bleue'].joueurs[0].hp
    assert b1_hp in [9, 10]

# --- Scénario 6 : Évolution ---
@given('un attaquant "Tueur"')
def create_killer(contexte):
    contexte['tueur'] = Personnage("Tueur")
    contexte['stats_avant'] = contexte['tueur'].endurance + contexte['tueur'].force + contexte['tueur'].niveau + contexte['tueur'].agilite

@given('une cible "Victime" avec 1 point de vie')
def create_killable_victim(contexte):
    cible = Personnage("Victime")
    cible.hp = 1
    contexte['victime'] = cible

@when('"Tueur" attaque et tue "Victime"')
def kill_victim(contexte):
    with patch('src.main.random.randint', return_value=5):
        contexte['tueur'].attaquer(contexte['victime'])

@then('les statistiques de "Tueur" ont augmente')
def check_evolution(contexte):
    tueur = contexte['tueur']
    stats_apres = tueur.endurance + tueur.force + tueur.niveau + tueur.agilite
    assert stats_apres > contexte['stats_avant']

@given('un personnage "Rapide" avec 10 en agilite')
def create_fast(contexte):
    contexte['rapide'] = Personnage("Rapide", agilite=10)

@given('un personnage "Lent" avec 0 en agilite')
def create_slow(contexte):
    contexte['lent'] = Personnage("Lent", agilite=0)

@when('un duel est lance')
def start_duel(contexte):
    contexte['premier_attaquant'] = resoudre_duel(contexte['rapide'], contexte['lent'])

@then('"Rapide" attaque en premier')
def check_first_attacker(contexte):
    assert contexte['premier_attaquant'].nom == "Rapide"

@given('une equipe avec "Saine" a 10 HP et "Blessee" a 2 HP')
def create_team_with_weakling(contexte):
    saine = Personnage("Saine")
    blessee = Personnage("Blessee")
    blessee.hp = 2
    contexte['equipe_cible'] = Equipe("Cibles", [saine, blessee])

@when('on cherche la cible prioritaire')
def find_priority(contexte):
    contexte['cible_trouvee'] = contexte['equipe_cible'].obtenir_cible_prioritaire()

@then('"Blessee" est choisie')
def check_priority_target(contexte):
    assert contexte['cible_trouvee'].nom == "Blessee"