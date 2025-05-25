# dashboard.py
import streamlit as st
import pandas as pd
import plotly.express as px

@st.cache_data
def load_data():
    return pd.read_excel("data/purchase_history.xlsx", parse_dates=["Purchase Date"])

@st.cache_data
def load_products():
    return pd.read_excel("data/products.xlsx", parse_dates=["Product ID"])

    # products_df = pd.read_excel("data/products.xlsx")
    # purchases_df = pd.read_excel("data/purchase_history.xlsx")

# def show_dashboard():
#     df = load_data()
#
#     st.title("📊 Customer Club Dashboard")
#     st.markdown("---")
#
#     # --- DATE SELECTION ---
#     min_date = df["date"].min()
#     max_date = df["date"].max()
#     start_date, end_date = st.date_input("Select date range", [min_date, max_date])
#
#     if not isinstance(start_date, pd.Timestamp):
#         start_date = pd.to_datetime(start_date)
#     if not isinstance(end_date, pd.Timestamp):
#         end_date = pd.to_datetime(end_date)
#
#     df_filtered = df[(df["date"] >= start_date) & (df["date"] <= end_date)]
#
#     # --- KPI Cards ---
#     total_sales = df_filtered["amount"].sum()
#     sales_count = df_filtered.shape[0]
#     new_customers = df_filtered[df_filtered["is_new"] == True]["customer_name"].nunique()
#     old_customers = df_filtered[df_filtered["is_new"] == False]["customer_name"].nunique()
#     total_customers = df["customer_name"].nunique()
#     total_new_customers = df[df["is_new"] == True]["customer_name"].nunique()
#
#     st.markdown("### 📈 Key Performance Indicators")
#     col1, col2, col3 = st.columns(3)
#     col1.metric("💰 Total Sales", f"${total_sales:,.0f}")
#     col2.metric("🛒 Sales Count", sales_count)
#     col3.metric("👥 Total Customers", total_customers)
#
#     col4, col5, col6 = st.columns(3)
#     col4.metric("🧑‍🤝‍🧑 New Customers", new_customers)
#     col5.metric("🔁 Old Customers", old_customers)
#     col6.metric("📅 All-Time New Customers", total_new_customers)
#
#     st.markdown("---")
#
#     # --- FILTER BOARD ---
#     st.subheader("📋 Filter & Explore Data")
#     col1, col2, col3 = st.columns(3)
#     selected_product = col1.selectbox("Filter by Product", ["All"] + sorted(df["product"].unique().tolist()))
#     selected_level = col2.selectbox("Filter by Level", ["All"] + sorted(df["level"].unique().tolist()))
#     selected_type = col3.selectbox("Customer Type", ["All", "New", "Old"])
#
#     if selected_product != "All":
#         df_filtered = df_filtered[df_filtered["product"] == selected_product]
#     if selected_level != "All":
#         df_filtered = df_filtered[df_filtered["level"] == selected_level]
#     if selected_type == "New":
#         df_filtered = df_filtered[df_filtered["is_new"] == True]
#     elif selected_type == "Old":
#         df_filtered = df_filtered[df_filtered["is_new"] == False]
#
#     st.dataframe(df_filtered, use_container_width=True)
def show_low_stock_alert():
    st.markdown("### ⚠️ Low Stock Alerts")
    products_df = load_products()  # <- product list
    products_df.columns = products_df.columns.str.strip()
    low_stock_df = products_df[products_df["In Stock"] < 3]
    if not low_stock_df.empty:
        st.warning("The following products are low in stock:")
        st.dataframe(low_stock_df)
    else:
        st.success("All products are sufficiently stocked.")

def show_costumer_purchase_history():
    st.markdown("### 🧾 costumer purchase history is here")
    purchase_history_df=load_data()
    purchase_history_df.columns = purchase_history_df.columns.str.strip()
    st.warning("📑 here is the total history of purchased products:")
    st.dataframe(purchase_history_df)

