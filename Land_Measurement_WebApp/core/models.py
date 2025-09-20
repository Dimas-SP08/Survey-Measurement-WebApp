class Survey_Point:
    '''represents a single survey point with elevation calculation and status'''
    
    def __init__(self,
                 label : str,
                 backsight : float,
                 foresight : float,
                 distance : float,
                 initial_elev : float
                 ) -> None:
        '''Create a survey point'''

        self.label : str = label
        self.distance : float = distance
        self.backsight: float = backsight
        self.foresight : float = foresight

        heightdiffer = backsight - foresight
        initial_elev += heightdiffer
        stats = self.predict_status(heightdiffer)

        self.heightdiff : float =  heightdiffer
        self.elevation : float = initial_elev
        self.status : str = stats

    def predict_status(self,hegithdiffer : float) -> str:
        '''Decide if the point is RISE, FALL, or FLAT'''
        if hegithdiffer > 0:
            return "RISE"
        elif hegithdiffer < 0:
            return "FALL"
        else:
            return "FLAT"

    def to_dict(self,
                label : str,
                backsight : float,
                foresight : float,
                distance : float,
                heightdiffer : float,
                elevation : float,
                status : str
                ) -> dict:
        
        '''Convert point data to a dict for tables''' 
        return {
            "POINT NUMBER":label,
            "BACKSIGHT":backsight,
            "FORESIGHT":foresight,
            "DISTANCE (m)":distance,
            "HEIGHT DIFFERENCE":heightdiffer,
            "ELEVATION (AMSL)":elevation,
            "STATUS":status
        }
        
     