import os
from deta import Deta
from dotenv import load_dotenv
import streamlit as st


load_dotenv(".env")
DETA_KEY = os.getenv("DATA_KEY")

if 'key' not in st.session_state:
    st.session_state['key'] = 'value'

# Session State also supports attribute based syntax
if 'key' not in st.session_state:
    st.session_state.key = 'value'
        
deta = Deta(project_key=st.secrets["DETA_KEY"])
db = deta.Base("user_db")

def insert_user(username, name, password):
    return db.put({"key": username, "name": name, "password": password})

def fecth_all_users():
    res = db.fetch()
    return res.items

def get_user(username):
      return db.get(username)
  
def update_user(username, updates):
    return db.update(updates, username)

def delete_user(username):
    return db.delete(username)