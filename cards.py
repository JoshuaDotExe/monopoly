import random

from players import player

class card:
    def __init__ (self, name, ID):          #Community Chest ID = 1, Chance ID = 2
        self.name = name
        self.ID = ID

    def com_chest_init():                   #p_bal, p_space, p_in_jail, board, player_list
        def adv_2_go(current_player, board, player_list):
            print('Advance to GO!')
            current_player.space = 0
            current_player.balance += 400
            return current_player, board, player_list
        def bnk_err(current_player, board, player_list):
            print('There was a bank error in your favour! Collect $200!')
            current_player.balance =+ 200
            return current_player, board, player_list
        def doc_fee(current_player, board, player_list):
            print('Pay doctor\'s fees of $50')
            current_player.balance -= 50
            return current_player, board, player_list
        def go_jail(current_player, board, player_list):
            print('Go Straight to jail! Do not pass go and do not collect $200!')
            current_player.space = 10
            current_player.is_jailed = True
            return current_player, board, player_list
        def beau_cont(current_player, board, player_list):
            print('You\'ve won a beauty contest! Collect $10!')
            current_player.balance += 10
            return current_player, board, player_list
        def sale_of_stock(current_player, board, player_list):
            print('You\'ve made a profit from selling stocks! Collect $50!')
            current_player.balance += 50
            return current_player, board, player_list
        def grnd_op(current_player, board, player_list):
            print('You host a grand opera night! Collect $50 from every player!')       #Implement collecting func here
            num_players = len(player_list)
            current_player.balance += 50*num_players
            for x in player_list:
                if current_player !=x:
                    x.balance -= 50
                else:
                    pass
                pass
            return current_player, board, player_list
        def holiday_fund(current_player, board, player_list):
            print('Your holiday fund matures, collect $100!')
            current_player.balance += 100
            return current_player, board, player_list
        def tax_ref(current_player, board, player_list):
            print('You get a tax refund! Collect $20!')
            current_player.balance += 20
            return current_player, board, player_list
        def brth_d(current_player, board, player_list):
            print('It\'s your birthday! Collect $10 from every player!')                 #Implement collecting func here
            num_players = len(player_list)
            current_player.balance += 10*num_players
            for x in player_list:
                if current_player !=x:
                    x.balance -= 10
                else:
                    pass
                pass
            return current_player, board, player_list
        def life_ins(current_player, board, player_list):
            print('Life insurance premiums increase, pay $100')
            current_player.balance -= 100
            return current_player, board, player_list
        def hosp_fee(current_player, board, player_list):
            print('Hospital fees come due! Pay $50')
            current_player.balance -= 50
            return current_player, board, player_list
        def school_fee(current_player, board, player_list):
            print('A new school term starts, pay $50 in school fees')
            current_player.balance -= 50
            return current_player, board, player_list
        def consult_fee(current_player, board, player_list):
            print('A new school term starts, pay $50 in school fees')
            current_player.balance -= 50
            return current_player, board, player_list
        def str_repairs(current_player, board, player_list):                                                            #Implement house num collecting func here
            print('You\'ve been made liable for street repair infront of your buildings, pay $25 per house and $50 per hotel!')
            total = 0
            for space in board:
                if type(space) == property and space.owner == current_player.player_num:
                    if space.num_of_houses < 5 and space.num_of_houses > 0:
                        total += space.num_of_houses*25
                    elif space.num_of_houses == 5:
                        total += 100
                    else:
                        pass
                else:
                    pass
            current_player.balance -= total
            return current_player, board, player_list    
        cc_cards = {
            1 : adv_2_go,
            2 : bnk_err,
            3 : doc_fee,
            4 : sale_of_stock,
            5 : beau_cont,
            6 : go_jail,
            7 : grnd_op,
            8 : holiday_fund,
            9 : tax_ref,
            10 : brth_d,
            11 : life_ins,
            12 : hosp_fee,
            13 : school_fee,
            14 : consult_fee,
            15 : str_repairs
            }
        return cc_cards
    def chance_init():
        def adv_2_go(current_player, board, player_list):
            print('Advance to GO!')
            current_player.space = 0
            current_player.balance += 400
            return current_player, board, player_list
        def adv_2_24(current_player, board, player_list):
            print('Advance to Red 3')
            current_player.space = 0
            return current_player, board, player_list
        def adv_2_11(current_player, board, player_list):
            print('Advance to Pink 1')
            current_player.space = 11
            return current_player, board, player_list
        def adv_2_util(current_player, board, player_list):
            print('Advance to the nearest utility! If a player owns it pay 10 times your dice roll!')
            if current_player.space > 12 and current_player.space < 28:
                current_player.space = 28
            else:
                current_player.space = 12
            return current_player, board, player_list
        def adv_2_rail(current_player, board, player_list):
            print('Advance to the nearest Railway Station')
            if current_player.space>35 and current_player.space<5:
                current_player.space = 5
            elif current_player.space>5 and current_player.space<15:
                current_player.space = 15
            elif current_player.space>15 and current_player.space<25:
                current_player.space = 25
            elif current_player.space>25 and current_player.space<35:
                current_player.space = 35
            else:
                print('Invalid rail search')
            return current_player, board, player_list
        def bnk_div(current_player, board, player_list):
            print('The bank pays your dividend! Collect $50!')
            current_player.balance += 50
            return current_player, board, player_list
        def croswrd_comp(current_player, board, player_list):
            print('You win a crossword competition! Collect $100!')
            current_player.balance += 100
            return current_player, board, player_list
        def go_back_3(current_player, board, player_list):
            print('Go back 3 spaces!')
            current_player.space -= 3
            return current_player, board, player_list
        def head_jail(current_player, board, player_list):
            print('Go Straight to jail! Do not pass go and do not collect $200!')
            current_player.space = 10
            current_player.is_jailed = True
            return current_player, board, player_list
        def build_repairs(current_player, board, player_list):                                    #Implement house num collecting func here
            print('Your buildings have become run down, pay $25 per house and $50 per hotel to renovate!')
            total = 0
            for space in board:
                if type(space) == property and space.owner == current_player.player_num:
                    if space.num_of_houses < 5 and space.num_of_houses > 0:
                        total += space.num_of_houses*25
                    elif space.num_of_houses == 5:
                        total += 100
                    else:
                        pass
                else:
                    pass
            current_player.balance -= total
            return current_player, board, player_list 
        def poor_tax(current_player, board, player_list):
            print('The IRS has caught up with your tax evasion, pay $15 in poor people taxes')
            current_player.balance -= 15
            return current_player, board, player_list
        def adv_2_5(current_player, board, player_list):
            print('Advance to Rail 1!')
            current_player.space = 5
            return current_player, board, player_list
        def adv_2_39(current_player, board, player_list):
            print('Advance to Dark Blue 1!')
            current_player.space = 39
            return current_player, board, player_list
        def pay_50_2all(current_player, board, player_list):
            print('You\'ve been elected chairman of the board! Pay out $50 to each player in bribes')   #Implement collecting func here
            num_players = len(player_list)
            current_player.balance -= 50*num_players
            for x in player_list:
                if current_player !=x:
                    x.balance += 50
                else:
                    pass
                pass
            return current_player, board, player_list
        def build_loan(current_player, board, player_list):
            print('Your building loan matures, collect $150!')
            current_player.balance += 150
            return current_player, board, player_list        
        chn_cards = {
            1 : adv_2_go,
            2 : adv_2_24,
            3 : adv_2_11,
            4 : adv_2_util,
            5 : adv_2_rail,
            6 : bnk_div,
            7 : croswrd_comp,
            8 : go_back_3,
            9 : head_jail,
            10 : build_repairs,
            11 : poor_tax,
            12 : adv_2_5,
            13 : adv_2_39,
            14 : pay_50_2all,
            15 : build_loan
        }
        return chn_cards