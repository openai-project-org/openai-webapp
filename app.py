from flask import Flask, render_template, request
import openai
import requests
import os

app = Flask(__name__)

#OPENAI_SERVICE_URL = "http://localhost:8081" # rushane/webapp-image:1.0
OPENAI_SERVICE_URL = os.environ.get('OPENAI_SERVICE_URL')## rushane/webapp-image:1.2
OPENAI_SERVICE_URL = f"http://{OPENAI_SERVICE_URL}" # rushane/webapp-image:1.2

@app.route("/")
def index():
#    return OPENAI_SERVICE_URL
    return render_template("index.html")

@app.route("/complete", methods=["GET", "POST"])
def complete():
    if request.method == "POST":
        prompt = request.form["prompt"]

        try:
            response = requests.post(OPENAI_SERVICE_URL + "/completions", json={'input_text': prompt})
            result = response.json()
            return render_template("complete.html", prompt=prompt, response=result)

        except:
            return 'Could not access the chat service'

    else:
        return render_template("complete.html")

@app.route("/chat", methods=["GET", "POST"])
def chat():
    if request.method == "POST":
        #prompt = request.form["prompt"]
        #response = openai.Completion.create(engine="davinci", prompt=prompt, max_tokens=1000, )
        #return render_template("complete.html", prompt=prompt, response=response.choices[0].text)
        return "We are still building this page"
    else:
        return render_template("chat.html")

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0',port='8080')
