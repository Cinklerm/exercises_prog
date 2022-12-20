class Rectangle:
    # Etablir les valeurs de depart
    largeur = 0.0
    longeur = 0.0
    aire = 0.0

    # Quand nous creons l'objet, nous devons passer la largeur et la longeur
    def __init__(self, largeur, longeur):
        self.largeur = largeur
        self.longeur = longeur

    # Cuand nous calculons l'aire, nous sauvegardons la valeur dans le nouveau champ
    def calcul_aire(self):
        self.aire = self.longeur * self.largeur

    # Nous imprimons tous ici
    def afficher_infos(self):
        print("largeur:" + str(self.largeur))
        print("longeur:" + str(self.longeur))
        print("aire:" + str(self.aire))
