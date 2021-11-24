import random, sys, os, time

from board import board
from properties import property
from events import event


def main():
    game_board = board.board_init() #(self, name, value, rent, num_of_houses, owner) OR (self, name, ID)
    event_index = event.events_dict_init()

    for x in range(len(game_board)):
        print(game_board[x].name)
        
    event.event_call(0, event_index)
    
if __name__ == '__main__':
    main()
else:
    print(f'__name__ != __main__ @{os.getcwd()}')