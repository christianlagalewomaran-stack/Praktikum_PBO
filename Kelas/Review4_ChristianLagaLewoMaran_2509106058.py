class hero:
    def __init__(self, nama, health, attack):
        self.nama = nama
        self.health = health
        self.attack = attack
        
    def serang(self, target):
        print(f"{self.nama} menyerang {target.nama}")
        
class mage(hero):
    def __init__(self, nama, health, attack, mana= 100):
        super().__init__(nama, health, attack)
        self.mana = mana
        
    def serang(self, target):
        print(f"{self.nama} menyerang musuh dengan magis {target.nama}")
        
class assasin(hero):
    def __init__(self, nama, health, attack, mana= 100):
        super().__init__(nama, health, attack)
        self.mana = mana
        
class doubleRole(mage, assasin):
    def __init__(self, nama, health, attack, mana, jarak):
        super().__init__(nama, health, attack, mana)
        self.jarak = jarak
        
    def serang(self, target):
        return super().serang(target)
        
class assasinEnergy(assasin):
    def __init__(self, nama, health, attack, mana, energy):
        super().__init__(nama, health, attack, mana)
        self.energy = energy
        
    def serang(self, target):
        print(f"{self.nama} menyerang {target.nama} menggunakan energy")

balmond = hero("balmond", 1000, 10)
eudora = mage("eudora", 500, 10, 100)
fanny = assasinEnergy("fanny", 1500, 250, 0, 100)
karina = doubleRole("karina", 1000, 250, 100, 5)

balmond.serang(eudora)
eudora.serang(balmond)
fanny.serang(balmond)
karina.serang(balmond)