<<<<<<< HEAD
import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt




st.title("📊 Sales Dashboard")


df = pd.read_csv("df.csv")

#Kpi Cards
total_sales = df["total_amounnt"].sum()
total_quantity = df["quantity"].sum()
total_orders = len(df)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("💰 Total Sales", f"₹ {total_sales}")

with col2:
    st.metric("📦 Total Quantity", f"{total_quantity:}")

with col3:
    st.metric("🧾 Total Orders", total_orders)

st.divider()


st.sidebar.header("📌 Dashboard Options")

option = st.sidebar.radio(
    "Select Analysis",
    ["City-wise Sales", "Category-wise Sales", "Top customers",'Top Cities','High valued orders']
)


if option == "City-wise Sales":
    st.subheader("🏙️ City-wise Sales")

    city_sales = (
        df.groupby("city")
        .agg({"quantity": "sum", "price": "sum"})
        .reset_index()
    )

    st.dataframe(city_sales, use_container_width=True)

    fig, ax = plt.subplots(dpi=400)
    ax.bar(city_sales["city"], city_sales["price"])
    ax.set_title("Total Sales by City")
    ax.set_ylabel("Sales")
    

    st.pyplot(fig)


elif option == "Category-wise Sales":
    st.subheader("📦 Category-wise Sales")

    category_sales = (
        df.groupby("category")
        .agg({"price": "sum", "quantity": "sum"})
        .sort_values(by="price", ascending=False)
        .reset_index()
        
    )

    st.dataframe(category_sales, use_container_width=True)

    fig, ax = plt.subplots()
    ax.barh(category_sales["category"], category_sales["price"])
    ax.set_title("Total Sales by Category")
    ax.set_xlabel("Sales")

    st.pyplot(fig)

# elif option == "":
#     st.subheader("🔎  Insights")

#     # ensure columns and types
#     if 'total_amounnt' in df.columns:
#         df['total_amount'] = df['total_amounnt']
#     elif 'total_amount' not in df.columns:
#         df['total_amount'] = df.get('total', np.nan)

#     df['order_date'] = pd.to_datetime(df['order_date'])
#     df['month'] = df['order_date'].dt.to_period('M').astype(str)
#     df['day_of_week'] = df['order_date'].dt.day_name()

#     total_sales = df['total_amount'].sum()
#     total_orders = len(df)
#     avg_order = df['total_amount'].mean()

elif option =="Top customers":

    st.subheader("**Top customers (by total spend)**")
    top_customers = df.groupby('customer')['total_amounnt'].sum().sort_values(ascending=False).reset_index()
    st.dataframe(top_customers.head(10), use_container_width=True)


elif option=='Top Cities':
    st.markdown("**Top Cities**")
    
    city_sales = df.groupby('city')['total_amounnt'].sum().sort_values(ascending=False)
    st.dataframe(city_sales)
    fig, ax = plt.subplots()
    ax.bar(city_sales.index, city_sales.values)
    ax.set_title('Sales by City')
    ax.set_ylabel('Sales')
    st.pyplot(fig)
    



elif option=='High valued orders':

    st.subheader("**High value orders (top 10)**")
    hv = df.nlargest(10, 'total_amounnt')[['order_id','customer','city','category','quantity','total_amounnt']]
    st.dataframe(hv.reset_index(drop=True), use_container_width=True)



=======
import numpy as np
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt




st.title("📊 Sales Dashboard")


df = pd.read_csv("df.csv")

#Kpi Cards
total_sales = df["total_amounnt"].sum()
total_quantity = df["quantity"].sum()
total_orders = len(df)

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("💰 Total Sales", f"₹ {total_sales}")

with col2:
    st.metric("📦 Total Quantity", f"{total_quantity:}")

with col3:
    st.metric("🧾 Total Orders", total_orders)

st.divider()


st.sidebar.header("📌 Dashboard Options")

option = st.sidebar.radio(
    "Select Analysis",
    ["City-wise Sales", "Category-wise Sales"]
)


if option == "City-wise Sales":
    st.subheader("🏙️ City-wise Sales")

    city_sales = (
        df.groupby("city")
        .agg({"quantity": "sum", "price": "sum"})
        .reset_index()
    )

    st.dataframe(city_sales, use_container_width=True)

    fig, ax = plt.subplots()
    ax.bar(city_sales["city"], city_sales["price"])
    ax.set_title("Total Sales by City")
    ax.set_ylabel("Sales")
    

    st.pyplot(fig)


elif option == "Category-wise Sales":
    st.subheader("📦 Category-wise Sales")

    category_sales = (
        df.groupby("category")
        .agg({"price": "sum", "quantity": "sum"})
        .sort_values(by="price", ascending=False)
        .reset_index()
        
    )

    st.dataframe(category_sales, use_container_width=True)

    fig, ax = plt.subplots()
    ax.barh(category_sales["category"], category_sales["price"])
    ax.set_title("Total Sales by Category")
    ax.set_xlabel("Sales")

    st.pyplot(fig)



>>>>>>> 3ee1a1a83c81f782f646eeb99deb70505ab67708
