from flask import Flask, request, session
from twilio.twiml.messaging_response import MessagingResponse
from chatbot import main
from main import *
app = Flask(__name__)
@app.route('/Ressbot',methods = ['POST'])
def ress():
    incoming_msg = request.values['body']
    chat_log = session.get('chat_log')
    answer = ask(incoming_msg, chat_log)
    session['chat_log'] = append_interaction_to_chat_log(incoming_msg, answer,
    chat_log)
    msg = MessagingResponse()
    msg.message(answer)
    return str(msg)

if __name__ == '__main__':
 app.run(debug=True)