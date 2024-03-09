import google.generativeai as genai

class GeminiModel:
    def __init__(self, api_key, model_name):
        # Configure the API with the provided key
        genai.configure(api_key=api_key)
        
        # Default configuration settings; can be customized further if needed
        generation_config = {
            "temperature": 0,
            "top_p": 1,
            "top_k": 1,
            "max_output_tokens": 30720,
        }
        
        safety_settings = [
            {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_ONLY_HIGH"},
            {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_ONLY_HIGH"},
            {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_ONLY_HIGH"},
            {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_ONLY_HIGH"},
        ]
        
        # Set up the model with the provided model name
        self.model = genai.GenerativeModel(model_name=model_name,
                                           generation_config=generation_config,
                                           safety_settings=safety_settings)

    def generate_content(self, prompts):
        # Generate content based on the provided prompts
        response = self.model.generate_content([prompts])
        return response.text


# # Example usage:
# if __name__ == "__main__":
#     api_key = "YOUR_API_KEY"
#     model_name = "gemini-1.0-pro"
    
#     gen_ai_model = GeminiModel(api_key, model_name)
#     prompts = ["hey Hi"]
#     response_text = gen_ai_model.generate_content(prompts)
#     print(response_text)