class Produit:
    def __init__(self, nom, prix_unitaire, quantite_stock):
        self.nom = nom
        self.prix_unitaire = prix_unitaire
        self.quantite_stock = quantite_stock

    def afficher_info(self):
        print(f"Nom du produit: {self.nom}")
        print(f"Prix unitaire: {self.prix_unitaire} €")
        print(f"Quantité en stock: {self.quantite_stock}")

    def ajouter_stock(self, quantite):
        self.quantite_stock += quantite
        print(f"{quantite} unité(s) de {self.nom} ajoutée(s) au stock.")
        
    def vendre(self, quantite):
        if quantite <= self.quantite_stock:
            self.quantite_stock -= quantite
            print(f"{quantite} unité(s) de {self.nom} vendue(s).")
            return True
        else:
            print(f"Il n'y a pas assez de {self.nom} en stock.")
            return False

# Création des produits
produit1 = Produit("Ordinateur portable", 800, 10)
produit2 = Produit("Smartphone", 600, 20)

# Affichage des informations des produits
print("Informations des produits :")
produit1.afficher_info()
produit2.afficher_info()
print()

# Ajout de produits en stock
produit1.ajouter_stock(5)
produit2.ajouter_stock(10)

# Demande à l'utilisateur de saisir la quantité de produits à acheter
quantite_achat = int(input("Combien d'unités de Smartphone souhaitez-vous acheter ? "))

# Mise à jour du stock après l'achat
if produit2.vendre(quantite_achat):
    print(f"Merci pour votre achat ! Votre facture s'élève à {quantite_achat * produit2.prix_unitaire} €.")
else:
    print("Achat annulé.")

# Affichage des nouvelles informations des produits
print("\nNouvelles informations des produits après l'achat :")
produit1.afficher_info()
produit2.afficher_info()