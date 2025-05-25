import streamlit as st
import pandas as pd
import os

PURCHASE_FILE = "data/purchases.xlsx"

def user_purchase_history(username):
    st.title("🛒 Purchase History")

    if os.path.exists(PURCHASE_FILE ):
        df = pd.read_excel(PURCHASE_FILE )
        user_purchases = df[df["username"] == username]
        if user_purchases.empty:
            st.info("You haven't made any purchases yet.")
        else:
            st.dataframe(user_purchases)

    else:
        st.error("no purchased has been saved yet")


