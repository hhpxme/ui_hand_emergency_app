import requests

r = requests.get('https://firebasestorage.googleapis.com/v0/b/upload-video-536b1.appspot.com/o/?alt=media')

with open('f.json', 'wb') as f:
    f.write(r.content)
