def prompt_for_detect_anomalies(data):
    prompt =f"""
            You are a **professional surveying QA analyst**.
            Analyze the following measurement data and flag potential anomalies.

            ### INPUT DATA:
            {data}

            ### ANALYSIS CRITERIA:
            1. Check thread consistency (top > mid > bottom where applicable)
            2. Verify mid thread is approximately average of top and bottom (when both exist)
            3. Validate distance measurements for logical progression
            4. Identify measurement outliers or recording errors
            5. Check for missing or zero values where they shouldn't be

            ### OUTPUT FORMAT:
            Return **ONLY** a valid JSON array.
            Do not include backticks, code fences, or extra commentary.
            Use this exact structure:

            [
                {{
                "backsight1": {{
                    "mid": "True/False",
                    "desc_mid": "Brief description of mid thread anomaly",
                    "top": "True/False", 
                    "desc_top": "Brief description of top thread anomaly",
                    "bottom": "True/False",
                    "desc_bottom": "Brief description of bottom thread anomaly"
                }},
                "foresight1": {{
                    "mid": "True/False",
                    "desc_mid": "Brief description of mid thread anomaly",
                    "top": "True/False",
                    "desc_top": "Brief description of top thread anomaly", 
                    "bottom": "True/False",
                    "desc_bottom": "Brief description of bottom thread anomaly"
                }},
                "distance1": {{
                    "dist": "True/False",
                    "desc": "Brief description of distance anomaly"
                }}
                }},
                ...
            ]

            ### IMPORTANT NOTES:
            - Use "True" if anomaly detected, "False" if normal
            - You must add the number at ,foresight1,foresight2....... and other, include backsight and distance
            - Keep descriptions concise but informative
            - If top/bottom are 0, assume they're not measured and mark as "False"
            - Focus on technical surveying accuracy
            - Generate one object per measurement point in the input data
            """
    return prompt

def prompts_make_report(data,purpose):
    prompt = f"""
            You are a professional survey and mapping analyst.
            Based on the following technical data, create a comprehensive elevation analysis report in English.

            ### MEASUREMENT DATA:
            {data}

            ### SURVEY PURPOSE:
            {purpose}

            ### REQUESTED REPORT STRUCTURE:
            Create a report with a clear and professional structure, covering the following points:

            1.  **📈 Summary and Overview of Measurement Results:**
                - Briefly explain the land elevation profile.
                - Mention the highest and lowest elevation points.
                - Calculate and mention the total elevation difference from start to end point.

            2.  **💡 Land Suitability Analysis:**
                - Based on the survey purpose ({purpose}), provide an analysis of the land conditions.
                - Does the land contour support this purpose? What are the challenges? (e.g., if for roads, is the gradient too steep?)

            3.  **⚠️ Important Technical Considerations:**
                - Identify areas with the most significant elevation changes.
                - Provide technical considerations that need attention, such as potential cut and fill, drainage requirements, or slope stability.

            4.  **📅 Recommendations for Next Steps:**
                - Suggest logical next steps. Examples: more detailed topographic survey, geotechnical investigation, or preliminary design planning.

            ### WRITING FORMAT:
                - Use formal and professional language.
                - Clearly separate sections with headings (use ALL CAPS headings).
                - Use bullet points or numbered lists where appropriate.
                - Avoid using Markdown or special symbols (❌ no emojis, ❌ no **bold**).
                - Keep the structure clean so it can be directly exported into a Word document.

            """
    return prompt
