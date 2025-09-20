class Survey_CTRL:
    '''Controler to manage survey workflow'''

    def __init__(self) -> None:
        
        '''Initialize the controler'''
        self.ascii : int =97 # 'a' in ASCII
        self.point_group_index : int =1

    def add_point(self) -> tuple[str, str, str] :
        '''Generate labels for points'''
        label1 = f'P{self.point_group_index}-{chr(self.ascii)}'
        label2 = f'P{self.point_group_index}-{chr(self.ascii + 1)}'
        label  = f'{label1} - {label2}'
        return label,label1,label2

    def calculate_mid_thread(self,
                             top_thread : float,
                             mid_thread : float,
                             bottom_thread : float) -> float :
        '''Calculate mid thread from top and bottom thread'''
        if top_thread != 0 and bottom_thread != 0:                       
            result_mid_thread = (top_thread + bottom_thread) / 2
            return result_mid_thread
        else:
            return mid_thread

        

    
    