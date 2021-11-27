import random

class event:
    def __init__(self, name, ID):
        self.name = name
        self.ID = ID
        
    def diction():              #p_bal, p_in_jail, p_space
        def go(p_bal, p_in_jail, p_space, p_num):
            print('GO')
            p_bal += 400
            return p_bal, p_in_jail, p_space, p_num
        
        def jail(p_bal, p_in_jail, p_space, p_num):
            if p_in_jail == False:
                print("You're just visiting!")
                return p_in_jail, p_bal
            else:
                print('Pay the fine or serve your sentence!!')
                fin = False
                while fin == False:
                    user_in = input('Type in PAY or ROLL :')
                    if user_in.upper == 'PAY':
                        p_bal -= 50
                        fin = True
                        p_in_jail = False
                        print('Much obliged, you\'re free to go!')
                        return p_bal, p_in_jail, p_space, p_num
                    elif user_in.upper == 'ROLL':
                        print('Good luck getting those doubles!')    
                        fin = True
                        die1 = random.randint(1,6)
                        die2 = random.randint(1,6)
                        if die1 == die2:
                            print(f'Double {die1}!\nYou\'re free to go!')
                            p_in_jail = False
                            return p_bal, p_in_jail, p_space, p_num
                        else:
                            print(f'Rolled a {die1} and a {die2}\nLooks like you\'ll be staying here a while longer!')
                            return p_bal, p_in_jail, p_space, p_num
                    else:
                        print('Please input PAY or ROLL')
                          
        def free_prk(p_bal, p_in_jail, p_space, p_num):
            print('Woo! Free Parking!')
            return p_bal, p_in_jail, p_space, p_num
        
        def go_2_jail(p_bal, p_in_jail, p_space, p_num):
            print('Go Straight to jail! Do not pass go and do not collect $200!')
            p_space = 10
            p_in_jail = True
            return p_bal, p_in_jail, p_space, p_num
        
        def com_chest(p_bal, p_in_jail, p_space, p_num):
            
            def adv_2_go(p_bal):
                print('Advance to GO!')
                p_space = 0
                p_bal += 400
                return p_space, p_bal
            def bnk_err(p_bal):
                print('There was a bank error in your favour! Collect $200!')
                p_bal =+ 200
                return p_bal
            def doc_fee(p_bal):
                print('Pay doctor\'s fees of $50')
                p_bal -= 50
                return p_bal
            def go_jail(p_in_jail):
                print('Go Straight to jail! Do not pass go and do not collect $200!')
                p_space, p_in_jail = go_2_jail(p_in_jail)
                return p_space, p_in_jail
            def beau_cont(p_bal):
                print('You\'ve won a beauty contest! Collect $10!')
                p_bal += 10
                return p_bal
            def sale_of_stock(p_bal):
                print('You\'ve made a profit from selling stocks! Collect $50!')
                p_bal += 50
                return p_bal
            def grnd_op():
                print('You host a grand opera night! Collect $50 from every player!')       #Implement collecting func here
                pass
            def holiday_fund(p_bal):
                print('Your holiday fund matures, collect $100!')
                p_bal += 100
                return p_bal
            def tax_ref(p_bal):
                print('You get a tax refund! Collect $20!')
                p_bal += 20
                return p_bal
            def brth_d(p_bal):
                print('It\'s your birthday! Collect $10 from every player!')                 #Implement collecting func here
                pass
            def life_ins(p_bal):
                print('Life insurance premiums increase, pay $100')
                p_bal -= 100
                return p_bal
            def hosp_fee(p_bal):
                print('Hospital fees come due! Pay $50')
                p_bal -= 50
                return p_bal
            def school_fee(p_bal):
                print('A new school term starts, pay $50 in school fees')
                p_bal -= 50
                return p_bal
            def consult_fee(p_bal):
                print('A new school term starts, pay $50 in school fees')
                p_bal -= 50
                return p_bal
            def str_repairs(p_bal):                                                         #Implement house num collecting func here
                print('You\'ve been made liable for street repair infront of your buildings, pay $25 per house and $50 per hotel!')
                
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
            print('I really need to finish the community chest functions')
            return cc_cards
        
        def chance(p_bal, p_in_jail, p_space, p_num):
            
            def adv_2_go(p_bal):
                print('Advance to GO!')
                p_space = 0
                p_bal += 400
                return p_space, p_bal
            def adv_2_24():
                print('Advance to Red 3')
                p_space = 24
                return p_space
            def adv_2_11():
                print('Advance to Pink 1')
                p_space = 11
                return p_space
            def adv_2_util(p_space):
                print('Advance to the nearest utility! If a player owns it pay 10 times your dice roll!')
                if p_space > 12 and p_space < 28:
                    p_space = 28
                else:
                    p_space = 12
                return p_space
            def adv_2_rail(p_space):
                print('Advance to the nearest Railway Station')
                if p_space>35 and p_space<5:
                    p_space = 5
                elif p_space>5 and p_space<15:
                    p_space = 15
                elif p_space>15 and p_space<25:
                    p_space = 25
                elif p_space>25 and p_space<35:
                    p_space = 35
                else:
                    print('Invalid rail search')
                return p_space
            def bnk_div(p_bal):
                print('The bank pays your dividend! Collect $50!')
                p_bal += 50
                return p_bal
            def croswrd_comp(p_bal):
                print('You win a crossword competition! Collect $100!')
                p_bal += 100
                return p_bal
            def go_back_3(p_space):
                print('Go back 3 spaces!')
                p_space -= 3
                return p_space
            def head_jail(p_in_jail):
                'Go Straight to jail! Do not pass go and do not collect $200!'
                p_space, p_in_jail = go_2_jail(p_in_jail)
                return p_space, p_in_jail
            def build_repairs():                                    #Implement house num collecting func here
                print('Your buildings have become run down, pay $25 per house and $50 per hotel to renovate!')
                return
            def poor_tax(p_bal):
                print('The IRS has caught up with your tax evasion, pay $15 in poor people taxes')
                p_bal -= 15
                return p_bal
            def adv_2_5():
                print('Advance to Rail 1!')
                p_space = 5
                return p_space
            def adv_2_39():
                print('Advance to Dark Blue 1!')
                p_space = 39
                return p_space
            def pay_50_2all():
                print('You\'ve been elected chairman of the board! Pay out $50 to each player in bribes')   #Implement collecting func here
                return
            def build_loan(p_bal):
                print('Your building loan matures, collect $150!')
                p_bal += 150
                return p_bal
            
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
            print('I really need to finish the chance functions')
            return chn_cards
        
        def in_tax(p_bal, p_in_jail, p_space, p_num):
            print('Pay $200 in income taxes!')
            p_bal -= 200
            return p_bal, p_in_jail, p_space, p_num
        
        def lib_tax(p_bal, p_in_jail, p_space, p_num):
            print('Pay $100 in taxes!')
            p_bal -= 100
            return p_bal, p_in_jail, p_space, p_num
        event_index = {
            0 : go,
            2 : com_chest,
            7 : chance,
            4 : in_tax,
            38 : lib_tax,
            10 : jail,
            17 : com_chest,
            20 : free_prk,
            22 : chance,
            30 : go_2_jail,
            33 : com_chest,
            36 : chance
        }
        return event_index
    
class ownable_event:
    def __init__(self, name, ID, owner, num_of_houses):
        self.name = name
        self.ID = ID
        self.owner = owner
        self.num_of_houses = num_of_houses
    
    def diction():
        def rail1():
            print('I really need to finish the railway event functions')
            return 
        
        def rail2():
            print('I really need to finish the railway event functions')
            return 
        
        def rail3():
            print('I really need to finish the railway event functions')
            return 
        
        def rail4():
            print('I really need to finish the railway event functions')
            return 
        
        def telecom_1():
            print('I really need to finish the telecomms event functions')
            return 
        
        def telecom_2():
            print('I really need to finish the telecomms event functions')
            return 
    
        ownable_event_index = {
            5 : rail1,
            12: telecom_1,
            15: rail2,
            25: rail3,
            28: telecom_2,
            35: rail4
        }
        return ownable_event_index
        
        
        
        
    
    