from core import Survey_CTRL,Survey_Point
from ai_integration import GeminiClient
import re,json
from utils import  *

class InputThreadsPage:
    def __init__(self):
        self.calculate = Survey_CTRL()

    def render(self,navigate_to):
        markdown(get_main_html())
        markdown(get_header_html("Enter Survey Measurements",f"Complete the data for all {get_state("point",0)} survey points below."))
        
        amsl = get_state("initial_amsl")
        temp_results = []
        temp_raw_data = []

        markdown("___")
        warning("⚠️ If the top and bottom threads are used, the mid thread will verify the average of top and bottom")
        # Loop through each point and create an expander for its inputs
        for i in range(get_state('point')):
            label, label1, label2 = self.calculate.add_point()
            
            # The first expander is open by default to guide the user
            is_expanded = i == 0
            
            with expander(f"Measurement for Point: {label}", expanded=is_expanded):
                # Get AI result for the current point if it exists
                ai_result = get_state("ai_result", [])
                backsight_ai, foresight_ai, distance_ai = {}, {}, {}
                if len(ai_result) > i:
                    point_ai_data = ai_result[i]
                    backsight_ai = point_ai_data.get(f"backsight{i+1}", {})
                    foresight_ai = point_ai_data.get(f"foresight{i+1}", {})
                    distance_ai = point_ai_data.get(f"distance{i+1}", {})


               
                col1, col2 = columns(2)
                with col1:
                    subheader(f"Enter {label1} (BACKSIGHT)")

                    top_thread = number_input("Enter top thread (0 if empty):", key=f"top{i}",format="%.5f" ) 
                    self.thread_info("top",backsight_ai,"desc_top")
                    

                    mid_thread = number_input("Enter mid thread:", key=f"mid{i}",format="%.5f")
                    self.thread_info("mid",backsight_ai,"desc_mid")

                    bottom_thread = number_input("Enter bottom thread (0 if empty):", key=f"bottom{i}",format="%.5f")
                    self.thread_info("bottom",backsight_ai,"desc_bottom")
            
                    Backsight = self.calculate.calculate_mid_thread(top_thread, mid_thread, bottom_thread)

                    # --- FORESIGHT ---
                with col2:
                    subheader(f"Enter {label2} (FORESIGHT)")

                    top_thread2 = number_input("Enter top thread (0 if empty):", key=f"top2{i}",format="%.5f")
                    self.thread_info("top",foresight_ai,"desc_top")
                    
                    mid_thread2 = number_input("Enter mid thread:", key=f"mid2{i}",format="%.5f")
                    self.thread_info("mid",foresight_ai,"desc_mid")
                    
                    bottom_thread2 = number_input("Enter bottom thread (0 if empty):", key=f"bottom2{i}",format="%.5f")
                    self.thread_info("bottom",foresight_ai,"desc_bottom")
                    
                    foresight = self.calculate.calculate_mid_thread(top_thread2, mid_thread2, bottom_thread2)

                # --- DISTANCE ---
                subheader(f"Distance for {label}")
                distance = number_input("Enter distance:", key=f"distance{i}",format="%.5f")
                self.thread_info("dist",distance_ai,"desc")

            # --- Data Aggregation ---
            raw_data_point = {
                "point_label": label,
                "backsight": {"top": top_thread, "mid": mid_thread, "bottom": bottom_thread},
                "foresight": {"top": top_thread2, "mid": mid_thread2, "bottom": bottom_thread2},
                "distance": distance
            }
            temp_raw_data.append(raw_data_point)

            result = Survey_Point(label, Backsight, foresight, distance, amsl)
            result_dict = result.to_dict(result.label, result.backsight, result.foresight, result.distance, result.heightdiff, result.elevation, result.status)
            amsl = result.elevation
            temp_results.append(result_dict)
            
            # Increment counters for next point
            self.calculate.ascii += 1
            self.calculate.point_group_index += 1

        # --- Final Actions Control Panel ---
        # --- Final Actions Control Panel ---
        markdown("___")
        col = columns([1, 2, 1])
        with col[1]:
            subheader("AI Analyze for Anomaly")
        with container():
            with col[1]:
                if button("Analyze", key="analyze", type="secondary",use_container_width=True):
                    prompt = f"""
                        You are a **professional surveying QA analyst**.
                        Analyze the following measurement data and flag potential anomalies.

                        ### INPUT DATA:
                        {temp_raw_data}

                        ### ANALYSIS RULES:
                        1. For each point (`backsight`, `foresight`, and `distance`):
                           - **If both top and bottom readings are provided (non-zero):**
                             - Calculate expected mid = (top + bottom) / 2.
                             - Compare provided mid with expected mid.
                             - Flag `"mid": "True"` if deviation is significant (beyond normal tolerance, e.g., >2–3 mm).
                             - Description should clearly state the difference, e.g.:
                               - "Mid reading 4mm higher than average of top and bottom"
                               - "Mid reading within acceptable tolerance (matches average)"
                           - **If top = 0 or bottom = 0:**
                             - Do not calculate expected mid, accept mid as-is.
                             - Mark top or bottom as `"False"` with description:
                               - `"desc_top": "No top reading provided – assumed safe"`
                               - `"desc_bottom": "No bottom reading provided – assumed safe"`
                           - **Top / Bottom checks:**
                             - If provided (≠ 0), verify they are within tolerance range.
                             - Mark `"True"` only if they deviate too much, otherwise `"False"` with description "Within acceptable tolerance".
                        2. **Distance check:**
                           - Mark `"dist": "True"` if outside expected range and explain deviation (e.g., "Distance exceeds tolerance by 0.8m").
                           - Otherwise mark `"dist": "False"` and describe "Distance within acceptable range".

                        ### OUTPUT FORMAT:
                        Return **ONLY** a valid JSON array.
                        Do not include backticks, code fences, or extra commentary.
                        Use this exact structure:

                        [
                          {{
                            "backsight1": {{
                              "mid": "True",
                              "desc_mid": "Mid reading 5mm higher than average of top and bottom",
                              "top": "False",
                              "desc_top": "Within acceptable tolerance",
                              "bottom": "False",
                              "desc_bottom": "Within acceptable tolerance"
                            }},
                            "foresight1": {{
                              "mid": "False",
                              "desc_mid": "Mid reading matches average (within tolerance)",
                              "top": "False",
                              "desc_top": "No top reading provided – assumed safe",
                              "bottom": "False",
                              "desc_bottom": "No bottom reading provided – assumed safe"
                            }},
                            "distance1": {{
                              "dist": "False",
                              "desc": "Distance within acceptable range"
                            }}
                          }},
                          ...
                        ]

                        ### STYLE REQUIREMENTS:
                        - Always use short, professional, clear explanations.
                        - Be precise: if possible, mention how far mid deviates from expected average.
                        - Use the exact phrases:
                          - `"No ... reading provided – assumed safe"` for missing top/bottom.
                          - `"Within acceptable tolerance"` for values that are OK.
                          - `"deviates by X mm"` for out-of-range readings.
                        """
                    with spinner('AI Assistant is analyzing your data...'):
                        try:
                            ai = GeminiClient(secrets("model"))
                            response = ai.genrate_content(prompt, "gemini-1.5-flash", 0.0)
                            clean_response = re.sub(r"```(?:json)?\s*", "", response)
                            clean_response = re.sub(r"```", "", clean_response)
                            clean_response = re.sub(r",\s*]", "]", clean_response)
                            clean_response = clean_response.strip()
                            try:
                                parsed = json.loads(clean_response)
                                set_state("ai_result", parsed)
                                rerun()
                            except json.JSONDecodeError:
                                warning("⚠️ AI response could not be parsed. Raw output shown below:")
                                code(response, language="json")

                        except Exception as e:
                            error(f"An error occurred during AI analysis: {str(e)}")
        
        markdown("___")


        col = columns([1,2,1,2,1])
        # ...existing code...

        with col[1]:
            if button("Back", key="back_point", type="primary", use_container_width=True):
                set_state("show_confirm_dialog_back",True)
            if get_state("show_confirm_dialog_back", False):
                confirm_and_process("Are you sure you want to go back?", result_name="confirm_result_back")
            if get_state("confirm_result_back") is True:
                set_state("show_confirm_dialog_back",False)
                set_state("confirm_result_back",None ) # reset
                navigate_to("input_points")
            elif get_state("confirm_result_back") is False:
                set_state("show_confirm_dialog_back",False)
                set_state("confirm_result_back",None ) # reset
        
        
        with col[3]:
            if button("Submit", key="submit", type="secondary", use_container_width=True):
                set_state("show_confirm_dialog_submit",True)
            if get_state("show_confirm_dialog_submit", False):
                confirm_and_process("Are you sure you want to submit the data? You won't be able to edit later.", result_name="confirm_result_submit")
            if get_state("confirm_result_submit") is True:
                set_state("show_confirm_dialog_submit" , False)
                set_state("confirm_result_submit" , None ) # reset
                set_state("results", temp_results)
                navigate_to("results")
            elif get_state("confirm_result_submit") is False:
                set_state("show_confirm_dialog_submit" ,False)
                set_state("confirm_result_submit" , None)  # reset

    def thread_info(self,thread_type,ai_thread,desc_thread):
        if ai_thread:
            if ai_thread.get(thread_type, "False") == "True":
                warning(f"⚠️ {ai_thread.get(desc_thread, '')}")
            else:
                success(f"✅ {ai_thread.get(desc_thread, '')}")