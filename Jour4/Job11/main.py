def nombre(liste):
    for i in range(len(liste)):
        liste[i] += 1

L = [7, 11, 42, 39, 2]

print("Liste :", L)
nombre(L)
print("Liste avec + 1 :", L)

