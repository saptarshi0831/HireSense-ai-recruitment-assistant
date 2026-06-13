import json

from pathlib import Path

DB = Path("data/candidates.json")

def load_db():

    with open(DB, "r") as f:
        return json.load(f)
    
def save_candidate(candidate):

    data = load_db()

    data.append(candidate)
    
    with open (DB, "w") as f:

        json.dump(data,
                  f,
                  indent=2)