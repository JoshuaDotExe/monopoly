from players import player

class property:
    def __init__(self, name, value, rent, num_of_houses, owner):
        self.name = name
        self.value = value
        self.rent = rent
        self.num_of_houses = num_of_houses
        self.owner = owner
    
    def __repr__(self):
        return "Property : {}\nPrice ${}, Rent {}\nHouses = {}, Owner = Player {}".format(self.name, self.value, self.rent, self.num_of_houses, self.owner)
    
    def landed(current_player, game_board, player_list):
        current_owner = game_board[current_player.space].owner
        if current_owner == 0:
            current_player, game_board = property.unowned(current_player, game_board)
            if current_owner == current_player.num:
                current_player, game_board = game_board.rail_check(current_player, game_board)
            else:
                pass
        elif current_owner == current_player.num:
            game_board()
        elif current_owner != current_player.num:
            current_player, game_board, player_list = property.owned(current_player, game_board, player_list)
        else:
            print('Owner value: Invalid')
        return current_player, game_board, player_list
    
    def owned(p, board, player_list):
        owner = player_list[board[p.space].owner].name
        rent = board[p.space].rent[board[p.space].num_of_houses]
        
        print(f'Uh oh! Looks like it\'s owned by {owner}')
        print(f'With {board[p.space].num_of_houses} houses, pay rent of ${rent} to {owner}!')
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
    
    def unowned(p, board):
        if board[p.space].value <= p.balance:
            
            def buy(p, board):
                print(f'Balance = ${p.balance} - ${board[p.space].value} = ${p.balance - board[p.space].value}\nCongratulations! You\'ve bought {board[p.space].name}')
                p.balance -= board[p.space].value
                board[p.space].owner = p.num
                return p, board
            def no_buy(p, board):
                print('Maybe next time!')
                return p, board
            
            d = {
                'YES' : buy,
                'NO' : no_buy
            }
            
            user_in = input(f'This property is unowned! Would you like to purchase it for ${board[p.space].value}?\nYES or NO : ')
            while True:
                if user_in.upper() in d:
                    d[user_in.upper()](p, board)
                    return p, board
                else:
                    user_in = input('Please enter a YES or NO :')
        else:
            print('Looks like you don\'t have enough for this property! Maybe next time')
            return p, board
    
    def home_turf():
        print('You own this! Safe and sound, for now!')
        return
    