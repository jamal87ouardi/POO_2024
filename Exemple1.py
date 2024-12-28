class Patient :

    def __init__(self, poids, taille):
        self.__poids = poids
        self.__taille = taille

    def calculerIMC(self) :
        imc = self.__poids / (self.__taille**2)
        return imc
    
ali = Patient(80.0, 1.75)

print(f"IMC ali est {ali.calculerIMC()}")

moad = Patient(72.5, 1.82)
print(f"imc de moad est {moad.calculerIMC()}")