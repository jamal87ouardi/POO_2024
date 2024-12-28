class Patient:
    

    def __init__(self, poids, taille):
       
        self.poids = poids
        self.taille = taille

    def calculerIMC(self):
        
        return self.poids / (self.taille ** 2)

    
poids = float(input("Entrez le poids en kg : "))
taille = float(input("Entrez la taille en mètres : "))

p = Patient(poids, taille)

imc = p.calculerIMC()


print(f"Votre IMC est : {imc}")
        

    
