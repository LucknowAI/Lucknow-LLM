import textwrap
import google.generativeai as genai
from IPython.display import Markdown
import time

GOOGLE_API_KEY = "AIzaSyBE2A0E_MIpf-i9cZRSRXP430Br4FZxJqc"


class TrainDataCreator:
    model = genai.GenerativeModel('gemini-pro')
    genai.configure(api_key=GOOGLE_API_KEY)

    def __init__(self):
        pass

    @staticmethod
    def get_prompt():
        with open('prompt.txt', 'r') as f:
            prompt_data = f.read()
        return prompt_data

    @staticmethod
    def to_markdown(text):
        text = text.replace('•', '  *')
        return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

    def create(self, file, new_file_name='train_data.json'):
        """Provides instances in gemini format.

        This function takes text file as input and provide
        output in formate of pairs of question and answer.
        :param file: absolute path of file
        :return lines: list of JSON objects."""

        prompt = self.get_prompt()
        new_train_file = open(new_file_name, 'w')
        with open(file) as file:
            lines = file.readlines()
            for line in lines:
                full_prompt = prompt + line + "\n\nOutput: \n"
                gemini_response = self.model.generate_content(full_prompt)
                try:
                    response_ = eval(gemini_response.text)
                    print(gemini_response.text)
                    new_train_file.writelines(gemini_response.text)
                except Exception as e:
                    print( "Response format Error")

    def clean(self, file):
        clean_file = open('clean_file.txt', 'w')
        with open(file, 'r') as file:
            lines = file.readlines()
            for line in lines:
                if len(line) < 5:
                    pass
                else:
                    clean_file.write(line)
        print("File have no blank line now!")

creator = TrainDataCreator()
# path = "/home/thor_x_me/PycharmProjects/Lucknow-LLM-data/Unstructured_data/Famous_Personalities/Famous_personalities.txt"
# creator.clean(path)
clean_path = "/home/thor_x_me/PycharmProjects/Lucknow-LLM-data/scripts/clean_file.txt"
creator.create(clean_path)
