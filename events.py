import random

from players import player
from properties import property

class event:
    def __init__(self, name, ID):
        self.name = name
        self.ID = ID
    
    def __repr__(self):
        return "Event : {}, ID : {}".format(self.name, self.ID)
    
    def diction():
        def go(p):
            print('Collect $400!')
            p = player.bal_plus(p, 400)
            return p
        
        def jail(current_player):
            if current_player.is_jailed == 0:
                print("You're just visiting!")
                return current_player
             
            else:
                
                def jail_pay(current_player):
                    current_player = player.bal_minus(current_player, 50)
                    current_player.is_jailed = 0
                    print('Much obliged, you\'re free to go!')
                    return current_player
                def jail_roll(current_player):
                    print('Good luck getting those doubles!')    
                    die1 = random.randint(1,6)
                    die2 = random.randint(1,6)
                    if die1 == die2:
                        print(f'Double {die1}!\nYou\'re free to go!')
                        current_player.is_jailed = False
                    else:
                        print(f'Rolled a {die1} and a {die2}\nYou have {4-current_player.is_jailed} more turns left in your sentence!') #Should add 3 turn rule by turning is_jailed into an int
                        current_player.is_jailed += 1
                        if current_player.is_jailed == 4:
                            current_player.is_jailed = 0
                            print('You\'ve served your sentence, you\'re free to go!')
                    return current_player
                
                prison_options = {
                    'PAY' : jail_pay,
                    'ROLL' : jail_roll
                }
                print('Pay the fine or serve your sentence!!')
                user_in = input('Type in PAY or ROLL :')
                while True:
                    if user_in.upper in prison_options:
                        current_player = prison_options[user_in.upper](current_player)
                        break
                    else:
                        print('Please input PAY or ROLL')
                return current_player
                
                          
        def free_prk(current_player):
            print('Woo! Free Parking!')
            return current_player
        
        def go_2_jail(current_player):
            current_player = event.jailer()
            return current_player
        def in_tax(current_player):
            print('Pay $200 in income taxes!')
            current_player = player.bal_minus(current_player, 200)
            return current_player
        def lib_tax(current_player):
            print('Pay $100 in taxes!')
            current_player = player.bal_minus(current_player, 100)
            return current_player
        event_index = {
            0 : go,
            4 : in_tax,
            38 : lib_tax,
            10 : jail,
            20 : free_prk,
            30 : go_2_jail
        }
        return event_index
    
    def jailer(p):
        print('Go straight to jail! Do not pass go and do not collect $200!')
        p.space = 10
        p.is_jailed = 1
        return p

class rail_event:
    def __init__(self, name, ID, value, owner, rent, num_of_houses):
        self.name = name
        self.ID = ID
        self.value = value
        self.owner = owner
        self.rent = rent
        self.num_of_houses = num_of_houses
    
    def __repr__(self):
        return "Property : {}\nPrice ${}, Rent {}\nHouses = {}, Owner = Player {}".format(self.name, self.value, self.rent, self.num_of_houses, self.owner)
    
    def rail_call(p, board, player_list):
        if board[p.space].owner == 0:
            if board[p.space].value <= p.balance:
            
                def buy(p, board, player_list):
                    print(f'Balance = ${p.balance} - ${board[p.space].value} = ${p.balance - board[p.space].value}\nCongratulations! You\'ve bought {board[p.space].name}')
                    p.balance -= board[p.space].value
                    board[p.space].owner = p.num
                    return p, board, player_list
                def no_buy(p, board, player_list):
                    print('Maybe next time!')
                    return p, board, player_list
                
                d = {
                    'YES' : buy,
                    'NO' : no_buy
                }
                
                user_in = input(f'This property is unowned! Would you like to purchase it for ${board[p.space].value}?\nYES or NO : ')
                while True:
                    if user_in.upper() in d:
                        return d[user_in.upper()](p, board, player_list)
                    else:
                        user_in = input('Please enter a YES or NO :')
            else:
                print('Looks like you don\'t have enough for this property! Maybe next time')
        elif board[p.space].owner == p.num:
            print('You own this! Safe and sound, for now!')
        elif board[p.space].owner != p.num:
            p, board, player_list = property.owned(p, board, player_list)
        else:
            print('Owner value: Invalid')
        return p, board, player_list
        
    

class util_event:
    def __init__(self, name, ID, value, owner, num_of_houses):
        self.name = name
        self.ID = ID
        self.value = value
        self.owner = owner
        self.num_of_houses = num_of_houses
    
    def __repr__(self):
        return "Property : {}\nPrice ${}\nHouses = {}, Owner = Player {}".format(self.name, self.value, self.num_of_houses, self.owner)
    
    def util_call(p, board, player_list, roll):
        p_space = p.space
        p_num = p.num
        if board[p_space].owner == 0:
            p, board = property.unowned(p, board)
            if board[p_space].owner:
                util_owned = 0
                util_list = [board[12], board[28]]
                for x in util_list:
                    if x.owner == p_num:
                        util_owned += 1
                for x in util_list:
                    x.num_of_houses = util_owned
            else:
                pass
        elif board[p_space].owner == p_num:
            print('You own this!')
        elif board[p_space].owner != p_num:
            owner_name = player_list[board[p.space].owner].name
            if board[p.space].num_of_houses == 1:
                multiplier = 4
            elif board[p.space].num_of_houses == 2:
                multiplier = 10
            rent = multiplier * roll
            print(f'Uh oh! Looks like it\'s owned by {owner_name}')
            print(f'With a roll of {roll} and a multiplier of {multiplier}x, pay rent of ${rent} to {owner_name}!')
            if p.balance < rent:
                print('Looks like you need some more funds! Lets see if there\'s anything for you to mortgage')
                owed = p.balance - rent
                player_bal = p.balance
                p, board, owed = player.broke(p, board, owed)
                if p.balance is None:
                    rent = player_bal + (rent-owed)
                    player_list[board[p.space].owner] = player.bal_plus(player_list[board[p.space].owner], rent)
                    print(f'Player {p.num} : {p.name} is out!')
                    for x in board:
                        if x.owner == p.num:
                            x.owner, x.num_of_houses = 0, 0
                            print(f'{x.name} is now unowned!')
                        else:
                            print('They owned no properties.')
                            pass
                    del player_list[p.num]
                else:
                    print('You\'ve managed to pay off your debts! For now...')
                    p = player.bal_minus(p, rent)
                    player_list[board[p.space].owner] = player.bal_plus(player_list[board[p.space].owner], rent)
            else:
                p = player.bal_minus(p, rent)
                player_list[board[p.space].owner] = player.bal_plus(player_list[board[p.space].owner], rent)
        return p, board, player_list
    
    def util_check(current_player, board):
        num_of_telecom = 0
        l = [board[12], board[28]]
        for x in l:
            if x.owner == current_player.num:
                num_of_telecom += 1
            else:
                pass
        for x in l:
            if x.owner == current_player.num:
                x.num_of_houses = num_of_telecom
                print(f'Num telecom = {x.num_of_houses} on {x.name}')
            else:
                pass
        return current_player, board
    
    