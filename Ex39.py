class Commande :
    def __init__(self,type_proc,nombre):
        self.__type_proc = type_proc
        self.__nombre = nombre

    def calculerPrixBrut(self):
        if self.__type_proc == "i3" :
            totalBrut = 2500*self.__nombre
        elif self.__type_proc == "i5" :
            totalBrut = 3200*self.__nombre
        elif self.__type_proc == "i7" :
            totalBrut = 4000*self.__nombre
        else:
            print("Type incorrect")
            totalBrut = 0
        return totalBrut
    
    def calculerRemise(self):
        totalBrut = self.calculerPrixBrut()
        if totalBrut >= 2500 :
            if totalBrut <= 4500 :
                remise = 0.23 * totalBrut
            else:
                remise = 0.32 * totalBrut
        
        return remise
    

    def calculerPrixNet(self):
        return self.calculerPrixBrut() - self.calculerRemise()


com1 = Commande("i3",3)

print(com1.calculerPrixBrut())
print(com1.calculerRemise())
print(f" total : {com1.calculerPrixNet()}")
        
    