#encapsulation
class Hero:
    jumlah = 0
 
    def __init__(self, name, health):
        self.__name = name
        self.__health = health
 
    #getter
    def getname(self):
        return self.__name
    
    def gethealth(self):
        return self.__health
    
    #setter
    def diserang(self, attserang):
        self.__health -= attserang
    
    
#instansiasi objek
lina = Hero("Lina", 10)
#cetak privat 
print(lina.getname())
print(lina.gethealth())
lina.diserang(5)
print(lina.gethealth())
