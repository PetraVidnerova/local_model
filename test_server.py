
import requests

res = requests.get("http://127.0.0.1:5000")
print(res)
print(res.text)

        

query = {
    "prompt": """
Name: Isabella Rodriguez
Age: 34
Innate traits: friendly, outgoing, hospitable
Learned traits: Isabella Rodriguez is a cafe owner of Hobbs Cafe who loves to make people feel welcome. She is always looking for ways to make the cafe a place where people can come to relax and enjoy themselves.
Currently: Isabella Rodriguez is planning on having a Valentine's Day party at Hobbs Cafe with her customers on February 14th, 2023 at 5pm. She is gathering party material, and is telling everyone to join the party at Hobbs Cafe on February 14th, 2023, from 5pm to 7pm.
Lifestyle: Isabella Rodriguez goes to bed around 11pm, awakes up around 6am.
Daily plan requirement: Isabella Rodriguez opens Hobbs Cafe at 8am everyday, and works at the counter until 8pm, at which point she closes the cafe.
Current Date: Monday February 13


In general, Isabella Rodriguez goes to bed around 11pm, awakes up around 6am.
Isabella's wake up hour? Output only the number. The output format is: *<NUMBER>*
Do not print anything else than the output format between the stars.
"""
}

res = requests.post("http://127.0.0.1:5000/query", json=query)
print(res)
print(res.json()["response"])


#query = {
#    "prompt": """
#Statements about Klaus Mueller
#1. Klaus Mueller is writing a research paper
#2. Klaus Mueller enjoys reading a book on gentrification
#3. Klaus Mueller is conversing with Ayesha Khan about excercising
#What 5 high-level insights can you infer from the above statesments?
#(example format: insight (because of 1, 3))
#"""
#}
#
#res = requests.post("http://127.0.0.1:5000/query", json=query)
#print(res)
#print(res.json()["response"])

