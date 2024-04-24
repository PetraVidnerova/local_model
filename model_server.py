import json 
from flask import Flask, request, jsonify
from model import MixtralModel

model = MixtralModel()

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, this is your Mixtral model.'

@app.route('/query', methods=['POST'])
def query_model():
 data = json.loads(request.data)
 print(data)
 response = model.answer(data["prompt"])

 # response = """
 # Hello, Mixtral is down.
 # So sadly down.
 # Deep down.
 # """

 return jsonify({ 'response': response }), 200



if __name__ == "__main__":
    app.run()
