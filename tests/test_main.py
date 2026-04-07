from pytest_bdd import scenarios, given, when, then
from src.main import Personnage
import pytest

# Charge le fichier Gherkin
scenarios('../features/combat.feature')

# --- Fixtures pour stocker l'état pendant les tests ---
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

@then('la cible a 9 points de vie')
def check_target_hp(contexte):
    assert contexte['cible'].hp == 9

# --- Scénario 3 ---
@given('une victime avec 1 point de vie')
def create_victim(contexte):
    contexte['hero'] = Personnage("Victime", hp=1)

@when('la victime subit 1 degat')
def take_damage(contexte):
    contexte['hero'].recevoir_degats(1)

@then('le personnage est mort')
def check_dead(contexte):
    assert contexte['hero'].est_vivant is False