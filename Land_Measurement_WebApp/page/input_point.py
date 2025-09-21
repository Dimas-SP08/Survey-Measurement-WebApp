"""import necessary libraries"""
from utils import *

class InputPointsPage:
    def __init__(self):
        pass

    def render(self, navigate_to):
        markdown(get_main_html())
        markdown(get_header_html("Configure Your Survey","Enter the initial parameters for the survey measurement."))
    
        
        subheader("Initial Data Input")

        point = number_input(
            "Number of Survey Points",
            min_value=1,
            max_value=50,
            step=1,
            value=3,
            help="Enter the total number of points you plan to measure."
        )

        init_amsl = number_input(
            "Initial Elevation (AMSL in meters)",
            min_value=-100.000,
            max_value=9000.000,
            step=0.001,
            value=1000.000,
            help="Enter the starting elevation (Above Mean Sea Level) for your first point."
        )

        purpose = text_input(
            "Survey Purpose (Optional)",
            value="Road Construction",
            help="Briefly describe the purpose of this survey, e.g., 'Land Boundary Measurement'."
        )
        
        

        # Action Buttons
        col = columns([1,2,1,2,1])
        
        with col[1]:
            if button("Back", key="back_home", type="primary",use_container_width=True):
                navigate_to("home")
        
        with col[3]:
            if button("Next", key="start_threads",type="secondary",use_container_width=True):
                # Save state and navigate
                set_state("point",point)
                set_state("initial_amsl",init_amsl)
                set_state("purpose",purpose)

                navigate_to("input_threads")

        

    