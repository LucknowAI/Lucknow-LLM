import textwrap
import google.generativeai as genai
from IPython.display import Markdown

GOOGLE_API_KEY = "PASTE YOUR API KEY HERE"


class TrainDataCreator:
    model = genai.GenerativeModel('gemini-pro')
    genai.configure(api_key=GOOGLE_API_KEY)

    def __init__(self):
        pass

    def get_prompt(self):
        with open('prompt_text.txt', 'r') as f:
            prompt_data = f.read()
        return prompt_data

    @staticmethod
    def to_markdown(text):
        text = text.replace('•', '  *')
        return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

    def create(self, txt: str):
        """Provides instances in gemini format.

        This function takes paragraph(str) as input and provide
        pairs of question and answer in gemini format.
        Pairs can be more than one, so use accordingly.
        :param txt: string
        :return lines: list of JSON objects."""

        prompt = self.get_prompt()
        full_prompt = prompt + txt + "\n\nOutput: \n"
        gemini_response = self.model.generate_content(full_prompt)
        try:
            response_ = eval(gemini_response.text)
            return response_
        except Exception as e:
            return "Response format Error"
