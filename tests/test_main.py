from pytest_bdd import scenarios, given, when, then
from src.main import Personnage, Equipe
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