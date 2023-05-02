# Python program to read
# json file


import json

def init_data():
    template = """
    'game_data': {
    'level_attained' : 5
    }
    """

def read_data():
    # Opening JSON file
    json_file = open('game_data.json')

    # returns JSON object as
    # a dictionary
    data = json.load(json_file)

    # Iterating through the json
    # list
    for i in data['game_configuration']:
        print(i)

    # Closing file
    json_file.close()
