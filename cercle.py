from math import pi

class Cercle:

    # Le champ contenant le rayon de cercle
    rayon = 0.0

    # Cuand nous creons l'objet
    def __init__(self, rayon):
        self.rayon = rayon

    # Nous calculons et returnons l'aire
    def calcul_aire(self):
        return self.rayon * self.rayon * pi

    # Nous calculons et returnons le circonference
    def calcur_circonference(self):
        return 2 * self.rayon * pi