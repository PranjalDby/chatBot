from flask import Flask, request,session,render_template,url_for,redirect
import openai
import os
import main
# openai.api_key = os.getenv("OPENAI_API_KEY")
app = Flask(__name__)
ans = ""
@app.route("/",methods = ("GET","POST"))
def create_layout():
    global ans
    if request.method == "POST":
        ques = request.form['ques']
        print(ques)
        ans = main.ask(ques)
        chat_log = main.append_interaction_to_chat_log(ques,ans)
    
    result = ans
    return render_template("index.html",result = result)

def generate(result):
    for i in result:
        "".join(i)
if __name__ == '__main__':
    app.run()
