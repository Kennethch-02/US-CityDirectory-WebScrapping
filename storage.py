import os
import json

def save_to_txt(title, data):
    if not os.path.exists('Data'):
        os.makedirs('Data')
    filename = os.path.join('Data', title.replace(" ", "_") + ".txt")
    
    with open(filename, 'w') as f:
        f.write(json.dumps(data))


def save_to_database(data):

    with open('database.json', 'w') as f:
        f.write(json.dumps(data))
