import pyrebase

firebaseConfig = {
    "apiKey": "AIzaSyDIfq7M-T-4UJrIO82lzIqG_8E2PC7ETTg",
    "authDomain": "testlienket-56e1c.firebaseapp.com",
    "databaseURL": "https://testlienket-56e1c-default-rtdb.firebaseio.com/",
    "projectId": "testlienket-56e1c",
    "storageBucket": "testlienket-56e1c.appspot.com",
    "messagingSenderId": "813859433634",
    "appId": "1:813859433634:web:a007fdc59b67fd4be37bfb"
}

# firebaseConfig = {
#     'apiKey': "AIzaSyAv9z7nqC6sa87UKuU4d7AMkVG1iC3gJOA",
#     'authDomain': "upload-video-536b1.firebaseapp.com",
#     'databaseURL': "https://upload-video-536b1-default-rtdb.firebaseio.com",
#     'projectId': "upload-video-536b1",
#     'storageBucket': "upload-video-536b1.appspot.com",
#     'messagingSenderId': "717745140687",
#     'appId': "1:717745140687:web:f6603b9bd2fee68d5158ba",
# }

firebase = pyrebase.initialize_app(firebaseConfig)

db = firebase.database()
storage = firebase.storage()

