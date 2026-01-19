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



