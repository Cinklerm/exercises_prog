from string_foo import StringFoo

# 2 instances de la classe StringFoo
sf = StringFoo()
bc = StringFoo()

# Nous changons les valeurs
sf.set_string("Martin")
bc.set_string("CdM")

# Nous imprimons les valeurs
sf.print_string()
bc.print_string()