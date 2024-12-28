class Produit :
    def __init__(self, id, nom, prix):
        self.id = id
        self.nom = nom
        self.prix = prix

    
    def afficher(self):
        print(f" {self.nom}  - {self.prix} dh")

    def getPrice(self):
        return self.prix


class Pannier :

    def __init__(self):
        self.listProduits = []
    

    def ajouter_produit(self, produit:Produit):
        self.listProduits.append(produit)

    def calculerTotal(self):
        total = 0
        for p in self.listProduits :
            total += p.getPrice()

        return total
    
    def afficher_pannier(self):
        for p in self.listProduits :
            p.afficher()



class Livraison :
    def __init__(self, type, cout):
        self.type = type
        self.cout = cout

    def getCout(self):
        return self.cout

    def afficher(self):
        print(f" Livraison: {self.type} - {self.cout}")

    

class Commande :
    def __init__(self, nomClient, pannier:Pannier, livraison:Livraison):
        self.nomClient = nomClient
        self.pannier = pannier
        self.livraison = livraison
        self.total = self.calculer_total_commande()


    def calculer_total_commande(self):
        return self.pannier.calculerTotal() + self.livraison.getCout()


    def afficher_resume(self): 
        self.pannier.afficher_pannier()
        self.livraison.afficher()
        print(f"total : {self.total} dh")




pannier_ayman = Pannier()

p1 = Produit(1, "Smartphone", 7000)
p2 = Produit(2, "Ordinateur portable", 12000)
p3 = Produit(3, "Smartphone", 7000)

pannier_ayman.ajouter_produit(p1)
pannier_ayman.ajouter_produit(p2)
pannier_ayman.ajouter_produit(p3)



liv = Livraison("Expresse", 100)

com = Commande("Wafi Ayman", pannier_ayman, liv)

com.afficher_resume()



    
    