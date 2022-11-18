import json

# Opening JSON file
f = open('f.json')

# returns JSON object as
# a dictionary
data = json.load(f)

# Iterating through the json
# list
for i in data['items']:
    s1 = str(i).split(': ')
    s2 = s1[1].split('\'')
    print(s2[1])
