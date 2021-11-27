import random, sys, os, time

from board import board
from properties import property
from events import event
from players import *
from common import *
from cards import card

def main():
    game_board = board.board_init() #(self, name, value, rent, num_of_houses, owner) OR (self, name, ID)
    event_index = event.diction()
    ownable_event_index = ownable_event.diction()
    p_list = debug_player_create()
    community_chest_index, chance_index = card.com_chest_init(), card.chance_init()
    
    p_num = 1
    p_bal = p_list[p_num].balance
    p_name = p_list[p_num].name
    p_space = p_list[p_num].space
    p_space_name = game_board[p_list[p_num].space].name
    p_in_jail = p_list[p_num].is_jailed
    current_p = p_list[p_num]
    
    print(f'Current position = {p_space_name}')
    playercmd = input(f'Player {p_num}/{p_name}! What would you like to do?\nROLL or TRADE or BUILD or HELP :')
    while True:
        if playercmd.upper() == 'ROLL':
            p_in_jail, roll_total = roll()
            if p_in_jail == True:
                return
            else:
                p_space += roll_total
            print(f'Landed on : {game_board[p_space].name}')
            if type(game_board[p_space]) is property:
                print('Property!')
            elif type(game_board[p_space]) is event:
                event_index[p_space](p_bal,p_in_jail,p_space,p_num)
            elif type(game_board[p_space]) is card:
                if game_board[p_space].ID == 1:
                    community_chest_index[1]
                else:
                    chance_index[1]
            elif type(game_board[p_space]) is ownable_event:
                ownable_event_index[p_space]()
            else:
                print('Something\'s gone very wrong here')
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
            playercmd = input('Please enter ROLL or TRADE or BUILD or HELP :')
        
    
if __name__ == '__main__':
    main()
else:
    print(f'__name__ != __main__ @{os.getcwd()}')