class Survey_Point:
    '''represents a single survey point with elevation calculation and status'''
    
    def __init__(self,
                 label : str,
                 backsight : float,
                 foresight : float,
                 distance : float,
                 cumulative_dist : float,
                 initial_elev : float
                 ) -> None:
        
        '''Create a survey point'''
        self.label : str = label
        self.distance : float = distance
        self.cumulative_dist = cumulative_dist
        self.backsight: float = backsight
        self.foresight : float = foresight

        self.cumulative_dist += distance
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

    def to_dict(self) -> dict:
        '''Convert point data to a dict for tables''' 
        return {
            "POINT NUMBER":self.label,
            "BACKSIGHT":self.backsight,
            "FORESIGHT":self.foresight,
            "DISTANCE (m)":self.distance,
            "CUMULATIVE DISTANCE (m)":self.cumulative_dist,
            "HEIGHT DIFFERENCE":self.heightdiff,
            "ELEVATION (AMSL)":self.elevation,
            "STATUS":self.status
        }
        
     