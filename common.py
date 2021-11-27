import random, os, sys, time

from board import *
from properties import *
from players import *
from events import *

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

def roll():
    i=0
    roll_total = 0
    fin = False
    while fin == False:
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        dice = die1+die2
        roll_total += dice
        if die1 == die2:
            print(f'Double {die1}!')
            i += 1
            if i == 3:
                return True,roll_total
            else:
                pass
        else:
            print(f'Rolled a {die1} and a {die2}')
            return False,roll_total
        

def jailer():
    print('Go straight to jail! Do not pass go and do not collect $200!')
    player_space = 10
    return player_space