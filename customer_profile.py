import streamlit as st
import pandas as pd
import os

CUSTOMER_FILE = "data/customers.xlsx"

def get_customer_data(username):
    if os.path.exists(CUSTOMER_FILE):
        df = pd.read_excel(CUSTOMER_FILE)
    else:
        return None
    return df[df["username"] == username].iloc[0] if username in df["username"].values else None

def update_customer_data(username, updated_data):
    df = pd.read_excel(CUSTOMER_FILE)
    idx = df[df["username"] == username].index[0]
    for key, value in updated_data.items():
        df.at[idx, key] = value
    df.to_excel(CUSTOMER_FILE, index=False)

def customer_profile(username, mode):
    if mode=="view":
        st.title("👤 My Profile")

        data = get_customer_data(username)
        if data is None:
            st.warning("No profile data found.")
            return

    # Pre-fill form
        st.subheader("📋 Your Information")
        st.write(f"**Name:** {data['name']}")
        st.write(f"**Date of Birth:** {data['dob']}")
        st.write(f"**City:** {data['city']}")
        st.write(f"**Street:** {data['street']}")
        st.write(f"**Address:** {data['address']}")
        st.write(f"**Phone:** {data['phone']}")
        st.write(f"**Register Date:** {data['registration_date']}")
    if mode=="edit":
        st.title("✏️ Edit My Profile")

        data = get_customer_data(username)
        if data is None:
            st.warning("No profile data found.")
            return

        # Pre-fill form
        name = st.text_input("Full Name", data["name"])
        dob = st.date_input("Date of Birth", pd.to_datetime(data["dob"]))
        phone = st.text_input("Phone Number", data["phone"])
        city = st.text_input("City", data["city"])
        street = st.text_input("Street", data["street"])
        address = st.text_area("Full Address", data["address"])

        if st.button("Update Profile"):
            update_customer_data(username, {
                "name": name,
                "dob": dob,
                "phone": phone,
                "city": city,
                "street": street,
                "address": address,
            })
            st.success("Profile updated successfully!")