import random, sys, time     #Random for random num generator, sys for size_check()

def board_init():            #Done for neatness as long lists can be scary to look at
    return [['Go', -1, -1,[]],
            ['br1', 60, 0,[2,10,30,90,160,250]],
            ['cc_1', -1, -1,[]],
            ['br2', 60, 0,[4,20,60,180,320,450]],
            ['in_tax', -1, -1,[]],
            ['rail_1', 200, 0,[25,50,100,200]],
            ['lb1', 100, 0,[6,30,90,270,400,550]],
            ['chance_1', -1, -1,[]],
            ['lb2', 100, 0,[6,30,90,270,400,550]],
            ['lb3', 120, 0,[8,40,100,300,450,600]],
            ['jail', -1, -1,[]],
            ['pnk_1', 140, 0,[10,50,150,450,625,750]],
            ['tele_1', 150, 0,[]],
            ['pnk_2', 140, 0,[10,50,150,450,625,750]],
            ['pnk_3', 160, 0,[12,60,180,500,700,900]],
            ['rail_2', 200, 0,[25,50,100,200]],
            ['or_1', 180, 0,[14,70,200,550,750,950]],
            ['cc_2', -1, -1,[]],
            ['or_2', 180, 0,[14,70,200,550,750,950]],
            ['or_3', 200, 0,[16,80,220,600,800,1000]],
            ['free_prkn', -1, -1,[]],
            ['red_1', 220, 0,[18,90,250,700,875,1050]],
            ['chance_2', -1, -1,[]],
            ['red_2', 220, 0,[18,90,250,700,875,1050]],
            ['red_3', 240, 0,[20,100,300,750,925,1100]],
            ['rail_3', 200, 0,[25,50,100,200]],
            ['ylw_1', 260, 0,[22,110,330,800,975,1150]],
            ['ylw_2', 260, 0,[22,110,330,800,975,1150]],
            ['tele_2', 150, 0,[]],
            ['ylw_3', 280, 0,[24,120,360,850,1025,1200]],
            ['go2jail', -1, -1,[]],
            ['grn_1', 300, 0,[26,130,390,900,1100,1275]],
            ['grn_2', 300, 0,[26,130,390,900,1100,1275]],
            ['cc_3', -1, -1,[]],
            ['grn_3', 320, 0,[28,150,450,1000,1200,1400]],
            ['rail_4', 200, 0,[25,50,100,200]],
            ['chance_3', -1, -1,[]],
            ['db_1', 350, 0,[35,175,500,1100,1300,1500]],
            ['lib_tax', -100, -1,[]],
            ['db_2', 400, 0,[50,200,600,1400,1700,2000]]]
    
    #Board layout = ['Place name', +price/-identifier, player owner, [rent prices 0-5 houses]] should probably change to a tuple, remember to do performance benchmarks
    #Prices all retrieved from monopoly.fandom.com

def size_check(board):       #For pedantic object byte size checking, shouldn't really be used in actual software
    totalSize = 0
    objectSize = 0
    objectObjectSize = 0
    for x in range(0, 39):
        objectSize = sys.getsizeof(board[x])
        objectObjectSize = sys.getsizeof(board[x][3])
        totalSize = totalSize + objectSize + objectObjectSize
    
    print(f'Total Size = {totalSize + sys.getsizeof(board)}')

def roll_init():             #return jailCheck(int), roll(int)
    rollPhase = 0
    roll = 0
    jailCheck = 0
    while rollPhase < 3:
        die1 = random.randint(1,6)
        die2 = random.randint(1,6)
        roll = roll+(die1+die2)

        print(f"Roll = {die1} + {die2} = {die1+die2}")    
        if(die1 != die2):                 #Condition if doubles not rolled on dice
            rollPhase += 3
        else:                             #Condition if doubles rolled on dice
            rollPhase += 1
            print(f'Double {die1}!!')
            jailCheck += 1
    return jailCheck, roll

def player_new():
    p_add_intentions = True
    while p_add_intentions is True: 
        player_add = str(input("Would you like to add another player? (Y/N):"))
        if player_add.upper() == "Y":
            return p_add_intentions
            
        if player_add.upper() == "N":
            p_add_intentions = False
            return p_add_intentions
        else:
            print("Please enter a Y or N")
    
def player_init():          #return player_list(list), player_num(int)
    player_creation = True
    player_list = []
    player_num=1
    max_players = 6
    
    while player_creation == True and player_num<=max_players:
        
        name = input(f"Player {player_num}! Please enter your nickname:")
        player_list.append([name,1500,0])  #playerID = index + 1 [name,Money(int),space(starts on go)]
        player_num+=1
        if player_num <= max_players:  #Checks to see if it's under the max amount of players to ask for permission to add a new player
            player_creation = player_new()
        else:
            print(f'The maximum number of players has been reached! {max_players} Let\'s start!')
            
    return player_list, player_num

def turn(player_space):
    jailCheck, roll = roll_init()
    if(jailCheck >= 3):
        print('Go directly to jail! Do not pass go >:c')
        player_space = 10   #In jail!
    else:
        player_space += roll
    return player_space
        
        
board = board_init()         #Board data
size_check(board)
player_info_list, num_of_players = player_init()

for x in range(num_of_players-1):
    print(f'Player {x+1}\'s turn!')
    player_info_list[x][2] = turn(player_info_list[x][2])
    print(f'Player {x+1} has landed on space {board[player_info_list[x][2]]}\n')
 
