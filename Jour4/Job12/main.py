def tri(liste):
    n = 0
    for _ in liste:
        n += 1

    for i in range(n):
        for b in range(0, n-i-1):
            if liste[b] > liste[b+1]:
                temp = liste[b]
                liste[b] = liste[b+1]
                liste[b+1] = temp

ma_liste = [2, 8, 5, 4, 6, 11, 9]
print("Liste :", ma_liste)
tri(ma_liste)
print("Liste ordre croissant :", ma_liste)