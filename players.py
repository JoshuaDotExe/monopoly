class player:
    def __init__(self, num, name, balance, space, is_jailed): #player num, name, balance, rent, space, is_jailed
        self.num = num
        self.name = name
        self.balance = balance
        self.space = space
        self.is_jailed = is_jailed
    
    def __repr__(self):
        return "Player {}'s Name : {}, Balance ${}, Space = {}, Jailed? = {}".format(self.num, self.name, self.balance, self.space, self.is_jailed)
    
    def debug_player_create():
        player1 = player(1, 'John', 1500, 0, False)      #player num, name, balance, space, is_jailed
        player2 = player(2, 'Adam', 1500, 0, False)
        player3 = player(3, 'Clare', 1500, 0, False)
        player4 = player(4, 'Mohammed', 1500, 0, False)
        player5 = player(5, 'Lexes', 1500, 0, False)
        player6 = player(6, 'Jake', 1500, 0, False)
        p_list = {
            1 : player1,
            2 : player2,
            3 : player3,
            4 : player4,
            5 : player5,
            6 : player6
        }
        return p_list
    
    def bal_minus(p, change):
        print(f'{p.name}\'s balance = ${p.balance} - ${change} = ${p.balance - change}')
        p.balance -= change
        return p
        
    def bal_plus(p, change):
        print(f'{p.name}\'s balance = ${p.balance} + ${change} = ${p.balance + change}')
        p.balance += change
        return p
            
    
    def broke(p, game_board, owed):  #Takes in a player and finds out if they have properties, lists their properties, gives them an option of what to sell and how much it'll give them, doesn't let them stop selling till their owed is positive then returns the owned to add to their balance
        print(f'Debt = ${owed}')
        original_debt = owed
        d = {}
        total_value = 0
        for x in game_board:
            if p.num == game_board[p.space].owner:
                d[x.name] = tuple(x.value/2, game_board.index(x))
                total_value += x.value/2
            else:
                pass
        if total_value >= owed:
            name, prop_val = 'Name:', 'Mortgage Value:'
            print(f'Your owned properties are:\n{name: <12}|  ${prop_val}')
            for key in d:
                print(f'{key: <12}|  ${d[key][0]}')
            
            user_in = input('Please type the name of a property you would like to mortgage: ')
            while True:
                if user_in in d.keys():
                    game_board[d.get(user_in)[1]].owner = 0
                    print(f'Debt = ${owed} - ${d.get(user_in)[0]} = ${owed - d.get(user_in)[0]}')
                    owed -= d.get(user_in)[0]
                    game_board[d.get(user_in)[1]].owner = 0
                    if owed > 0:
                        user_in = input('Please type the name of a property you would like to mortgage: ')
                    else:
                        p.balance = abs(owed)
                        owed = original_debt
                        return p, game_board, owed
                elif user_in.upper() == 'FORFEIT':
                    print('Player gives up')
                    owed = original_debt
                    p.balance = None
                    return p, game_board, owed
                else:
                    user_in = input('Unknown name! WARNING: The names are case-sensitive!')
                    
                    
        else:
            print('Your property value is not enough! GAME OVER')
            owed = total_value
            p.balance = None
            return p, game_board, owed
        

        pass