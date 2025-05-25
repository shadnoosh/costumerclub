import os
import pandas as pd

ADMIN_NOTIFICATIONS_FILE = "data/admin_notifications.xlsx"

def notify_admin(purchase_data):
    if os.path.exists(ADMIN_NOTIFICATIONS_FILE):
        df = pd.read_excel(ADMIN_NOTIFICATIONS_FILE)
        df = pd.concat([df, pd.DataFrame([purchase_data])], ignore_index=True)
    else:
        df = pd.DataFrame([purchase_data])
    df.to_excel(ADMIN_NOTIFICATIONS_FILE, index=False)

def show_costumer_purchase():

    if os.path.exists(ADMIN_NOTIFICATIONS_FILE):
        df = pd.read_excel(ADMIN_NOTIFICATIONS_FILE)
        if df.empty:
            return pd.DataFrame(columns=["username","Product ID", "Product Name", "Quantity", "Total Price", "Purchase Date"])
        else:
            return df
    else:
        df = pd.DataFrame(columns=["username","Product ID", "Product Name", "Quantity", "Total Price", "Purchase Date"])
        df.to_excel(ADMIN_NOTIFICATIONS_FILE, index=False)
        return df
