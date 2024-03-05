print("Bienvenue dans la superette de Rémy")
class superette:
    def __init__(self):
        self.produits = {"Lait": [50, 1.45], "Oeufs": [80, 0.30], "Chocolat": [15, 3.75], "Viande": [22, 8.99]}
    def menuPrincipal(self):
        print("1. Lait")
        print("2. Oeufs")
        print("3. Chocolat")
        print("4. Viande")

