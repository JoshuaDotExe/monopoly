import random, sys, os

from properties import property
from players import player

class event:
    def __init__(self, name, ID):
        self.name = name
        self.ID = ID
    
    def __repr__(self):
        return "Event : {}, ID : {}".format(self.name, self.ID)
    
    def index():
        def go(p):
            print('Collect $400!')
            p = player.balAdd(p, 400)
            return p
        
        def jail(p):
            print("You're just visiting!")
            return p
                          
        def free_prk(p):
            print('Woo! Free Parking!')
            return p
        
        def go_2_jail(p):
            print('Go straight to jail! Do not pass go and do not collect $200!')
            p.space = 10
            p.jailStats = 1
            return p
        
        def in_tax(p):
            print('Pay $200 in income taxes!')
            p = player.balSub(p, 200)
            return p
        
        def lib_tax(p):
            print('Pay $100 in taxes!')
            p = player.balSub(p, 100)
            return p
        
        event_index = {
            0 : go,
            4 : in_tax,
            38 : lib_tax,
            10 : jail,
            20 : free_prk,
            30 : go_2_jail
        }
        return event_index
    
    def jailer(p):
        print('Go straight to jail! Do not pass go and do not collect $200!')
        p.space = 10
        p.jailStats = 1
        return p

class util_event:
    def __init__(self, name, ID, value, owner, num_of_houses):
        self.name = name
        self.ID = ID
        self.value = value
        self.owner = owner
        self.num_of_houses = num_of_houses
    
    def __repr__(self):
        return "Utility : {}, Price ${}, Houses = {}, Owner = Player {}".format(self.name, self.value, self.num_of_houses, self.owner)

    def getRent(utility, roll_total):
        if utility.num_of_houses == 1:
            multiplier = 4
        elif utility.num_of_houses == 2:
            multiplier = 10
        else:
            multiplier = 0
            print('Unknown num of properties owned')
        rent = roll_total * multiplier
        return rent

class rail_event:
    def __init__(self, name, ID, value, owner, rent, num_of_houses):
        self.name = name
        self.ID = ID
        self.value = value
        self.owner = owner
        self.rent = rent
        self.num_of_houses = num_of_houses
    
    def __repr__(self):
        return "Railway : {}, Price ${}, Rent {}, Houses = {}, Owner = Player {}".format(self.name, self.value, self.rent, self.num_of_houses, self.owner)
    
    def getRent(railway):
        rent = railway.rent[railway.num_of_houses]
        return rent

class card:
    def __init__ (self, name, ID, iter):          #Community Chest ID = 1, Chance ID = 2
        self.name = name
        self.ID = ID
        self.iter = iter

    def __repr__(self):
        return "Card : {}".format(self.name)
    
    def com_chest_init():                   #p_bal, p_space, p_in_jail, board, player_list
        def adv_2_go(p, board, player_list):
            print('Advance to GO!')
            p.space = 0
            return p, board, player_list

        def bnk_err(p, board, player_list):
            print('There was a bank error in your favour! Collect $200!')
            p = player.balAdd(p, 200)
            return p, board, player_list
        
        def doc_fee(p, board, player_list):
            print('Pay doctor\'s fees of $50')
            p = player.balSub(p, 50)
            return p, board, player_list
        
        def go_jail(p, board, player_list):
            print('You\'ve been arrested on suspicion of tax avoidance!\nGo straight to jail! Do not pass go and do not collect $200!')
            p.space = 10
            p.jailStats = 1
            return p, board, player_list
        
        def beau_cont(p, board, player_list):
            print('You\'ve won a beauty contest! Collect $10!')
            p = player.balAdd(p, 10)
            return p, board, player_list
        def sale_of_stock(p, board, player_list):
            print('You\'ve made a profit from selling stocks! Collect $50!')
            p = player.balAdd(p, 50)
            return p, board, player_list
        def grnd_op(p, board, player_list):
            print('You host a grand opera night! Collect $50 from every player!')       #Implement collecting func here
            num_players = len(player_list)
            p = player.balAdd(p, (50*num_players))
            for x in player_list:
                if p != x:
                    x.balance -= 50
                else:
                    pass
                pass
            return p, board, player_list
        def holiday_fund(p, board, player_list):
            print('Your holiday fund matures, collect $100!')
            p = player.balAdd(p, 100)
            return p, board, player_list
        def tax_ref(p, board, player_list):
            print('You get a tax refund! Collect $20!')
            p = player.balAdd(p, 20)
            return p, board, player_list
        def brth_d(p, board, player_list):
            print('It\'s your birthday! Collect $10 from every player!')                 #Implement collecting func here 
            p = player.balAdd(p, (10*(len(player_list)-1)))
            gift_list = player_list
            del gift_list[p.num]
            for x in gift_list:
                x = player.balSub(x, 10)
            return p, board, player_list
        def life_ins(p, board, player_list):
            print('Life insurance premiums increase, pay $100')
            p = player.balAdd(p, 100)
            return p, board, player_list
        def hosp_fee(p, board, player_list):
            print('Hospital fees come due! Pay $50')
            p = player.balSub(p, 50)
            return p, board, player_list
        def school_fee(p, board, player_list):
            print('A new school term starts, pay $50 in school fees')
            p = player.balSub(p, 50)
            return p, board, player_list
        def consult_fee(p, board, player_list):
            print('A new school term starts, pay $50 in school fees')
            p = player.balSub(p, 50)
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
            p = player.balSub(p, total)
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
            p = player.balAdd(p, 50)
            return p, board, player_list
        def croswrd_comp(p, board, player_list):
            print('You win a crossword competition! Collect $100!')
            p = player.balAdd(p, 100)
            return p, board, player_list
        def go_back_3(p, board, player_list):
            print('Go back 3 spaces!')
            p.space -= 3
            return p, board, player_list
        def head_jail(p, board, player_list):
            print('You\'ve been arrested on suspicion of tax avoidance!')
            p = event.jailer(p)
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
            p = player.balSub(p, total)
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
        #print(rand_list)
        out_dictionary = {}
        for key in dictionary:
            out_dictionary[key] = dictionary[rand_list[key-1]]
        return out_dictionary


