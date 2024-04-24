
import requests

res = requests.get("http://127.0.0.1:5000")
print(res)
print(res.text)


query = {
    "prompt": """
Hello Mixtral, can you say something nice to Josef?
"""
}

res = requests.post("http://127.0.0.1:5000/query", json=query)
print(res)
print(res.json()["response"])

query = {
    "prompt": """
Statements about Klaus Mueller
1. Klaus Mueller is writing a research paper
2. Klaus Mueller enjoys reading a book on gentrification
3. Klaus Mueller is conversing with Ayesha Khan about excercising
What 5 high-level insights can you infer from the above statesments?
(example format: insight (because of 1, 3))
"""
}

res = requests.post("http://127.0.0.1:5000/query", json=query)
print(res)
print(res.json()["response"])
