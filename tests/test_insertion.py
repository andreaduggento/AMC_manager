
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
      "_id": "unique_problem_id",
      "group_id": "3Farc_g004",
      "q_id": "3Farc_g004_q001",
      "short_title": "Submerged Volume",
      "long_title": "Calculating the Submerged Volume of an Object",
      "main_topic": "Fluidi_Archimede",
      "topic_tags": ["buoyancy", "density", "Archimedes' principle", "submerged volume"],
      "skill_tags": [],
      "target": ["triennali"],
      "question": {
        "pre_latex": """
          \\FPeval\\objectDensity{clip(round(random*400+600,0))} % Density of the object in kg/m^3, ensuring it's less than water to float
          \\FPeval\\waterDensity{1000} % Density of water in kg/m^3
          \\FPeval\\totalVolume{clip(round(random*0.5+0.5,2))} % Total volume of the object in m^3
          \\FPeval\\submergedVolume{clip(\\objectDensity/\\waterDensity*\\totalVolume)} % Submerged volume calculation based on density ratio
          \\FPeval\\wrongOne{clip(\\totalVolume - \\submergedVolume)} % Mistake: Non-submerged volume instead of submerged
          \\FPeval\\wrongTwo{clip(\\submergedVolume + 0.1)} % Randomly added volume, incorrect
          \\FPeval\\wrongThree{clip(\\submergedVolume - 0.1)} % Randomly subtracted volume, incorrect if it makes sense
          \\FPeval\\wrongFour{clip(\\totalVolume)} % Assumes the object is completely submerged, incorrect
          \\FPeval\\wrongFive{0} % Assumes the object does not submerge at all, incorrect
        """,
        "italian_latex": "Un oggetto con densità \\(\\objectDensity \\, \\text{kg/m}^3\\) e volume totale \\(\\totalVolume \\, \\text{m}^3\\) viene immerso in acqua. Calcola il volume dell'oggetto che sarà immerso.",
        "english_latex": "An object with a density of \\(\\objectDensity \\, \\text{kg/m}^3\\) and a total volume of \\(\\totalVolume \\, \\text{m}^3\\) is submerged in water. Calculate the volume of the object that will be submerged.",
        "image": None
      },
      "solution": {
        "italian": "Il volume immerso dell'oggetto è \\(\\submergedVolume \\, \\text{m}^3\\), calcolato come \\(\\frac{\\objectDensity}{\\waterDensity} \\times \\totalVolume\\).",
        "english": "The submerged volume of the object is \\(\\submergedVolume \\, \\text{m}^3\\), calculated as \\(\\frac{\\objectDensity}{\\waterDensity} \\times \\totalVolume\\)."
      },
      "format": ["multiple_choice"],
      "AMC_correctchoice": {
        "italian": "\\(\\submergedVolume \\, \\text{m}^3\\)",
        "english": "\\(\\submergedVolume \\, \\text{m}^3\\)"
      },
      "AMC_wrongchoices": {
        "italian": [
          "\\(\\wrongOne \\, \\text{m}^3\\)",
          "\\(\\wrongTwo \\, \\text{m}^3\\)",
          "\\(\\wrongThree \\, \\text{m}^3\\)",
          "\\(\\wrongFour \\, \\text{m}^3\\)",
          "\\(\\wrongFive \\, \\text{m}^3\\)"
        ],
        "english": [
          "\\(\\wrongOne \\, \\text{m}^3\\)",
          "\\(\\wrongTwo \\, \\text{m}^3\\)",
          "\\(\\wrongThree \\, \\text{m}^3\\)",
          "\\(\\wrongFour \\, \\text{m}^3\\)",
          "\\(\\wrongFive \\, \\text{m}^3\\)"
        ]
      }
    }

    # Insert the document into CouchDB
    # Replace 'your_username' and 'your_password' with your actual CouchDB credentials
    auth = ('your_username', 'your_password')
    insert_document(db_url, doc, auth=auth)
