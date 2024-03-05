n = int(input("Tapez un chiffre ou nombre pour voir sa table de multiplication "))
print("La table de multiplication de : ", n,"est :")
for i in range(1,11):
    print(i , " x ", n, " = ",i*n)
