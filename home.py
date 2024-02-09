import json

data = {'Smith': 'John', 'Alex': 'Smith', ''}
def list_data():
    return data

def add_family():
    data['Family'] =

def clear_data():
    data.clear()

def save():
    with open('data', 'w') as f:
        json.dump(data, f)


def load():
    with open('data', 'r') as f:
        data.update(json.load(f))
