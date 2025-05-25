# import streamlit as st
# import pandas as pd
# import os
#
# PRODUCTS_FILE = "data/products.xlsx"
#
# def load_products():
#     if os.path.exists(PRODUCTS_FILE):
#         return pd.read_excel(PRODUCTS_FILE)
#     else:
#         # If file doesn't exist, create it with headers
#         df = pd.DataFrame(columns=["Product ID", "Product Name", "Category", "Model", "Size", "Color", "Price", "In Stock", "Description"])
#         df.to_excel(PRODUCTS_FILE, index=False)
#         return df
#
# def add_product():
#     st.markdown("#### ➕ Add a New Product")
#     df = load_products()
#
#     with st.form("add_product_form"):
#         product_id = st.text_input("Product ID")
#         name = st.text_input("Product Name")
#         category = st.selectbox("Category", ["Shirt", "Skirt", "Shawl", "Pants", "T-shirt"])
#         model = st.text_input("Model")
#         size = st.text_input("Size (e.g., M, L, 34, etc.)")
#         color = st.text_input("Color")
#         price = st.number_input("Price", min_value=0.0, step=1.0)
#         stock = st.number_input("In Stock", min_value=0, step=1)
#         desc = st.text_area("Description")
#
#         submitted = st.form_submit_button("Add Product")
#
#         if submitted:
#             new_row = {
#                 "Product ID": product_id,
#                 "Product Name": name,
#                 "Category": category,
#                 "Model": model,
#                 "Size": size,
#                 "Color": color,
#                 "Price": price,
#                 "In Stock": stock,
#                 "Description": desc
#             }
#             df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
#             save_products(df)
#             st.success(f"✅ Product '{name}' added successfully!")
#             st.rerun()
# def edit_product():
#     st.markdown("#### ✏️ Edit Product")
#     df = load_products()
#
#     product_names = df["Product Name"].tolist()
#     if not product_names:
#         st.info("No products to edit.")
#         return
#
#     selected = st.selectbox("Select Product to Edit", product_names)
#     product = df[df["Product Name"] == selected].iloc[0]
#
#     with st.form("edit_product_form"):
#         name = st.text_input("Product Name", product["Product Name"])
#         category = st.selectbox("Category", ["Shirt", "Skirt", "Shawl", "Pants", "T-shirt"],
#                                 index=["Shirt", "Skirt", "Shawl", "Pants", "T-shirt"].index(product["Category"]))
#         model = st.text_input("Model", product["Model"])
#         size = st.text_input("Size", product["Size"])
#         color = st.text_input("Color", product["Color"])
#         price = st.number_input("Price", min_value=0.0, value=float(product["Price"]), step=1.0)
#         stock = st.number_input("In Stock", min_value=0, value=int(product["In Stock"]), step=1)
#         desc = st.text_area("Description", product["Description"])
#
#         submitted = st.form_submit_button("Save Changes")
#
#         if submitted:
#             idx = df[df["Product Name"] == selected].index[0]
#             df.loc[idx] = {
#                 "Product ID": product["Product ID"],
#                 "Product Name": name,
#                 "Category": category,
#                 "Model": model,
#                 "Size": size,
#                 "Color": color,
#                 "Price": price,
#                 "In Stock": stock,
#                 "Description": desc
#             }
#             save_products(df)
#             st.success(f"✅ Product '{name}' updated successfully!")
#             st.rerun()
# def delete_product():
#     st.markdown("#### 🗑️ Delete Product")
#     df = load_products()
#
#     product_names = df["Product Name"].tolist()
#     if not product_names:
#         st.info("No products to delete.")
#         return
#
#     selected = st.selectbox("Select Product to Delete", product_names)
#
#     if st.button("Delete Product"):
#         df = df[df["Product Name"] != selected]
#         save_products(df)
#         st.success(f"🗑️ Product '{selected}' deleted successfully!")
#         st.rerun()
# def save_products(df):
#     df.to_excel(PRODUCTS_FILE, index=False)
#
# # def admin_manage_products():
# #     st.title("🧾 Manage Products (Admin Only)")
# #
# #     # Load existing products
# #     df = load_products()
# #
# #     # Show existing products
# #     st.subheader("📦 Product Inventory")
# #     st.dataframe(df)
# #
# #     st.markdown("---")
# #     st.subheader("➕ Add a New Product")
# #
# #     with st.form("add_product_form"):
# #         product_id = st.text_input("Product ID")
# #         name = st.text_input("Product Name")
# #         category = st.selectbox("Category", ["Shirt", "Skirt", "Shawl", "Pants", "T-shirt"])
# #         model = st.text_input("Model")
# #         size = st.text_input("Size (e.g., M, L, 34, etc.)")
# #         color = st.text_input("Color")
# #         price = st.number_input("Price", min_value=0.0, step=1.0)
# #         stock = st.number_input("In Stock", min_value=0, step=1)
# #         desc = st.text_area("Description")
# #
# #         submitted = st.form_submit_button("Add Product")
# #
# #         if submitted:
# #             new_row = {
# #                 "Product ID": product_id,
# #                 "Product Name": name,
# #                 "Category": category,
# #                 "Model": model,
# #                 "Size": size,
# #                 "Color": color,
# #                 "Price": price,
# #                 "In Stock": stock,
# #                 "Description": desc
# #             }
# #             df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
# #             save_products(df)
# #             st.success(f"✅ Product '{name}' added successfully!")
# def admin_manage_products():
#     st.title("🧾 Product Inventory (Admin Only)")
#
#     df = load_products()
#     if df.empty:
#         st.warning("No products available.")
#         return
#
#     st.subheader("📦 Current Product List")
#     st.dataframe(df)
#
#     st.markdown("### Manage Products")
#     action = st.selectbox("Select Action", ["Add New Product", "Edit Existing Product", "Delete Product"])
#
#     if action == "Add New Product":
#         add_product()
#
#
#     elif action == "Edit Existing Product":
#         edit_product()
#
#     elif action == "Delete Product":
#         delete_product()
#
#
import streamlit as st
import pandas as pd
import os

