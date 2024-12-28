class Reservation:
    
    
    def __init__(self,typeCH, nuite, avecPD, personnes):
        self.__typeCH = typeCH
        self.__nuite = nuite
        self.__avecPD = avecPD
        self.__personnes = personnes

    def calculerPrixTotal(self):
        if self.__typeCH == "Simple":
            Total = 240*self.__nuite
        elif self.__typeCH == "Double":
            Total = 340*self.__nuite
        else :
            Total = 500*self.__nuite

        if(self.__avecPD) :
            Total = Total + 40*self.__nuite*self.__personnes
        
        return Total

r = Reservation("Double",3,True, 2)
print(r.calculerPrixTotal())