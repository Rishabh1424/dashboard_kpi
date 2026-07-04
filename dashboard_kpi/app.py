import streamlit as st
import pandas as pd
import plotly.express as px

# ----------------------------------
# Page Configuration
# ----------------------------------
st.set_page_config(
    page_title="Sales KPI Dashboard",
    page_icon="📊",
    layout="wide"
)

# ----------------------------------
# Dashboard Header
# ----------------------------------
st.title("📊 Sales KPI Dashboard")
st.markdown("### Real-Time Business Performance Overview")

# ----------------------------------
# Load Dataset
# ----------------------------------
df = pd.read_csv("sales_data.csv")

# Convert Date column
df["Date"] = pd.to_datetime(df["Date"])

# ----------------------------------
# KPI Calculations
# ----------------------------------
total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
total_orders = df["OrderID"].count()
total_customers = df["Customer"].nunique()

# ----------------------------------
# KPI Cards
# ----------------------------------
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("💰 Total Sales", f"${total_sales:,.0f}")

with col2:
    st.metric("📈 Total Profit", f"${total_profit:,.0f}")

with col3:
    st.metric("🛒 Total Orders", f"{total_orders}")

with col4:
    st.metric("👥 Customers", f"{total_customers}")

st.divider()

# ----------------------------------
# Monthly Sales Trend
# ----------------------------------
monthly_sales = (
    df.groupby(df["Date"].dt.strftime("%b"))["Sales"]
    .sum()
    .reindex(["Jan", "Feb", "Mar", "Apr", "May", "Jun"])
    .reset_index()
)

fig1 = px.line(
    monthly_sales,
    x="Date",
    y="Sales",
    markers=True,
    title="📈 Monthly Sales Trend"
)

st.plotly_chart(fig1, use_container_width=True)

# ----------------------------------
# Revenue By Category
# ----------------------------------
category_sales = (
    df.groupby("Category")["Sales"]
    .sum()
    .reset_index()
)

fig2 = px.bar(
    category_sales,
    x="Category",
    y="Sales",
    color="Category",
    title="📊 Revenue By Category"
)

st.plotly_chart(fig2, use_container_width=True)

# ----------------------------------
# Revenue Distribution Pie Chart
# ----------------------------------
fig3 = px.pie(
    category_sales,
    names="Category",
    values="Sales",
    hole=0.4,
    title="🥧 Revenue Distribution"
)

st.plotly_chart(fig3, use_container_width=True)

# ----------------------------------
# Sales By Region
# ----------------------------------
region_sales = (
    df.groupby("Region")["Sales"]
    .sum()
    .reset_index()
)

fig4 = px.bar(
    region_sales,
    x="Region",
    y="Sales",
    color="Region",
    title="🌍 Sales By Region"
)

st.plotly_chart(fig4, use_container_width=True)

# ----------------------------------
# Top 5 Sales Transactions
# ----------------------------------
st.subheader("🏆 Top 5 Sales Transactions")

top_sales = df.sort_values(
    by="Sales",
    ascending=False
).head(5)

st.dataframe(top_sales, use_container_width=True)

# ----------------------------------
# Complete Dataset
# ----------------------------------
st.subheader("📋 Complete Sales Dataset")

st.dataframe(df, use_container_width=True)