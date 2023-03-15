import os
import openai
from random import choice
import dotenv
from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
start_sequence = "\nAI:"
restart_sequence = "\nHuman: "
# response = openai.Completion.create(
#   model="text-davinci-003",
#   prompt="The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.\n\nHuman: Hello, who are you?\nAI: I am an AI created by Pranjal. How can I help you today?\nHuman:"
#   temperature=0.9,
#   max_tokens=150,
#   top_p=1,
#   frequency_penalty=0,
#   presence_penalty=0.6,
#   stop=[" Human:", " AI:"]
# )
start_chat = prompt="The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.\n\nHuman: Hello, who are you?\nAI: I am an AI created by Pranjal. How can I help you today?\nHuman:"
def ask(question,chat_log = None):

    if chat_log is None:
        chat_log =  start_chat
        prompt = question
    response = openai.Completion.create(
        prompt = prompt,
        engine = "text-davinci-003",
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.6,
        stop=["Human:AI:"]
    )
    story = response.choices[0].text.strip()
    return str(story)

def append_interaction_to_chat_log(question, answer, chat_log=None):
    if chat_log is None:
        chat_log = start_chat
    return f'{chat_log}Human: {question}\nAI: {answer}\n'



