import json 
from flask import Flask, request, jsonify
from model import MixtralModel, Embedding 

model = MixtralModel()
embed = Embedding()

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, this is your Mixtral model.'

@app.route('/query', methods=['POST'])
def query_model():
 data = json.loads(request.data)
 print(data)
 try: 
     response = model.answer(data["prompt"])
 except Exception as e:
     print(e)
     return jsonify({}), 404
 # response = """
 # Hello, Mixtral is down.
 # So sadly down.
 # Deep down.
 # """

 return jsonify({ 'response': response }), 200

@app.route('/embed', methods=['POST'])
def embedding():
    data = json.loads(request.data)
    response = embed.encode(data["sentences"])
    return jsonify({'embeddings': response}), 200



if __name__ == "__main__":
    app.run()
