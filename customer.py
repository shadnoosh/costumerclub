import streamlit as st
import pandas as pd
from datetime import datetime
from auth import save_user, load_users
import hashlib
import os
CUSTOMER_FILE = "data/customers.xlsx"
USER_FILE="data/user_data.xlsx"

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()
def save_customer_info(data):
    if os.path.exists(CUSTOMER_FILE):
        df = pd.read_excel(CUSTOMER_FILE)

    else:
        df = pd.DataFrame(columns=data.keys())


    df = pd.concat([df, pd.DataFrame([data])], ignore_index=True)
    df.to_excel(CUSTOMER_FILE, index=False)

def customer_register():
    df1=load_users()

    st.title("🧾 Customer Registration")

    # Personal info
    name = st.text_input("Full Name")
    dob = st.date_input("Date of Birth")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    hashed_pass=hash_password(password)
    confirm = st.text_input("Confirm Password", type="password")
    phone = st.text_input("Phone Number")
    city = st.text_input("City")
    street = st.text_input("Street")
    address = st.text_area("Full Address")

    if st.button("Register"):
        if password != confirm:
            st.warning("Passwords do not match.")
        elif username in df1["username"].values:
            st.error("Username already has been taken.")
            return False  # already exists
        else:
            # Save login credentials
            save_user(username, hashed_pass, role="customer")

            # Save customer details
            customer_data = {
                "username": username,
                "password":hashed_pass,
                "name": name,
                "dob": dob,
                "phone": phone,
                "city": city,
                "street": street,
                "address": address,
                "registration_date": datetime.now().date()
            }
            save_customer_info(customer_data)

            st.success("🎉 Customer registered successfully!")
