

class player:
    def __init__(self, player_num, name, balance, rent, space, is_jailed):
        self.player_num = player_num
        self.name = name
        self.balance = balance
        self.rent = rent
        self.space = space
        self.owner = is_jailed
        