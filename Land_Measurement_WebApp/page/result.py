from utils import *
import pandas as pd
from ai_integration import GeminiClient,prompts_make_report

class ResultsPage:
    def __init__(self):
        pass

    def render(self,navigate_to):
        markdown(get_main_html())

        markdown(get_header_html("Survey Analysis & Results","Review the measurement data, graphical analysis, and AI-generated report"))

        try:
            self.result = pd.DataFrame(get_state("results"))
            if self.result.empty:
                warning("No measurement data found to display.")
                return 
        except Exception as e:
            error(f"Failed to process measurement data: {e}")
            return 
        self.buffer_excel = export_to_excel(self.result)
        
        tab1, tab2, tab3 = tabs(["Data Table", "Graphical Analysis", "AI-Generated Report"])
        
        with tab1:
            subheader("Measurement Results Table")
            dataframe(self.result, use_container_width=True)
            info(f"Initial elevation (AMSL) used: **{get_state('initial_amsl')}** meters.")
            col = columns([1,2,1])
            with col[1]:
                download_button(
                    label="Download Table (xlsx)",
                    data=self.buffer_excel,
                    file_name='Land_Measurement_Results.xlsx'
                )
            
        
        with tab2:
            buffer = make_graphic_file_io(self.result)
            self.elevation_profile = buffer['elevation_profile']
            self.height_difference = buffer['height_difference']
            self.elevation_scatter = buffer['elevation_scatter']

            markdown("___")
            subheader("Elevation Profile")
            line_chart(data=self.result, x='POINT NUMBER', y='ELEVATION (AMSL)', height=400)
            col = columns([1,2,1])
            with col[1]:
                download_button(label="Download Elevation Profile Chart (PNG)", data=self.elevation_profile, file_name="Elevation_Profile.png")
            

            markdown("___")
            subheader("Height Difference Between Points")
            bar_chart(data=self.result, x='POINT NUMBER', y='HEIGHT DIFFERENCE', height=400)
            col = columns([1,2,1])
            with col[1]:
                download_button(label="Download Height Difference Chart (PNG)", data=self.height_difference, file_name="Height_Difference.png")
            

            markdown("___")
            subheader("Distance vs. Elevation Distribution")
            scatter_chart(data=self.result, x='DISTANCE (m)', y='ELEVATION (AMSL)', height=400)
            col = columns([1,2,1])
            with col[1]:
                download_button(label="Download Distance vs. Elevation Chart (PNG)", data=self.elevation_scatter, file_name="Distance_vs_Elevation.png")
            

        with tab3:
            subheader("AI-Generated Analysis Report")
            col = columns([1,2,1])
            with col[1]:
                if button("Generate AI Analysis Report", type="secondary",use_container_width=True):
                   with spinner("AI is analyzing data and preparing report..."):
                        try:
                            prompt = prompts_make_report(self.result.to_string(),get_state("purpose"))
                            ai = GeminiClient(secrets("model"))
                            response = ai.genrate_content(prompt, "gemini-1.5-flash", 0.3, 2000)
                            set_state("ai_report", response)

                        except Exception as e:
                            error(f"An error occurred during AI analysis: {str(e)}")


            if "ai_report" in session_state():
                markdown("___")
                markdown(get_state("ai_report"))
                
                col = columns([1,2,1])
                with col[1]:
                    word_buffer = export_to_word(get_state("ai_report"))
                    download_button(
                        label="Download Report (Word)",
                        data=word_buffer,
                        file_name="Survey_Report.docx"
                    )
                
            else:
                info(f"Click the button above to generate an automatic analysis report from your measurement data for {get_state("purpose")}.")

            

        