def board_init():
        go = event('GO', 0)
        brown_1 = property('Brown 1', 60, (2,10,30,90,160,250), 0, 0)
        community_chest = card('Community Chest', 1, 1)
        brown_2 = property('Brown 2', 60, (2,10,30,90,160,250), 0, 0)
        income_tax = event('Income Tax', 3)
        rail_1 = rail_event('Rail 1', 5, 200, 0, (50, 100, 150, 200), 0)                                                 #Ownable event
        light_b_1 = property('Light Blue 1', 100, (6,30,90,270,400,550), 0, 0)
        chance = card('Chance', 2, 1)
        light_b_2 = property('Light Blue 2', 100, (6,30,90,270,400,550), 0, 0)
        light_b_3 = property('Light Blue 3', 120, (8,40,100,300,450,600), 0, 0)
        jail = event('Jail', 10)
        pink_1 = property("Pink 1", 140, (10,50,150,450,625,750), 0, 0)
        util_1 = util_event("Util 1", 12, 150, 0, 0)                                        #Ownable event
        pink_2 = property("Pink 2", 140, (10,50,150,450,625,750), 0, 0)
        pink_3 = property("Pink 3", 160, (12,60,180,500,700,900), 0, 0)
        rail_2 = rail_event('Rail 2', 15, 200, 0, (50, 100, 150, 200), 0)                                                #Ownable event
        orange_1 = property('Orange 1', 180, (14,70,200,550,750,950), 0, 0)
        #Community Chest
        orange_2 = property('Orange 2', 180, (14,70,200,550,750,950), 0, 0)
        orange_3 = property('Orange 3', 200, (16,80,220,600,800,1000), 0, 0)
        free_parking = event('Free Parking', 20)
        red_1 = property('Red 1', 220, (22,110,330,800,975,1150), 0, 0)
        #Chance
        red_2 = property('Red 2', 220, (22,110,330,800,975,1150), 0, 0)
        red_3 = property('Red 3', 240, (20,100,300,750,925,1100), 0, 0)
        rail_3 = rail_event('Rail 3', 25, 200, 0, (50, 100, 150, 200), 0)
        yellow_1 = property('Yellow 1', 260, (22,110,330,800,975,1150), 0, 0)
        yellow_2 = property('Yellow 2', 260, (22,110,330,800,975,1150), 0, 0)
        util_2 = util_event('Utilities 2', 28, 150, 0, 0)
        yellow_3 = property('Yellow 3', 280, (24,120,360,850,1025,1200), 0, 0)
        go_2_jail = event('Go To Jail', 30)
        green_1 = property('Green 1', 300, (26,130,390,900,1100,1275), 0, 0)
        green_2 = property('Green 2', 300, (26,130,390,900,1100,1275), 0, 0)
        #Community Chest
        green_3 = property('Green 3', 320, (28,150,450,1000,1200,1400), 0, 0)
        rail_4 = rail_event('Rail 4', 35, 200, 0, (50, 100, 150, 200), 0)
        #Chance
        dark_b_1 = property('Dark Blue 1', 350, (35,175,500,1100,1300,1500), 0, 0)
        liberty_tax = event('Libery Tax', 4)
        dark_b_2 = property('Dark Blue 2', 400, (50,200,600,1400,1700,2000), 0, 0)
        
        game_board = [go, brown_1, community_chest, brown_2, income_tax, rail_1, light_b_1, chance, light_b_2, light_b_3, jail, pink_1, util_1, pink_2, pink_3, rail_2, orange_1, community_chest, orange_2, orange_3, free_parking, red_1, chance, red_2, red_3, rail_3, yellow_1, yellow_2, util_2, yellow_3, go_2_jail, green_1, green_2, community_chest, green_3, rail_4, chance, dark_b_1, liberty_tax, dark_b_2]
        return game_board

