import streamlit as st
import pandas as pd
import os
from datetime import datetime
from utils import notify_admin

PRODUCTS_FILE = "data/products.xlsx"
PURCHASE_FILE = "data/purchase_history.xlsx"

def load_products():
    if os.path.exists(PRODUCTS_FILE):
        return pd.read_excel(PRODUCTS_FILE)
    else:
        return pd.DataFrame()
def save_products(products_df):
    products_df.to_excel(PRODUCTS_FILE, index=False)
def save_purchase(purchase_data):
    if os.path.exists(PURCHASE_FILE):
        df = pd.read_excel(PURCHASE_FILE)
        df = pd.concat([df, pd.DataFrame([purchase_data])], ignore_index=True)
    else:
        df = pd.DataFrame([purchase_data])
    df.to_excel(PURCHASE_FILE, index=False)

def purchase_page():
    st.title("🛒 Make a Purchase")

    username = st.session_state.get("user")
    if not username:
        st.warning("⚠️ You must be logged in to make a purchase.")
        return

    products = load_products()
    if products.empty:
        st.info("No products available.")
        return

    st.subheader("Available Products")
    st.dataframe(products[["Product ID", "Product Name", "Category", "Price", "In Stock"]])

    st.markdown("---")
    st.subheader("🛍️ Purchase Form")

    product_name = st.selectbox("Select Product", products["Product Name"])
    quantity = st.number_input("Quantity", min_value=1, step=1)

    product_info = products[products["Product Name"] == product_name].iloc[0]
    price = product_info["Price"]
    in_stock = product_info["In Stock"]
    total = price * quantity

    st.markdown(f"💰 **Total Price: ${total:.2f}**")
    st.markdown(f"📦 **In Stock: {in_stock} items**")

    if st.button("Confirm Purchase"):
        if quantity > in_stock:
            st.error("❌ Not enough stock available.")
            return

        # Save purchase to history
        purchase_data = {
            "Username": username,
            "Product ID": product_info["Product ID"],
            "Product Name": product_name,
            "Quantity": quantity,
            "Total Price": total,
            "Purchase Date": datetime.now().strftime("%Y-%m-%d")
        }
        save_purchase(purchase_data)
        notify_admin(purchase_data)

        # Update and save stock
        remaining_stock = in_stock - quantity
        products.loc[products["Product Name"] == product_name, "In Stock"] = remaining_stock
        save_products(products)


        st.success("✅ Purchase successful!")
        st.info(f"🗃️ Remaining stock for **{product_name}**: {remaining_stock}")

        # 🚨 Low stock alert
        if remaining_stock < 3:
            st.warning(f"⚠️ Stock for **{product_name}** is running low ({remaining_stock} left). Consider restocking soon.")

        # 🧾 Show user purchase history
        if os.path.exists(PURCHASE_FILE):
            df = pd.read_excel(PURCHASE_FILE)
            user_history = df[df["Username"] == username]
            st.markdown("---")
            st.subheader("🧾 Your Purchase History")
            st.dataframe(user_history)