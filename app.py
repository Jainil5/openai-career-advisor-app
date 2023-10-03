from flask import Flask,request, jsonify
import openai
from keyfile import key
import json

openai.api_key = str(key).strip()

app = Flask(__name__)

def generate(subject, interest,input):
        messages = []
        pre_prompt = f"""
                I have selected {str(subject).strip()} for my acedemics. And my interests is {str(interest).strip()}. You need to remember this 
                and generate response for the further questions or anything asked to you.  
             """
        messages.append({"role":"user","content":pre_prompt})

        text = str(input).strip()
        prompt = f"""
            Input: {text} 
        """
        messages.append({"role":"user","content":prompt})
        response = openai.ChatCompletion.create(model= "gpt-3.5-turbo",messages = messages)
        reply = response["choices"][0]["message"]["content"]
        messages.append({"role":"assistant" , "content":"reply"})
        print(reply)
        return reply

@app.route("/ask_gpt", methods = ["POST"])
def ask_gpt():
        data = request.get_json()
        print(data)
        subject = data["subject"]
        interest = data["interest"]
        input = data["input"]
        response = generate(subject,interest,input)
        send = {"response":response}
        
        return send

if __name__ == "__main__":
      app.run(debug =True, port = 5000)