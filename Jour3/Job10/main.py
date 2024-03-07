def verif():
    while True:
            nombre = int(input("Entrez un nombre entier positif : "))
            if nombre >= 0:
                break 
            else:
                print("Veuillez entrer un nombre positif.")
    if nombre % 2 == 0:
        print("Pair")
    else:
        print("Impair")
verif()