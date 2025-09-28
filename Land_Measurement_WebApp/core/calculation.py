class Survey_CTRL:
    '''Controler to manage survey workflow'''

    def __init__(self) -> None:
        
        '''Initialize the controler'''
        self.point_group_index : int =1

    def add_point(self) -> tuple[str, str, str] :
        '''Generate labels for points'''
        label1 = f'P{self.point_group_index}'
        label2 = f'P{self.point_group_index + 1}'
        label  = f'{label1} - {label2}'
        return label,label1,label2

    def calculate_mid_thread_and_dist(self,
                             top_thread : float,
                             mid_thread : float,
                             bottom_thread : float) -> float :
        '''Calculate mid thread from top and bottom thread'''
        if top_thread != 0 and bottom_thread != 0:
            distance = (top_thread - bottom_thread) * 100                      
            result_mid_thread = (top_thread + bottom_thread) / 2
            if result_mid_thread == mid_thread:
                validate = "valid"
            else:
                validate = "invalid"
            return result_mid_thread,validate,distance
        else:
            validate = False
            distance= 0.0
            return mid_thread,validate,distance

        

    
    