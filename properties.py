class property:
    def __init__(self, name, value, rent, num_of_houses, owner):
        self.name = name
        self.value = value
        self.rent = rent
        self.num_of_houses = num_of_houses
        self.owner = owner
    
    def __repr__(self):
        return "Property : {}, Price ${}, Rent {}, Houses = {}, Owner = Player {}".format(self.name, self.value, self.rent, self.num_of_houses, self.owner)
    
    def getRent(prop):
        rent = prop.rent[prop.num_of_houses]
        return rent
    
    def houseCost(index, num_of_houses):
        houseBase = 50
        multiplier_adj = index/10
        value = houseBase * (1 + multiplier_adj) * num_of_houses
        return value
    