Feature: Système de combat RPG

  Scenario: Un personnage commence avec 10 points de vie
    Given un personnage nommé "Hero"
    Then le personnage a 10 points de vie
    And le personnage est vivant

  Scenario: Attaquer inflige des degats aleatoires
    Given un personnage nommé "Attaquant"
    And un second personnage nommé "Cible"
    When l'attaquant attaque la cible
    Then la cible a entre 9 et 10 points de vie

  Scenario: La mort a zero HP
    Given une victime avec 1 point de vie
    When la victime subit 1 degat
    Then le personnage est mort

  Scenario: L'armure reduit les degats subis
    Given une cible avec 2 points d'armure
    When la cible subit 5 degats
    Then la cible perd seulement 3 points de vie

  Scenario: Duel 2v2
    Given une equipe "Rouge" avec 2 joueurs
    And une equipe "Bleue" avec 2 joueurs
    When l'equipe Rouge et Bleue s'affrontent
    Then au moins un joueur a perdu des points de vie

    Scenario: Un personnage evolue s'il tue un ennemi
    Given un attaquant "Tueur"
    And une cible "Victime" avec 1 point de vie
    When "Tueur" attaque et tue "Victime"
    Then les statistiques de "Tueur" ont augmente

  Scenario: L'agilite determine l'ordre d'attaque
    Given un personnage "Rapide" avec 10 en agilite
    And un personnage "Lent" avec 0 en agilite
    When un duel est lance
    Then "Rapide" attaque en premier

  Scenario: Focus de la cible sous 30% HP
    Given une equipe avec "Saine" a 10 HP et "Blessee" a 2 HP
    When on cherche la cible prioritaire
    Then "Blessee" est choisie