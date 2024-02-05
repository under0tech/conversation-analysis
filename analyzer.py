import os
import time
import json
import utils
import nltk
from nltk.tokenize import word_tokenize

nltk.download('punkt')

threat_keywords_list = [
    {"category": "TERRORISM", "keywords": ["terror", "extremist", "radical", "insurgency"]},
    {"category": "GANG-RELATED", "keywords": ["gang", "territory", "rivalry", "faction"]},
    {"category": "HATE-CRIME", "keywords": ["hate", "discrimination", "bias", "prejudice", "bigotry", "intolerance"]},
    {"category": "WEAPON", "keywords": ["gun", "knife", "firearm", "explosive", "ammunition", "blade"]},
    {"category": "SHOOTING", "keywords": ["shooting", "gunfire", "sniper", "shootout", "gunshot", "fire"]},
    {"category": "CAR-RELATED", "keywords": ["carjacking", "accident", "collision", "car-theft", "speeding", "wrong-way"]},
    {"category": "VIOLENCE", "keywords": ["assault", "attack", "threaten", "harm", "aggression", "violence"]},
    {"category": "CRIMINAL", "keywords": ["robbery", "burglary", "drug", "kidnapping", "felony", "heist"]},
    {"category": "HOSTAGE", "keywords": ["hostage", "abduction", "ransom", "detention", "confinement"]},
    {"category": "CRISIS", "keywords": ["crisis", "emergency", "disaster", "calamity"]},
    {"category": "CYBERSECURITY", "keywords": ["hacking", "malware", "breach", "cybercrime"]}
]

def detect_threat(message):
    tokens = word_tokenize(message)
    tokens_lower = [token.lower() for token in tokens]
    for category_keywords in threat_keywords_list:
        if any(keyword in tokens_lower for keyword in category_keywords["keywords"]):
            return category_keywords["category"]
    return "REGULAR"

def analyzer_go(
        wait_time,  
        input_folder, 
        output_folder, 
        stop_command):
    
    while not stop_command.is_set():

        time.sleep(wait_time)
        json_files = [file for file in os.listdir(input_folder) if file.endswith(".json")]
        
        for file in json_files:
            try:
                if stop_command.is_set():
                    break
            
                json_file_path = f'{input_folder}/{file}'
                with open(json_file_path, 'r') as file:
                    data = json.load(file)
                threat_category = detect_threat(data['speech'])
                if threat_category != 'REGULAR':
                    data['category'] = threat_category
                    with open(json_file_path, 'w') as file:
                        json.dump(data, file, indent=2)
                    utils.move_file(json_file_path, output_folder)
                    utils.move_file(f'{input_folder}/{data["file"]}', output_folder)
                    print(f'THREAT FOUND -- \033[91m{threat_category}\033[0m' + 
                          f' in file {data["file"]}: {data["speech"]}')
                else:
                    os.remove(json_file_path)
                    os.remove(f'{input_folder}/{data["file"]}')

            except Exception as e:
                print(f"An error occurred: {e}")

    stopped_time = time.strftime("%H:%M:%S, %Y, %d %B", time.localtime())
    print(f'thread \033[93mAnalyzer\033[0m, DONE at {stopped_time}.')




