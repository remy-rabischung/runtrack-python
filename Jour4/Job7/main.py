def x3(L):
    nbx3 = 0
    for nb in L:
        if nb % 3 == 0:
            nbx3 +=1
    return nbx3
    
L = [8, 24, 48, 2, 16]
    
resultat = x3(L)
print("Nombre de multiples de 3 : ", resultat)