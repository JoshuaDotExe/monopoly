import random, sys, os, time

from board import board
from properties import property
from events import event, ownable_event
from players import *
from common import *
from cards import card

def main():
    game_board = board.board_init() #(self, name, value, rent, num_of_houses, owner) OR (self, name, ID)
    event_index = event.diction()
    ownable_event_index = ownable_event.diction()
    player_list = debug_player_create()
    community_chest_index, chance_index = card.com_chest_init(), card.chance_init()
    
    p_num = 1
    p_bal = player_list[p_num].balance
    p_name = player_list[p_num].name
    p_space = player_list[p_num].space
    p_space_name = game_board[player_list[p_num].space].name
    p_in_jail = player_list[p_num].is_jailed
    current_player = player_list[p_num]
    
    print(f'Current position = {p_space_name}')
    playercmd = input(f'Player {p_num}/{p_name}! What would you like to do?\nROLL or TRADE or BUILD or HELP :')
    while True:
        if playercmd.upper() == 'ROLL':
            p_in_jail, roll_total = roll()
            if p_in_jail == True:
                return
            else:
                current_player.space += roll_total
            print(f'Landed on : {game_board[current_player.space].name}')
            if type(game_board[current_player.space]) is property:
                print('This Is a property and needs more work on those functions!!')
            elif type(game_board[current_player.space]) is event:
                current_player = event_index[current_player.space](current_player)
            elif type(game_board[current_player.space]) is card:
                if game_board[current_player.space].ID == 1:
                    current_player, game_board, player_list = community_chest_index[1](current_player, game_board, player_list)
                elif game_board[current_player.space].ID == 2:
                    current_player, game_board, player_list = chance_index[1](current_player, game_board, player_list)
                else:
                    print('Didnt work :(')
                    pass
            elif type(game_board[current_player.space]) is ownable_event:
                ownable_event_index[current_player.space](current_player, game_board, player_list)
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