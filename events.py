class event:
    def __init__(self, name, ID):
        self.name = name
        self.ID = ID
        
    def events_dict_init():   
        def go():
            print('GO')
            money_change = 400
            return money_change
        def jail():
            pass
        def free_prk():
            pass
        def go_2_jail():
            pass
        def com_chest():
            pass
        def chance():
            pass
        def in_tax():
            pass
        def lib_tax():
            pass
        def rail1():
            pass
        def rail2():
            pass
        def rail3():
            pass
        def rail4():
            pass
        def telecom_1():
            pass
        def telecom_2():
            pass
            
        event_index = {
            0 : go,
            1 : com_chest,
            2 : chance,
            3 : in_tax,
            4 : lib_tax,
            5 : rail1,
            10: jail,
            12: telecom_1,
            15: rail2,
            20: free_prk,
            25: rail3,
            28: telecom_2,
            30: go_2_jail,
            35: rail4
        }
        
        return event_index
    
    def event_call(int, event_index):
        event_index[int]()
        
        
        
        
    
    