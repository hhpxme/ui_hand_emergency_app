import firebase_config
import requests
import json

def get_video_name():
    url = firebase_config.storage.get_url(None)
    r = requests.get(url)
    with open('json_file/f.json', 'wb') as f:
        f.write(r.content)

    # Opening JSON file
    f = open('json_file/f.json')

    # returns JSON object as
    # a dictionary
    data = json.load(f)

    name = []
    # Iterating through the json
    # list
    for i in data['items']:
        s1 = str(i).split(': ')
        s2 = s1[1].split('\'')
        name.append(s2[1])

    return name

# print(get_video_name())
