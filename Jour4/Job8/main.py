def calcul(L):
    pair = 0
    for nb in L:
        if nb % 2== 0:
            pair += nb
    return pair


L = [8, 24, 27, 48, 2,16, 9, 7, 84, 91]

somme = calcul(L)
print("Somme des nombres pairs dans la liste : ", somme)
