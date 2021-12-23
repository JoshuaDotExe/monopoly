import random

class player:
    def __init__(self, num, name, balance, space, jailStats): #player num, name, balance, rent, space, is_jailed
        self.num = num
        self.name = name
        self.balance = balance
        self.space = space
        self.jailStats = jailStats
    
    def __repr__(self):
        return "Player {}'s Name : {}, Balance ${}, Space = {}, Jail Stats = {}".format(self.num, self.name, self.balance, self.space, self.jailStats)
    
    def debug_player_list():
        player1 = player(1, 'John', 1500, 0, 0)      #player num, name, balance, space, jailStats
        player2 = player(2, 'Adam', 1500, 0, 0)
        player3 = player(3, 'Clare', 1500, 0, 0)
        player4 = player(4, 'Mohammed', 1500, 0, 0)
        player5 = player(5, 'Lexes', 1500, 0, 0)
        player6 = player(6, 'Jake', 1500, 0, 0)
        p_list = {
            1 : player1,
            2 : player2,
            3 : player3,
            4 : player4,
            5 : player5,
            6 : player6
        }
        return p_list
    
    def balSub(p, change):
        print(f'{p.name}\'s balance = ${p.balance} - ${change} = ${p.balance - change}')
        p.balance -= change
        
    def balAdd(p, change):
        print(f'{p.name}\'s balance = ${p.balance} + ${change} = ${p.balance + change}')
        p.balance += change
    
    def jailer(p):
        print('Go straight to jail! Do not pass go and do not collect $200')
        p.jailStats = 1
    
    def spaceMove(p, int):
        p.space += int
        if p.space > 39:
            p.space = p.space%40
            print('Passed GO! Received $200')
            player.balAdd(p, 200)