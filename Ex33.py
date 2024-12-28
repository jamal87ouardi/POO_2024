class Client :
    def __init__(self, consommation):
        self.__consommation = consommation

    def calculerTotal(self):
        if(self.__consommation <= 4):
            total = self.__consommation*40.5
        else:
            total = self.__consommation*60.0

        return total
    
c= float(input("Entrer la consommation"))

ayman = Client(c)

print(f"total : {ayman.calculerTotal()}")