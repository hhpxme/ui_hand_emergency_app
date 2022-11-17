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

firebase = pyrebase.initialize_app(firebaseConfig)
