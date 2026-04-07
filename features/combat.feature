Feature: Système de combat RPG

  Scenario: Un personnage commence avec 10 points de vie
    Given un personnage nommé "Hero"
    Then le personnage a 10 points de vie
    And le personnage est vivant

  Scenario: Attaquer fait perdre 1 HP
    Given un personnage nommé "Attaquant"
    And un second personnage nommé "Cible"
    When l'attaquant attaque la cible
    Then la cible a 9 points de vie

  Scenario: La mort a zero HP
    Given une victime avec 1 point de vie
    When la victime subit 1 degat
    Then le personnage est mort