import google.generativeai as genai
from typing import Union, List, Dict, Optional

class GeminiModel:
    def __init__(
        self,
        api_key: str,
        model_name: str = "gemini-1.0-pro",
        generation_config: Optional[Dict] = None,
        safety_settings: Optional[List] = None,
    ):
        """
        Initializes the Gemini model with optional generation and safety configurations.

        Args:
            api_key (str): Google Generative AI API key.
            model_name (str): Name of the Gemini model (e.g., "gemini-1.0-pro").
            generation_config (dict, optional): Custom generation configuration parameters.
            safety_settings (list, optional): Custom safety configuration list.
        """
        # Configure API
        genai.configure(api_key=api_key)

        # Default generation config (fallback)
        default_generation_config = {
            "temperature": 0,
            "top_p": 1,
            "top_k": 1,
            "max_output_tokens": 30720,
        }

        # Default safety settings (fallback)
        default_safety_settings = [
            {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_ONLY_HIGH"},
            {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_ONLY_HIGH"},
            {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_ONLY_HIGH"},
            {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_ONLY_HIGH"},
        ]

        # Use user-provided or default settings
        self.model = genai.GenerativeModel(
            model_name=model_name,
            generation_config=generation_config or default_generation_config,
            safety_settings=safety_settings or default_safety_settings,
        )

    def generate_content(self, prompts: Union[str, List[str]]) -> str:
        """
        Generate text or content based on the provided prompts.

        Args:
            prompts (str | list[str]): The input text prompt(s).

        Returns:
            str: The generated response text.
        """
        # Ensure prompts are in a list format for the API
        if isinstance(prompts, str):
            prompts = [prompts]
            
        try:
            response = self.model.generate_content(prompts)
            return response.text
        except Exception as e:
            print(f"An error occurred during content generation: {e}")
            # Depending on desired error handling, you might want to return None,
            # an empty string, or re-raise the exception.
            return ""


# Example usage:
if __name__ == "__main__":
    # --- IMPORTANT ---
    # Replace "YOUR_API_KEY" with your actual Google Generative AI API key
    # It's best practice to load this from an environment variable or a
    # secure config file instead of hardcoding it.
    API_KEY = "YOUR_API_KEY" 

    if API_KEY == "YOUR_API_KEY":
        print("Please replace 'YOUR_API_KEY' with your actual API key to run the example.")
    else:
        # --- Example 1: Using default settings ---
        print("--- Running with default settings ---")
        try:
            default_gemini = GeminiModel(api_key=API_KEY, model_name="gemini-1.5-flash")
            response_default = default_gemini.generate_content("Hello! Write a one-sentence greeting.")
            print(f"Default Response: {response_default}\n")
        except Exception as e:
            print(f"Error with default settings: {e}\n")

        # --- Example 2: Custom configuration ---
        print("--- Running with custom settings ---")
        try:
            # Example: Custom configuration for more creative output
            custom_gen_config = {"temperature": 0.8, "max_output_tokens": 512}
            
            # Example: Custom safety settings (use with caution)
            # This example blocks nothing.
            custom_safety = [{"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_NONE"}]
            
            custom_gemini = GeminiModel(
                api_key=API_KEY,
                model_name="gemini-1.5-flash",
                generation_config=custom_gen_config,
                safety_settings=custom_safety
            )
            
            response_custom = custom_gemini.generate_content("Write a poetic, one-sentence introduction to AI.")
            print(f"Custom Response: {response_custom}\n")
        except Exception as e:
            print(f"Error with custom settings: {e}\n")