def getProperties(game_board, playerNum):
    total_value = 0
    properties_dict = {}
    i = 0
    for x in game_board:
        if type(x) == property or rail_event or util_event:
            if x.owner == playerNum:
                i += 1
                properties_dict.update(i = x)
    for x in properties_dict:
        total_value += x.value
        if type(x) == property:
            prop_index = game_board.index(x)
            total_value += property.houseCost(prop_index, x.num_of_houses)
    return total_value, properties_dict
    

def main(game_board, p_list, playerNum, community_chest_index, chance_index):
    currentPlayer = p_list[playerNum]
    if currentPlayer.jailStats > 0:
        def jail_pay(p):
            p = player.balSub(p, 50)
            p.jailStats = 0
            print('Much obliged, you\'re free to go!')

        def jail_roll(p):
            print('Good luck getting those doubles!')    
            die1, die2 = random.randint(1,6), random.randint(1,6)
            if die1 == die2:
                print(f'Double {die1}!\nYou\'re free to go!')
                p.jailStats = 0
                p.space += (die1 + die2)
            else:
                print(f'Rolled a {die1} and a {die2}\nYou have {3-p.jailStats} more turns left in your sentence!') #Should add 3 turn rule by turning jailStats into an int
                p.jailStats += 1
                if p.jailStats == 4:
                    p.jailStats = 0
                    print('You\'ve served your sentence, you\'re free to go!')
        
        prison_options = {
                '1' : jail_pay,
                '2' : jail_roll
            }
        
        user_in = input('You\'re in jail! Pick an option\n1 : PAY\n2 : ROLL\n')
        while True:
            if user_in.upper() in prison_options:
                prison_options[user_in](currentPlayer)
                break
            else:
                user_in = input('Please enter a known command\n1 : PAY\n2 : ROLL\n')
    else:
        num_of_rolls = 0
        roll_total = 0
        while num_of_rolls < 3:
            die1, die2 = random.randint(1,6), random.randint(1,6)
            roll_total += die1 + die2
            if die1 == die2:
                print(f'Double {die1}!')
                num_of_rolls += 1
            else:
                print(f'Rolled a {die1} and a {die2}')
                num_of_rolls += 5
        else:
            if num_of_rolls == 3:
                print('You\'ve been caught speeding!')
                player.jailer(currentPlayer)
            else:
                print(f'Roll Total = {roll_total}')
    if currentPlayer.jailStats == 0:
        player.spaceMove(currentPlayer, roll_total)
        currentSpace = game_board[currentPlayer.space]
        print(f'You\'ve landed on {currentSpace.name}')
        if currentSpace == card:
            print('Card')
        if currentSpace == event:
            print('Event')
        elif currentSpace == property or rail_event or util_event:
            if currentSpace.owner == playerNum:
                print('You own this! Safe and sound, for now!')
                pass
            elif currentSpace.owner == 0:
                #Unowned
                pass
            else:
                #Owned
                rent = 0
                rent = property.getRent if type(currentSpace) == property else rent
                rent = rail_event.getRent if type(currentSpace) == rail_event else rent
                rent = util_event.getRent if type(currentSpace) == util_event else rent
                print(f'Uh oh! Looks like it\'s owned by player {currentSpace.owner}\nYou owe them rent to the tune of ${rent}')
                if currentPlayer.balance >= rent:
                    player.balAdd(p_list[currentSpace.owner], rent)
                    player.balSub(currentPlayer, rent)
                else:
                    total_value, properties_dict = getProperties(game_board, playerNum)
                    if total_value + currentPlayer.balance >= rent:
                    
                        
                            
                            
        else:
            print('Unknown Space Action')
    return game_board, p_list


if __name__ == '__main__':
    # When file is run it creates the necessary game variables and allows for the turns to be run one after the other for debugging
    game_board = board_init()
    p_list = player.debug_player_list()
    community_chest_index, chance_index = card.com_chest_init(), card.chance_init()
    def turn(game_board, p_list, x, community_chest_index, chance_index):
        game_board, p_list = main(game_board, p_list, x, community_chest_index, chance_index)
        return game_board, p_list
    def save(game_board, p_list, x, community_chest_index, chance_index):
        with open('output.txt', 'w') as file:
            file.write(f'Player {x}\'s turn.\n')
            for player in p_list:
                file.write(repr(p_list[player]) + '\n')
            for space in game_board:
                file.write(repr(space) + '\n')
            cardList = []
            for key in community_chest_index:
                cardList.append(key)
            file.write(f'Community Chest Index = {cardList}')
            cardList = []
            for key in chance_index:
                cardList.append(key)
            file.write(f'Community Chest Index = {cardList}')
        exit()
    
    command_index = {
        '1' : turn,
        '2' : save
    }
    
    while True:
        for playerNum in range(1, 7):
            user_in = input(f'It\'s player {playerNum}\'s turn.\n1 : TURN\n2 : SAVE\n')
            while True:
                if user_in in command_index:
                    command_index[user_in](game_board, p_list, playerNum, community_chest_index, chance_index)
                    break
                else:
                    user_in = input('Please enter a known command\n1 : TURN\n2 : SAVE\n')
            
                    
else:
    print(f'__name__ != __main__ @{os.getcwd()}')

