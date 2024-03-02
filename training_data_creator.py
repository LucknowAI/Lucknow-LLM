
import textwrap
import google.generativeai as genai
from IPython.display import Markdown

GOOGLE_API_KEY = "PASTE YOUR API KEY HERE"


class TrainDataCreator:
    model = genai.GenerativeModel('gemini-pro')
    genai.configure(api_key=GOOGLE_API_KEY)

    def __init__(self):
        pass

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

        prompt = """
        You are an advanced and skilled question-answer generator, 
        tasked with the intricate job of dissecting paragraphs to 
        craft a series of engaging and insightful questions and 
        answers. Your primary objective is to delve into the essence 
        of the paragraph, extracting pivotal information and themes 
        to formulate questions that are not only relevant but also 
        ching to the reader's understanding of the text. It's crucial 
        that the questions you generate are tightly aligned with the 
        content provided, ensuring no new, unrelated facts are 
        introduced. Your responses should accurately reflect the 
        information within the paragraph, presenting it in a manner 
        that's both informative and easily comprehensible. 
        your output format is valid json format 
        {  "text": "<start_of_turn>user # ... <end_of_turn><start_of_turn>model # ... <end_of_turn>"}, {  "text": "<start_of_turn>user # ... <end_of_turn><start_of_turn>model # ... <end_of_turn>"}
    examples
    input: 
    "The Nawabs of Lucknow, in reality, the Nawabs of Awadh, acquired the name after the reign of the third Nawab when Lucknow became their capital. The city became North India's cultural capital, and its nawabs, best remembered for their refined and extravagant lifestyles, were patrons of the arts. Under their dominion, music and dance flourished, and construction of numerous monuments took place.[32] Of the monuments standing today, the Bara Imambara, the Chota Imambara, and the Rumi Darwaza are notable examples. One of the Nawab's enduring legacies is the region's syncretic Hindu–Muslim culture that has come to be known as the Ganga-Jamuni Tehzeeb."
    Output:
    {
        "text": "<start_of_turn>user # What is the history behind the title of Nawabs of Lucknow? <end_of_turn><start_of_turn>model # The title of Nawabs of Lucknow, originally Nawabs of Awadh, was adopted after Lucknow became the capital during the reign of the third Nawab. <end_of_turn>"
    },
    {
        "text": "<start_of_turn>user # What made Lucknow the cultural capital of North India? <end_of_turn><start_of_turn>model # Lucknow became North India's cultural capital under the nawabs' patronage, who were known for their extravagant lifestyles and support of the arts. <end_of_turn>"
    },
    {
        "text": "<start_of_turn>user # How did the Nawabs of Lucknow contribute to the arts? <end_of_turn><start_of_turn>model # The Nawabs of Lucknow were patrons of the arts, under whom music and dance flourished and numerous monuments were constructed. <end_of_turn>"
    }
        """
        gemini_response = self.model.generate_content(prompt + txt)
        lines = gemini_response.text.split(",")
        return lines
