from random import random, randint

# La clase qui decrit un hero
class Hero:
    # points de vie, la valeur de depart est 10
    nombre_point_de_vie = 10
    # force d'attaque, valeur de depart 2
    force_d_attaque = 2
    # force de defense, valeur de depart 2
    force_defense = 2
    nom_hero = ""

    # Le nom du hero est obligatoire
    def __init__(self, nom):
        self.nom_hero = nom

    # on fait un attaque avec la valeur alletoire + force d'attaque
    def faire_attaque(self):
        val = randint(1, 6)
        return self.force_d_attaque + val

    # quand on recois dommage on diminue valeur de points de vie pour la dommage minus force de defense
    def recevoir_dommages(self, nombre_dommages):
        self.nombre_point_de_vie -= nombre_dommages - self.force_defense

    # retourne vrai si points de vie sont plus grands que zero
    def est_vivant(self):
        return self.nombre_point_de_vie > 0