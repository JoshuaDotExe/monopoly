import random

from players import player

class card:
    def __init__ (self, name, ID):          #Community Chest ID = 1, Chance ID = 2
        self.name = name
        self.ID = ID

    def __repr__(self):
        return "Card : {}".format(self.name)
    
    def com_chest_init():                   #p_bal, p_space, p_in_jail, board, player_list
        def adv_2_go(p, board, player_list):
            print('Advance to GO!')
            p.space = 0
            return p, board, player_list

        def bnk_err(p, board, player_list):
            print('There was a bank error in your favour! Collect $200!')
            p = player.bal_plus(p, 200)
            return p, board, player_list
        
        def doc_fee(p, board, player_list):
            print('Pay doctor\'s fees of $50')
            p = player.bal_minus(p, 50)
            return p, board, player_list
        
        def go_jail(p, board, player_list):
            print('Go Straight to jail! Do not pass go and do not collect $200!')
            p.space = 10
            p.is_jailed = True
            return p, board, player_list
        
        def beau_cont(p, board, player_list):
            print('You\'ve won a beauty contest! Collect $10!')
            p = player.bal_plus(p, 10)
            return p, board, player_list
        def sale_of_stock(p, board, player_list):
            print('You\'ve made a profit from selling stocks! Collect $50!')
            p = player.bal_plus(p, 50)
            return p, board, player_list
        def grnd_op(p, board, player_list):
            print('You host a grand opera night! Collect $50 from every player!')       #Implement collecting func here
            num_players = len(player_list)
            p = player.bal_plus(p, (50*num_players))
            for x in player_list:
                if p != x:
                    x.balance -= 50
                else:
                    pass
                pass
            return p, board, player_list
        def holiday_fund(p, board, player_list):
            print('Your holiday fund matures, collect $100!')
            p = player.bal_plus(p, 100)
            return p, board, player_list
        def tax_ref(p, board, player_list):
            print('You get a tax refund! Collect $20!')
            p = player.bal_plus(p, 20)
            return p, board, player_list
        def brth_d(p, board, player_list):
            print('It\'s your birthday! Collect $10 from every player!')                 #Implement collecting func here 
            p = player.bal_plus(p, (10*(len(player_list)-1)))
            gift_list = player_list
            del gift_list[p.num]
            for x in gift_list:
                x = player.bal_minus(x, 10)
            return p, board, player_list
        def life_ins(p, board, player_list):
            print('Life insurance premiums increase, pay $100')
            p = player.bal_plus(p, 100)
            return p, board, player_list
        def hosp_fee(p, board, player_list):
            print('Hospital fees come due! Pay $50')
            p = player.bal_minus(p, 50)
            return p, board, player_list
        def school_fee(p, board, player_list):
            print('A new school term starts, pay $50 in school fees')
            p = player.bal_minus(p, 50)
            return p, board, player_list
        def consult_fee(p, board, player_list):
            print('A new school term starts, pay $50 in school fees')
            p = player.bal_minus(p, 50)
            return p, board, player_list
        def str_repairs(p, board, player_list):                                                            #Implement house num collecting func here
            print('You\'ve been made liable for street repair infront of your buildings, pay $25 per house and $50 per hotel!')
            total = 0
            for space in board:
                if type(space) == property and space.owner == p.player_num:
                    if space.num_of_houses < 5 and space.num_of_houses > 0:
                        total += space.num_of_houses*25
                    elif space.num_of_houses == 5:
                        total += 100
                    else:
                        pass
                else:
                    pass
            p = player.bal_minus(p, total)
            return p, board, player_list    
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
        cc_cards = card.randomize(cc_cards)
        return cc_cards
    def chance_init():
        def adv_2_go(p, board, player_list):
            print('Advance to GO!')
            p.space = 0
            return p, board, player_list
        def adv_2_24(p, board, player_list):
            print('Advance to Red 3')
            p.space = 0
            return p, board, player_list
        def adv_2_11(p, board, player_list):
            print('Advance to Pink 1')
            p.space = 11
            return p, board, player_list
        def adv_2_util(p, board, player_list):
            print('Advance to the nearest utility! If a player owns it pay 10 times your dice roll!')
            if p.space > 12 and p.space < 28:
                p.space = 28
            else:
                p.space = 12
            return p, board, player_list
        def adv_2_rail(p, board, player_list):
            print('Advance to the nearest Railway Station')
            if p.space>35 and p.space<5:
                p.space = 5
            elif p.space>5 and p.space<15:
                p.space = 15
            elif p.space>15 and p.space<25:
                p.space = 25
            elif p.space>25 and p.space<35:
                p.space = 35
            else:
                print('Invalid rail search')
            return p, board, player_list
        def bnk_div(p, board, player_list):
            print('The bank pays your dividend! Collect $50!')
            p.balance += 50
            return p, board, player_list
        def croswrd_comp(p, board, player_list):
            print('You win a crossword competition! Collect $100!')
            p.balance += 100
            return p, board, player_list
        def go_back_3(p, board, player_list):
            print('Go back 3 spaces!')
            p.space -= 3
            return p, board, player_list
        def head_jail(p, board, player_list):
            print('Go Straight to jail! Do not pass go and do not collect $200!')
            p.space = 10
            p.is_jailed = True
            return p, board, player_list
        def build_repairs(p, board, player_list):                                    #Implement house num collecting func here
            print('Your buildings have become run down, pay $25 per house and $50 per hotel to renovate!')
            total = 0
            for space in board:
                if type(space) == property and space.owner == p.player_num:
                    if space.num_of_houses < 5 and space.num_of_houses > 0:
                        total += space.num_of_houses*25
                    elif space.num_of_houses == 5:
                        total += 100
                    else:
                        pass
                else:
                    pass
            p.balance -= total
            return p, board, player_list 
        def poor_tax(p, board, player_list):
            print('The IRS has caught up with your tax evasion, pay $15 in poor people taxes')
            p.balance -= 15
            return p, board, player_list
        def adv_2_5(p, board, player_list):
            print('Advance to Rail 1!')
            p.space = 5
            return p, board, player_list
        def adv_2_39(p, board, player_list):
            print('Advance to Dark Blue 1!')
            p.space = 39
            return p, board, player_list
        def pay_50_2all(p, board, player_list):
            print('You\'ve been elected chairman of the board! Pay out $50 to each player in bribes')   #Implement collecting func here
            num_players = len(player_list)
            p.balance -= 50*num_players
            for x in player_list:
                if p !=x:
                    x.balance += 50
                else:
                    pass
                pass
            return p, board, player_list
        def build_loan(p, board, player_list):
            print('Your building loan matures, collect $150!')
            p.balance += 150
            return p, board, player_list        
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
        chn_cards = card.randomize(chn_cards)
        return chn_cards
    
    def randomize(dictionary):
        rand_list = []
        for key in dictionary:
            rand_list.append(key)
        random.shuffle(rand_list)
        print(rand_list)
        out_dictionary = {}
        for key in dictionary:
            out_dictionary[key] = dictionary[rand_list[key-1]]
        return out_dictionary
    