import google.generativeai as genai

class GeminiClient:
    
    def __init__(self,api_code):
        api_key = api_code
        genai.configure(api_key=api_key)

    def genrate_content(self,prompt,model_ai,temperature,maximal=None):
            model = genai.GenerativeModel(model_name=f"{model_ai}")
            response = model.generate_content(
                contents=prompt,
                generation_config={
                    "temperature":temperature,
                    "max_output_tokens":maximal
                })
            return response.text
        

    