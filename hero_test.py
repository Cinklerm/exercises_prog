from hero import Hero

# nouveau hero
h = Hero("Spiderman")

# on fait attaque
h.faire_attaque()

# on imprime si le hero es vivant
print("vivant:" + str(h.est_vivant()))

# on recoit dommage 3 foit pour s'<'assurer que le hero ne sera pas vivant
h.recevoir_dommages(6)
h.recevoir_dommages(6)
h.recevoir_dommages(6)

# on imprime si le hero es vivant
print("vivant:" + str(h.est_vivant()))
