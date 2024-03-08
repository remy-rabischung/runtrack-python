L = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]
print("Liste : ", L)
list = []

for nb in L:
    if nb not in list:
        list.append(nb)

L = list
print("Liste sans doublons : ", L)
