import streamlit_authenticator as stauth
import database as db
usernames = ["aaditi", "mansi"]
names = ["Aaditi Manjalkar", "Mansi Mane"]
password = ["abc123", "def456"]
hashed_password = stauth.Hasher(password).generate()
for (username, name, hash_password) in zip(usernames, names, hashed_password): 
    db.insert_user(username, name, hash_password) 