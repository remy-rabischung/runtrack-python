def calcul(L):
    valeur = 0
    for nb in L:
        if nb in range(25, 91):
            valeur += nb 
    return valeur



L = [8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]

somme = calcul(L)
print("Somme des nombres compris entre 25 et 90 de la liste : ", somme)