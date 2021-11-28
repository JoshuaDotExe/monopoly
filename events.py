import random
from cards import card
from common import owned, unowned, home_turf

class event:
    def __init__(self, name, ID):
        self.name = name
        self.ID = ID
        
    def diction():              #p_bal, p_in_jail, p_space
        def go(current_player):
            print('Collect $400!')
            current_player.balance += 400
            return current_player
        
        def jail(current_player):
            if current_player.is_jailed == False:
                print("You're just visiting!")
                return current_player
            else:
                print('Pay the fine or serve your sentence!!')
                current_player.is_jailed = True
                fin = False
                while fin == False:
                    user_in = input('Type in PAY or ROLL :')
                    if user_in.upper == 'PAY':
                        current_player.balance -= 50
                        fin = True
                        current_player.is_jailed = False
                        print('Much obliged, you\'re free to go!')
                        return current_player
                    elif user_in.upper == 'ROLL':
                        print('Good luck getting those doubles!')    
                        fin = True
                        die1 = random.randint(1,6)
                        die2 = random.randint(1,6)
                        if die1 == die2:
                            print(f'Double {die1}!\nYou\'re free to go!')
                            current_player.is_jailed = False
                            return current_player
                        else:
                            print(f'Rolled a {die1} and a {die2}\nLooks like you\'ll be staying here a while longer!') #Should add 3 turn rule by turning is_jailed into an int
                            return current_player
                    else:
                        print('Please input PAY or ROLL')
                          
        def free_prk(current_player):
            print('Woo! Free Parking!')
            return current_player
        
        def go_2_jail(current_player):
            print('Go Straight to jail! Do not pass go and do not collect $200!')
            current_player.space = 10
            current_player.is_jailed = True
            return current_player
        def in_tax(current_player):
            print('Pay $200 in income taxes!')
            current_player.balance -= 200
            return current_player
        def lib_tax(current_player):
            print('Pay $100 in taxes!')
            current_player.balance -= 100
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
    
class ownable_event:
    def __init__(self, name, ID, value, owner, num_of_houses):
        self.name = name
        self.ID = ID
        self.value = value
        self.owner = owner
        self.num_of_houses = num_of_houses
    
    def diction():
        def rail1(current_player, board, player_list):
            if board[5].owner == 0:
                current_player, board = unowned(current_player, board)
                if board[5].owner == current_player.num:
                    current_player, board = ownable_event.rail_check(current_player, board)
                else:
                    pass
                return current_player, board, player_list
            elif board[5].owner == current_player.num:
                home_turf()
            elif board[5].owner != current_player.num:
                current_player, board, player_list = owned(current_player, board, player_list)
                return current_player, board, player_list
            else:
                print('Owner value: Invalid')
                return current_player, board, player_list 
        
        def rail2(current_player, board, player_list):
            if board[15].owner == 0:
                current_player, board = unowned(current_player, board)
                if board[15].owner == current_player.num:
                    current_player, board = ownable_event.rail_check(current_player, board)
                else:
                    pass
                return current_player, board, player_list
            elif board[15].owner == current_player.num:
                home_turf()
            elif board[15].owner != current_player.num:
                current_player, board, player_list = owned(current_player, board, player_list)
                return current_player, board, player_list
            else:
                print('Owner value: Invalid')
                return current_player, board, player_list
        
        def rail3(current_player, board, player_list):
            if board[25].owner == 0:
                current_player, board = unowned(current_player, board)
                if board[25].owner == current_player.num:
                    current_player, board = ownable_event.rail_check(current_player, board)
                else:
                    pass
                return current_player, board, player_list
            elif board[25].owner == current_player.num:
                home_turf()
            elif board[25].owner != current_player.num:
                current_player, board, player_list = owned(current_player, board, player_list)
                return current_player, board, player_list
            else:
                print('Owner value: Invalid')
                return current_player, board, player_list
        
        def rail4(current_player, board, player_list):
            if board[35].owner == 0:
                current_player, board = unowned(current_player, board)
                if board[35].owner == current_player.num:
                    current_player, board = ownable_event.rail_check(current_player, board)
                else:
                    pass
                return current_player, board, player_list
            elif board[35].owner == current_player.num:
                home_turf()
            elif board[35].owner != current_player.num:
                current_player, board, player_list = owned(current_player, board, player_list)
                return current_player, board, player_list
            else:
                print('Owner value: Invalid')
                return current_player, board, player_list
        
        def telecom_1(current_player, board, player_list):
            if board[12].owner == current_player.num:
                home_turf()
                return current_player, board, player_list
            elif board[12].owner == 0:
                current_player, board = unowned(current_player, board)
                return current_player, board, player_list
            else:
                print('Owner value: Invalid')
                return current_player, board, player_list
        
        def telecom_2(current_player, board, player_list):
            if board[28].owner == current_player.num:
                home_turf()
                return current_player, board, player_list
            elif board[28].owner == 0:
                current_player, board = unowned(current_player, board)
                return current_player, board, player_list
            else:
                print('Owner value: Invalid')
                return current_player, board, player_list
    
        ownable_event_index = {
            5 : rail1,
            12: telecom_1,
            15: rail2,
            25: rail3,
            28: telecom_2,
            35: rail4
        }
        return ownable_event_index
        
    def rail_check(current_player, board):
        num_of_rails = 0
        l = [board[5], board[15], board[25], board[35]]
        for x in l:
            if x.owner == current_player.num:
                num_of_rails += 1
            else:
                pass
        for x in l:
            if x.owner == current_player.num:
                x.num_of_houses = num_of_rails
                print(f'Num rails = {x.num_of_houses} on {x.name}')
            else:
                pass
        return current_player, board
            
        
        
        
        
        
    
    