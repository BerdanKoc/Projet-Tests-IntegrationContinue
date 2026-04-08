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