PRODUCTS_FILE = "data/products.xlsx"
IMAGE_DIR = "data/product_images"

def load_products():
    if os.path.exists(PRODUCTS_FILE):
        return pd.read_excel(PRODUCTS_FILE)
    else:
        df = pd.DataFrame(columns=["Product ID", "Product Name", "Category", "Model", "Size", "Color",
                                   "Price", "In Stock", "Description", "Image Path"])
        df.to_excel(PRODUCTS_FILE, index=False)
        return df

def save_products(df):
    df.to_excel(PRODUCTS_FILE, index=False)

def add_product():
    st.markdown("#### ➕ Add a New Product")
    df = load_products()

    with st.form("add_product_form"):
        product_id = st.text_input("Product ID")
        name = st.text_input("Product Name")
        category = st.selectbox("Category", ["Shirt", "Skirt", "Shawl", "Pants", "T-shirt"])
        model = st.text_input("Model")
        size = st.text_input("Size (e.g., M, L, 34, etc.)")
        color = st.text_input("Color")
        price = st.number_input("Price", min_value=0.0, step=1.0)
        stock = st.number_input("In Stock", min_value=0, step=1)
        desc = st.text_area("Description")
        image = st.file_uploader("Upload Product Image", type=["jpg", "png", "jpeg"])

        submitted = st.form_submit_button("Add Product")

        if submitted:
            image_path = ""
            if image:
                os.makedirs(IMAGE_DIR, exist_ok=True)
                image_path = os.path.join(IMAGE_DIR, image.name)
                with open(image_path, "wb") as f:
                    f.write(image.read())

            new_row = {
                "Product ID": product_id,
                "Product Name": name,
                "Category": category,
                "Model": model,
                "Size": size,
                "Color": color,
                "Price": price,
                "In Stock": stock,
                "Description": desc,
                "Image Path": image_path
            }
            df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
            save_products(df)
            st.success(f"✅ Product '{name}' added successfully!")
            st.rerun()

def edit_product():
    st.markdown("#### ✏️ Edit Product")
    df = load_products()

    product_names = df["Product Name"].tolist()
    if not product_names:
        st.info("No products to edit.")
        return

    selected = st.selectbox("Select Product to Edit", product_names)
    product = df[df["Product Name"] == selected].iloc[0]

    with st.form("edit_product_form"):
        name = st.text_input("Product Name", product["Product Name"])
        category = st.selectbox("Category", ["Shirt", "Skirt", "Shawl", "Pants", "T-shirt"],
                                index=["Shirt", "Skirt", "Shawl", "Pants", "T-shirt"].index(product["Category"]))
        model = st.text_input("Model", product["Model"])
        size = st.text_input("Size", product["Size"])
        color = st.text_input("Color", product["Color"])
        price = st.number_input("Price", min_value=0.0, value=float(product["Price"]), step=1.0)
        stock = st.number_input("In Stock", min_value=0, value=int(product["In Stock"]), step=1)
        desc = st.text_area("Description", product["Description"])
        image = st.file_uploader("Update Product Image (optional)", type=["jpg", "png", "jpeg"])

        submitted = st.form_submit_button("Save Changes")

        if submitted:
            image_path = product["Image Path"]
            if image:
                os.makedirs(IMAGE_DIR, exist_ok=True)
                image_path = os.path.join(IMAGE_DIR, image.name)
                with open(image_path, "wb") as f:
                    f.write(image.read())

            idx = df[df["Product Name"] == selected].index[0]
            df.loc[idx] = {
                "Product ID": product["Product ID"],
                "Product Name": name,
                "Category": category,
                "Model": model,
                "Size": size,
                "Color": color,
                "Price": price,
                "In Stock": stock,
                "Description": desc,
                "Image Path": image_path
            }
            save_products(df)
            st.success(f"✅ Product '{name}' updated successfully!")
            st.rerun()

def delete_product():
    st.markdown("#### 🗑️ Delete Product")
    df = load_products()

    product_names = df["Product Name"].tolist()
    if not product_names:
        st.info("No products to delete.")
        return

    selected = st.selectbox("Select Product to Delete", product_names)

    if st.button("Delete Product"):
        df = df[df["Product Name"] != selected]
        save_products(df)
        st.success(f"🗑️ Product '{selected}' deleted successfully!")
        st.rerun()

def admin_manage_products():
    st.title("🧾 Product Inventory (Admin Only)")

    df = load_products()
    if df.empty:
        st.warning("No products available.")
    else:
        st.subheader("📦 Current Product List")

        for _, row in df.iterrows():
            st.markdown(f"### 🏷️ {row['Product Name']}")
            if pd.notna(row["Image Path"]) and os.path.exists(row["Image Path"]):
                st.image(row["Image Path"], width=150)
            st.write(f"**Category**: {row['Category']} | **Model**: {row['Model']}")
            st.write(f"**Size**: {row['Size']} | **Color**: {row['Color']}")
            st.write(f"**Price**: ${row['Price']} | **Stock**: {row['In Stock']}")
            st.write(f"**Description**: {row['Description']}")
            st.markdown("---")

    st.markdown("### Manage Products")
    action = st.selectbox("Select Action", ["Add New Product", "Edit Existing Product", "Delete Product"])

    if action == "Add New Product":
        add_product()
    elif action == "Edit Existing Product":
        edit_product()
    elif action == "Delete Product":
        delete_product()