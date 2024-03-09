import textwrap
import google.generativeai as genai
from IPython.display import Markdown
import time
import data_preprocessing


def get_api_key(api_key_file="/home/thor_x_me/PycharmProjects/Lucknow-LLM-data/scripts/API_KEY.txt"):
    """
    :param api_key_file: Path of API key saved in a text file
    :return: API key string
    """
    with open(api_key_file) as key:
        api_key = key.read()
        return api_key


GOOGLE_API_KEY = get_api_key()


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
        """ This function takes text file as input and provide list of objects
         in a json file. Objects are of format provided in prompt.

        :param file:
        :param new_file_name:
        :return: json file containing list of objects"""

        prompt = self.get_prompt()
        new_train_file = open(new_file_name, 'w')       # New objects will be saved here
        new_train_file.writelines('[')
        failed_lines = open('failed_lines.txt', 'w')    # Sentence group which failed generating objects are saved here
        with open(file) as file:
            lines = file.readlines()
            for line in lines:
                sentences = data_preprocessing.split_into_segments(line)    # Breaking paragraph into manageable chunks
                for sentence in sentences:
                    full_prompt = prompt + sentence + "\n\nOutput: \n"
                    gemini_response = self.model.generate_content(full_prompt)
                    try:
                        response_ = eval("[" + gemini_response.text + "]")
                        print(gemini_response.text)
                        new_train_file.writelines(gemini_response.text)
                        time.sleep(2)
                    except Exception as e:
                        print( "Response format Error")
                        print(gemini_response.text)
                        failed_lines.writelines(line)
        new_train_file.writelines(']')
        new_train_file.close()
        failed_lines.close()
        file.close()
        return new_file_name

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
# clean_path = "/home/thor_x_me/PycharmProjects/Lucknow-LLM-data/scripts/clean_file.txt"
# creator.create(clean_path)
