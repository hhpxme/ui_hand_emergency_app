import firebase_config

import smtplib
import random
from email.message import EmailMessage


def email_alert(subject, body, to):
    msg = EmailMessage()
    msg.set_content(body)
    msg["subject"] = subject
    msg["to"] = to

    user = "doanchuyennganh.it@gmail.com"
    msg["from"] = user
    password = "mdvqurhxrcyjhybv"

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(user, password)
    server.send_message(msg)

    server.quit()


auth = firebase_config.firebase.auth()

email = input("Enter your email here:\n")
password = input("Enter your password:\n")
count = 0
while count <= 3:
    confirmpass = input("Confirm your password:\n")
    if password == confirmpass:
        random = random.randint(1000, 9999)

        subject = "Email verification"
        body = f"The code to verification your email is: {random}"
        email_alert(subject, body, email)

        verification = int(input("Ente"
                                 "r your verification code here:\n"))
        print(random)
        if verification == random:
            try:
                auth.create_user_with_email_and_password(email, password)
                print("Sign-up successfully")
            except:
                print("Can't sign-up")
        else:
            print("Error")
    else:
        count += 1
        print("Confirm your password again!!!")
else:
    print("Try again late!!!")
