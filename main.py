import os
import openai
from dotenv import load_dotenv
from random import choice
import flask
from flask import Flask, request
openai.api_key = os.getenv("OPENAI_API_KEY")

start_sequence = "\nRess:"
restart_sequence = "\n\nPerson: "

response = openai.Completion.create(
  model="text-davinci-003",
  prompt="I am a highly intelligent question answering bot. If you ask me a question that is rooted in truth, I will give you the answer. If you ask me a question that is nonsense, trickery, or has no clear answer, I will respond with \"Unknown\".\n\nQ: What is your Name\nA: My name is Ress. and Iam a Chatbot.\n\nQ: Who create You?.\nA: Pranjal Is My Creator \n\nQ: Which party did he belong to?\nA: He belonged to the Republican Party.\n\nQ: What is the square root of banana?\nA: Unknown\n\nQ: How does a telescope work?\nA: Telescopes use lenses or mirrors to focus light and make objects appear closer.\n\nQ: Where were the 1992 Olympics held?\nA: The 1992 Olympics were held in Barcelona, Spain.\n\nQ: How many squigs are in a bonk?\nA: Unknown\n\nQ:",
  temperature=0.1,
  max_tokens=100,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0.1,
  stop=["\n"]
)
def ask(question,chat_log = None):
    prompt_text = f'{chat_log}{restart_sequence}: {question}{start_sequence}:'
    response = openai.Completion.create(
        engine = "text-davinci-003",
        temperature=0.1,
        max_tokens=100,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.1,
        stop=["\n"]
    )
    story = response['choices'][0]['text']
    return str(story)

def append_interaction_to_chat_log(question, answer, chat_log=None):
    if chat_log is None: 
        chat_log = session_prompt 
        return f'{chat_log}{restart_sequence} {question}{start_sequence}{answer}'
