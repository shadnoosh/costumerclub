# auth.py
import pandas as pd
import hashlib
import os

DATA_FILE = "data/user_data.xlsx"

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def load_users():
    if os.path.exists(DATA_FILE):
        return pd.read_excel(DATA_FILE)
    else:
        df = pd.DataFrame(columns=["username", "password", "role"])
        df.to_excel(DATA_FILE, index=False)
        return df

def save_user_admin(username, password):
    df = load_users()
    if username in df["username"].values:
        return False  # already exists
    new_user = pd.DataFrame([[username, hash_password(password)]], "admin",  columns=["username", "password", "role"])
    df = pd.concat([df, new_user], ignore_index=True)
    df.to_excel(DATA_FILE, index=False)
    return True

def save_user(username, password, role="customer"):
    df = load_users()
    if username in df["username"].values:
        return False  # already exists

    new_user = {"username": username, "password": password, "role": role}
    df = pd.concat([df, pd.DataFrame([new_user])], ignore_index=True)
    df.to_excel(DATA_FILE, index=False)
    return True
def authenticate(username, password):
    df = load_users()
    hashed = hash_password(password)
    user_row = df[(df["username"] == username) & (df["password"] == hashed)]
    return not user_row.empty

def get_user_role(username):
    df = pd.read_excel(DATA_FILE)
    user = df[df["username"] == username]
    if not user.empty:
        return user.iloc[0]["role"]
    return None