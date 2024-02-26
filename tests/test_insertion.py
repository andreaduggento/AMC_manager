
import requests
import json

def insert_document(db_url, doc, auth=None):
    headers = {'Content-type': 'application/json'}
    response = requests.post(db_url, data=json.dumps(doc), headers=headers, auth=auth)
    
    if response.status_code == 201:
        print("Document inserted successfully.")
    else:
        print("Failed to insert document:", response.text)

if __name__ == "__main__":
    db_url = 'http://localhost:5984/amc_01'
    
    # Example document
    doc = {
      "_id": "example_problem_001",
      "short_title": "Free Fall",
      "long_title": "Calculate the time for a free-falling object",
      "main_topic": "Mechanics",
      "topic_tags": ["free fall", "motion"],
      "skill_tags": ["calculation", "conceptual"],
      "target": ["high school", "undergraduate"],
      "question": {
        "pre_latex": "Given an object in free fall, calculate the time it takes to hit the ground.",
        "italian_latex": "Dato un oggetto in caduta libera, calcolare il tempo che impiega per toccare il suolo.",
        "english_latex": "Given an object in free fall, calculate the time it takes to hit the ground.",
        "image": None
      },
      "solution": "t = \sqrt{\frac{2h}{g}}",
      "format": ["open"],
      "AMC_correctchoice": {
        "italian": "Correct answer in Italian",
        "english": "Correct answer in English"
      },
      "AMC_wrongchoices": {
        "italian": ["Wrong answer A in Italian", "Wrong answer B in Italian", "Wrong answer C in Italian"],
        "english": ["Wrong answer A in English", "Wrong answer B in English", "Wrong answer C in English"]
      }
    }
    
    # Insert the document into CouchDB
    # Replace 'your_username' and 'your_password' with your actual CouchDB credentials
    auth = ('your_username', 'your_password')
    insert_document(db_url, doc, auth=auth)