def show_dashboard():
    # Load data
    # Correct the assignment
    purchases_df = load_data()  # <- purchase history (should contain 'Purchase Date')
    purchases_df.columns = purchases_df.columns.str.strip()

    products_df = load_products()  # <- product list
    products_df.columns = products_df.columns.str.strip()

    # --- Title ---
    st.title("📊 Customer Club Dashboard")
    st.markdown("---")

    # --- DATE SELECTION ---
    min_date = purchases_df["Purchase Date"].min()
    max_date = purchases_df["Purchase Date"].max()
    start_date, end_date = st.date_input("Select date range", [min_date, max_date])

    start_date = pd.to_datetime(start_date)
    end_date = pd.to_datetime(end_date)

    df_filtered = purchases_df[(purchases_df["Purchase Date"] >= start_date) & (purchases_df["Purchase Date"] <= end_date)]

    # --- KPI Cards ---
    total_sales = df_filtered["Total Price"].sum()
    sales_count = df_filtered.shape[0]
    total_customers = df_filtered["Username"].nunique()

    st.markdown("### 📈 Key Performance Indicators")
    col1, col2, col3 = st.columns(3)
    col1.metric("💰 Total Sales", f"${total_sales:,.0f}")
    col2.metric("🛒 Sales Count", sales_count)
    col3.metric("👥 Total Customers", total_customers)

    st.markdown("---")

    # --- SEARCH BAR ---
    st.subheader("🔍 Search & Filter Products")
    search_term = st.text_input("Search by Product Name or Customer")

    # --- FILTER BOARD ---
    col1, col2 = st.columns(2)
    selected_product = col1.selectbox("Filter by Product", ["All"] + sorted(purchases_df["Product Name"].unique().tolist()))
    selected_category = col2.selectbox("Filter by Category", ["All"] + sorted(products_df["Category"].unique().tolist()))

    # Apply filters
    if search_term:
        df_filtered = df_filtered[df_filtered.apply(
            lambda row: search_term.lower() in str(row["Product Name"]).lower()
                        or search_term.lower() in str(row["Username"]).lower(), axis=1)]
    if selected_product != "All":
        df_filtered = df_filtered[df_filtered["Product Name"] == selected_product]
    if selected_category != "All":
        df_filtered = df_filtered[df_filtered["Category"] == selected_category]

    # --- Filtered Table ---
    st.markdown("### 📊 Filtered Purchase Data")
    st.dataframe(df_filtered, use_container_width=True)

    # --- SALES TRENDS ---
    st.markdown("### 📈 Sales Overview")
    sales_by_date = df_filtered.groupby("Purchase Date")["Total Price"].sum().reset_index()
    sales_by_product = df_filtered.groupby("Product Name")["Total Price"].sum().reset_index()

    chart_col1, chart_col2 = st.columns(2)
    with chart_col1:
        st.bar_chart(sales_by_date.rename(columns={"Purchase Date": "index"}).set_index("index"))
    with chart_col2:
        st.bar_chart(sales_by_product.rename(columns={"Product Name": "index"}).set_index("index"))

    # --- LOW STOCK PRODUCTS ---
    # st.markdown("### ⚠️ Low Stock Alerts")
    # low_stock_df = products_df[products_df["In Stock"] < 3]
    # if not low_stock_df.empty:
    #     st.warning("The following products are low in stock:")
    #     st.dataframe(low_stock_df)
    # else:
    #     st.success("All products are sufficiently stocked.")
    show_low_stock_alert()
    #to show the costumers purchase history
    show_costumer_purchase_history

    # --- PIE CHART ---
    st.markdown("### 🧁 Product Sales Distribution")
    if not sales_by_product.empty:
        fig = px.pie(sales_by_product, values="Total Price", names="Product Name", title="Sales Share by Product")
        st.plotly_chart(fig, use_container_width=True)

    # --- DOWNLOAD OPTION ---
    st.markdown("### 📤 Export Filtered Data")
    csv = df_filtered.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="Download CSV",
        data=csv,
        file_name=f"filtered_sales_data_{start_date.date()}_to_{end_date.date()}.csv",
        mime="text/csv"
    )
