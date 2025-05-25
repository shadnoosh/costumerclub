import streamlit as st
# import pandas as pd
from auth import authenticate, save_user, get_user_role
from dashboard import show_dashboard, show_low_stock_alert, show_costumer_purchase_history
from customer_profile import customer_profile, update_customer_data
from customer import  customer_register
from purchase_history import user_purchase_history
from manage_products import admin_manage_products
from purchase import purchase_page
from utils import show_costumer_purchase

# import os

st.set_page_config(page_title="Costumer Club", page_icon="🌟", layout="centered")
st.title("Costumer Club")
with open("assets/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
if "page" not in st.session_state:
        st.session_state["page"] = "Login"
if "user" not in st.session_state:
        st.session_state["user"] = ""
# Login form
def show_login():
    st.title("🔐 Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if authenticate(username, password):
            st.success("Logged in successfully!")
            st.session_state["authenticated"] = True
            st.session_state["user"] = username
            st.rerun()
        else:
            st.error("Invalid username or password.")

    # st.markdown("---")
    # if st.button("Don't have an account? Register here"):
    #     st.session_state["page"] = "Register"
    #     st.rerun()
    st.markdown("---")
    st.markdown("Don't have an account? 👉 Select **Register** from the sidebar.")

# Register form
def show_register():
    st.title("📝 Register")
    username = st.text_input("Choose a Username")
    password = st.text_input("Choose a Password", type="password")
    confirm = st.text_input("Confirm Password", type="password")
    if st.button("Register"):
        if password != confirm:
            st.warning("Passwords do not match.")
        # elif save_user(username, password):
        elif save_user(username, password, role="customer"):
            st.session_state["register_success"] = True
            st.session_state["page"] = "Login"
            st.rerun()  # Trigger rerun — message will show on Login page
        else:
            st.error("Username already exists.")

        # Show register success message if redirected from Register
    if st.session_state.get("register_success"):
        st.success("User registered successfully! You can now login.")
        st.session_state["register_success"] = False  # reset flag after showing

    st.markdown("---")
    st.markdown("Already have an account? 👉 Select **Login** from the sidebar.")
# Main app content after login
# def show_dashboard():
#     st.title(f"🎉 Welcome {st.session_state['user']}!")
#     st.write("You are now logged in to the Customer Club.")
#     st.markdown("---")
#     st.subheader("📊 Dashboard coming soon...")

# Main router
def main():
    if "authenticated" not in st.session_state:
        st.session_state["authenticated"] = False

    if st.session_state["authenticated"]:
        role = get_user_role(st.session_state["user"])
        if role=="admin":

            menu = st.sidebar.radio("Menu", ["Dashboard","Manage Products", "Logout", "View Products", "Low Stock Alerts", "Customer Purchases"])
            if menu == "Dashboard":
                show_dashboard()
            elif menu=="Manage Products":
                admin_manage_products()
            elif menu=="Customer Purchases":
                show_costumer_purchase()
            elif menu=="View Products":
                admin_manage_products()
            elif menu=="Low Stock Alerts":
                show_low_stock_alert()
            elif menu=="Customer Purchases":
                show_costumer_purchase_history()

            elif menu == "Logout":
                st.session_state["authenticated"] = False
                st.session_state["user"] = ""
                st.success("You have been logged out.")
                st.rerun()
        elif role=="customer":
            menu = st.sidebar.radio("Menu", ["My Profile","Edit my Profile", "My Purcheses History","Do Purchase", "Logout"])
            if menu == "My Profile":

                customer_profile(st.session_state["user"], mode="view")
            elif menu=="Edit my Profile":

                customer_profile(st.session_state["user"], mode='edit')

            elif menu == "My Purcheses History":
                user_purchase_history(st.session_state["user"])

            elif menu == "Do Purchase":
                purchase_page()

            elif menu == "Logout":
                st.session_state["authenticated"] = False
                st.session_state["user"] = ""
                st.success("You have been logged out.")
                st.rerun()
    else:
        menu = st.sidebar.radio("Navigation", ["Login", "Register"])
        if menu == "Login":
            show_login()
        else:
            customer_register()

if __name__ == "__main__":
    main()