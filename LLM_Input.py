from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()


llm = ChatOpenAI(temperature=0, model_name='gpt-4o-mini')

class LLM_Model():
    def __init__(self, input):
        self.input = input

    def Initiate_Response(self):
        user_prompt = self.input
        Tone_Prompt = """
            You are to take the user input {user_prompt} and categorize the user input into one of the following 
            categories: Cold, Warm, Sunny, Gloomy, or Neutral.
            Once you have decided on the categories, you must only give the category back
            as a reponse. Do not add anything else to the reponse. Do not explain why you
            chose the category. Simply just give the category and nothing else.

            Example Output:
            Cold
        """

        Tone_Prompt_Template = PromptTemplate.from_template(Tone_Prompt)
        Tone_Prompt_Chain = Tone_Prompt_Template | llm | StrOutputParser()

        Invoke = Tone_Prompt_Chain.invoke({user_prompt})
        return Invoke
    

if __name__ == "__main__":
    user_input = input('Type Prompt Here: ')
    LLM_Model(user_input).Initiate_Response()