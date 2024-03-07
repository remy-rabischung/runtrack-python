def courses(type, saison):
    if type == "Fruits" and saison == "Hiver":
        print("Orange, Mandarine, Kiwi")
    if type == "Fruits" and saison == "été":
        print("Poire, fraise, cassis")
    if type == "Légumes" and saison == "Hiver":
        print("carotte, topinambour, endive")
    if type == "Légumes" and saison == "été":
        print("artichaut, aubergine,navet")

courses("Fruits", "Hiver")
courses("Légumes", "été")


