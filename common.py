import random, os, sys, time

from board import *
from properties import *
from players import player
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

def shuffle_cards(diction):
        l = list(diction.items())
        random.shuffle(l)
        diction = dict(l)
        return diction

def rich_enough(price, balance):
    if price <= balance:
        return True
    elif price > balance:
        return False
    else:
        print('Err: common.rich_enough')

def unowned(current_player, board):
    space = current_player.space
    print(f'Space = {space}')
    suf_bal = rich_enough(board[space].value,current_player.balance)
    if suf_bal == True:
        user_in = input(f'This property is unowned! Would you like to purchase it for ${board[current_player.space].value}?\nYES or NO :')
        while True:
            if user_in.upper() == 'YES':
                current_player.balance -= board[space].value
                board[space].owner = current_player.num
                print(f'Congratulations! You\'ve bought {board[space].name}')
                return current_player, board
            elif user_in.upper() == 'NO':
                print('Maybe next time!')
                return current_player, board
            else:
                user_in = input('Please enter a YES or NO :')
    else:
        print('Looks like you don\'t have enough for this property! Maybe next time')
        return current_player, board

def owned(current_player, board, player_list):
    print('Uh oh, pay up along with some really cool ascii graphics')
    return current_player, board, player_list
    
def home_turf():
    print('You own this! Safe and sound')
    return
    
