import random
from cards import card

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
            4 : in_tax,
            38 : lib_tax,
            10 : jail,
            20 : free_prk,
            30 : go_2_jail
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
        
        
        
        
    
    