
class StringFoo:
    # La valeur laquel nous changerons
    valeur = ""

    # Le methode pour imprimer la valeur
    def print_string(self):
        print(self.valeur)

    # Pour changer la valeur nous appelons ce methode
    def set_string(self, val):
        self.valeur = val
