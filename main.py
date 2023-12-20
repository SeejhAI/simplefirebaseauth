import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth

cred = credentials.Certificate("fastapiauth-b1b8a-firebase-adminsdk-h0ytw-eb421fe0df.json")
firebase_admin.initialize_app(cred)

email = "ishaque@example.com"
password = "123456"

user = auth.create_user(email=email, password=password)
print(user.uid)
# print(cred)