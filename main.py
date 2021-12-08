import random, sys, os, time
from board import board
from properties import property
from events import util_event, event, rail_event
from players import player
from cards import card

def main():
    game_board = board.board_init() #(self, name, value, rent, num_of_houses, owner) OR (self, name, ID)
    event_index = event.diction()
    player_list = player.debug_player_create()
    community_chest_index, chance_index = card.com_chest_init(), card.chance_init()
    print('All dependencies loaded, program starting...\n')
    
    while True:
        if len(player_list) == 1:
            break
        else:
            for x in player_list:         #Grabs player data
                p = player_list[x]
                playercmd = input(f'Player {p.num}/{p.name}!\n    Position = {game_board[p.space].name}\n    Balance = ${p.balance}\nWhat would you like to do?\nROLL or TRADE or BUILD or HELP : ')
                while True: #using break ends the turn
                    if playercmd.upper() == 'ROLL':
                        
                        roll_total = 0
                        die1, die2 = random.randint(1,6), random.randint(1,6)
                        roll_total += die1 + die2
                        if die1 == die2:
                            print(f'Double {die1}!')
                            die1, die2 = random.randint(1,6), random.randint(1,6)
                            roll_total += die1 + die2
                            if die1 == die2:
                                print(f'Double {die1}!')
                                die1, die2 = random.randint(1,6), random.randint(1,6)
                                roll_total += die1 + die2
                                if die1 == die2:
                                    print(f'Double {die1}!? That\'s a double too many!')
                                    p.space, p.is_jailed = event.jailer()
                                    break
                                else:
                                    print(f'Rolled a {die1} and a {die2}')
                            else:
                                print(f'Rolled a {die1} and a {die2}')
                        else:
                            print(f'Rolled a {die1} and a {die2}')
                        
                        p.space += roll_total
                        if p.space != p.space%40:
                            print('Passed GO! Collect $200!')
                            p.space = p.space%40
                            p = player.bal_plus(p, 200)
                        else:
                            pass
                        
                        if type(game_board[p.space]) is card: 
                            if game_board[p.space].ID == 2:     #Allows for the chance space chance cards to work
                                print('Landed on Chance! Pick up a card!')
                                p, game_board, player_list = chance_index[1](p, game_board, player_list)
                            if game_board[p.space].ID == 1:
                                print('Landed on Community Chest! Pick up a card!')
                                p, game_board, player_list = community_chest_index[1](p, game_board, player_list)
                            else:
                                pass
                        
                        print(f'Landed on {game_board[p.space].name}')
                        
                        if type(game_board[p.space]) is property:
                            p, game_board, player_list = property.landed(p, game_board, player_list)
                        
                        elif type(game_board[p.space]) is event:
                            p = event_index[p.space](p)
                            
                        elif type(game_board[p.space]) is rail_event:
                            p, game_board, player_list = rail_event.rail_call(p, game_board, player_list)
                        elif type(game_board[p.space]) is util_event:
                            p, game_board, player_list = util_event.util_call(p, game_board, player_list, roll_total)
                            
                        else:
                            print('Something\'s gone very wrong here')
                        print('\n')
                        print(game_board[p.space])
                        break
                            
                    elif playercmd.upper() == 'TRADE':
                        print('Func not implemented yet')
                        break
                    elif playercmd.upper() == 'BUILD':
                        print('Func not implemented yet')
                        break
                    elif playercmd.upper() == 'HELP':
                        print('Func not implemented yet')
                        break
                    else:
                        playercmd = input('Please enter ROLL or TRADE or BUILD or HELP : ')
                print('----------------------------------------\n\n----------------------------------------')



if __name__ == '__main__':
    main()
else:
    print(f'__name__ != __main__ @{os.getcwd()}')