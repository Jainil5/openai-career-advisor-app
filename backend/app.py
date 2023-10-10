from flask import Flask,request, jsonify
from openai_api import generate

app = Flask(__name__)

@app.route("/ask_gpt", methods = ["POST"])
def ask_gpt():
        data = request.get_json()
        # print(data)
        input = data["input"]
        response = generate(input)
        send = {"response":response}
        return send



if __name__ == "__main__":
      app.run(debug =True, port = 5000)