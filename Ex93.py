class Evenement :
    def _init_(self, typeEve , avecPhotographe, avecDecoration ):
        self.__typeEve = typeEve
        self.__avecPhotographe = avecPhotographe
        self.__avecDecoration = avecDecoration
    
    def calculerPrixBase (self) :
        if self.__typeEve =="anniversaire" :
            PrixBase = 2000
        elif self.__typeEve == "mariage" :
            PrixBase = 5000
        elif self.__typeEve == "conference" :
            PrixBase = 3000
        
    def calculerCoutSup (self):
        CoutSup = 0
        if self.__avecPhotographe :
            CoutSup = 800
        
        if self.__avecDecoration :
            CoutSup +=  1200
        
        return CoutSup
    
    def afficherTotal(self) :
        return self.calculerPrixBase() + self.calculerCoutSup()
     
eve1 = Evenement("anniversaire", True, False)
print(eve1.calculerPrixBase())
print(eve1.calculerCoutSup())
print(f"Total est:{eve1.afficherTotal} DH")