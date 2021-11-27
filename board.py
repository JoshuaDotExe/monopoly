from properties import property
from events import event, ownable_event
from cards import card

class board:
    def board_init():
        go = event('GO', 0)
        brown_1 = property('Brown 1', 60, (2,10,30,90,160,250), 0, 0)
        community_chest = card('Community Chest', 1)
        brown_2 = property('Brown 2', 60, (2,10,30,90,160,250), 0, 0)
        income_tax = event('Income Tax', 3)
        rail_1 = ownable_event('Rail 1', 5, 0, 0)                                                 #Ownable event
        light_b_1 = property('Light Blue 1', 100, (6,30,90,270,400,550), 0, 0)
        chance = card('Chance', 2)
        light_b_2 = property('Light Blue 2', 100, (6,30,90,270,400,550), 0, 0)
        light_b_3 = property('Light Blue 2', 120, (8,40,100,300,450,600), 0, 0)
        jail = event('Jail', 10)
        pink_1 = property("Pink 1", 140, (10,50,150,450,625,750), 0, 0)
        util_1 = ownable_event("Util 1", 12, 0, 0)                                        #Ownable event
        pink_2 = property("Pink 2", 140, (10,50,150,450,625,750), 0, 0)
        pink_3 = property("Pink 3", 160, (12,60,180,500,700,900), 0, 0)
        rail_2 = ownable_event('Rail 2', 15, 0, 0)                                                #Ownable event
        orange_1 = property('Orange 1', 180, (14,70,200,550,750,950), 0, 0)
        #Community Chest
        orange_2 = property('Orange 2', 180, (14,70,200,550,750,950), 0, 0)
        orange_3 = property('Orange 3', 200, (16,80,220,600,800,1000), 0, 0)
        free_parking = event('Free Parking', 20)
        red_1 = property('Red 1', 220, (22,110,330,800,975,1150), 0, 0)
        #Chance
        red_2 = property('Red 2', 220, (22,110,330,800,975,1150), 0, 0)
        red_3 = property('Red 3', 240, (20,100,300,750,925,1100), 0, 0)
        rail_3 = ownable_event('Rail 3', 25, 0, 0)
        yellow_1 = property('Yellow 1', 260, (22,110,330,800,975,1150), 0, 0)
        yellow_2 = property('Yellow 2', 260, (22,110,330,800,975,1150), 0, 0)
        util_2 = ownable_event('Utilities 2', 28, 0, 0)
        yellow_3 = property('Yellow 3', 280, (24,120,360,850,1025,1200), 0, 0)
        go_2_jail = event('Go To Jail', 30)
        green_1 = property('Green 1', 300, (26,130,390,900,1100,1275), 0, 0)
        green_2 = property('Green 2', 300, (26,130,390,900,1100,1275), 0, 0)
        #Community Chest
        green_3 = property('Green 3', 320, (28,150,450,1000,1200,1400), 0, 0)
        rail_4 = ownable_event('Rail 4', 35, 0, 0)
        #Chance
        dark_b_1 = property('Dark Blue 1', 350, (35,175,500,1100,1300,1500), 0, 0)
        liberty_tax = event('Libery Tax', 4)
        dark_b_2 = property('Dark Blue 2', 400, (50,200,600,1400,1700,2000), 0, 0)
        
        board = [go, brown_1, community_chest, brown_2, income_tax, rail_1, light_b_1, chance, light_b_2, light_b_3, jail, pink_1, util_1, pink_2, pink_3, rail_2, orange_1, community_chest, orange_2, orange_3, free_parking, red_1, chance, red_2, red_3, rail_3, yellow_1, yellow_2, util_2, yellow_3, go_2_jail, green_1, green_2, community_chest, green_3, rail_4, chance, dark_b_1, liberty_tax, dark_b_2]
        print("board loaded")
        return board
        