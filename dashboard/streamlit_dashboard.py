import streamlit as st
import pandas as pd
import os
import plotly.express as px

st.set_page_config(
    page_title="Business Growth Analytics",
    page_icon="📊",
    layout="wide"
)

# =========================
# CUSTOM STYLING
# =========================

st.markdown("""
<style>

[data-testid="stSidebar"] {
    background-color: #111827;
}

[data-testid="stSidebar"] * {
    color: white;
}

.metric-card {
    background-color: #1f2937;
    padding: 15px;
    border-radius: 10px;
}

</style>
""", unsafe_allow_html=True)

# =========================
# LOAD DATA
# =========================

data_path = os.path.join("data", "processed", "cleaned_sales_data.csv")
df = pd.read_csv(data_path)

df["Order Date"] = pd.to_datetime(df["Order Date"])

# =========================
# TITLE
# =========================

st.title("📊 Business Growth Analytics Dashboard")
st.caption("Advanced analytics dashboard for business growth insights")

# =========================
# SIDEBAR FILTERS
# =========================

st.sidebar.title("⚙️ Analytics Filters")

st.sidebar.markdown("Filter data to explore business insights")

# REGION FILTER
region = st.sidebar.multiselect(
    "🌍 Region",
    options=sorted(df["Region"].unique()),
    default=sorted(df["Region"].unique())
)

# CATEGORY FILTER
category = st.sidebar.multiselect(
    "📦 Category",
    options=sorted(df["Category"].unique()),
    default=sorted(df["Category"].unique())
)

# SEGMENT FILTER
segment = st.sidebar.multiselect(
    "👥 Customer Segment",
    options=sorted(df["Segment"].unique()),
    default=sorted(df["Segment"].unique())
)

# DATE FILTER
start_date = st.sidebar.date_input(
    "📅 Start Date",
    df["Order Date"].min()
)

end_date = st.sidebar.date_input(
    "📅 End Date",
    df["Order Date"].max()
)

# RESET FILTER BUTTON
if st.sidebar.button("🔄 Reset Filters"):
    st.rerun()

# =========================
# APPLY FILTERS
# =========================

filtered_df = df[
    (df["Region"].isin(region)) &
    (df["Category"].isin(category)) &
    (df["Segment"].isin(segment)) &
    (df["Order Date"] >= pd.to_datetime(start_date)) &
    (df["Order Date"] <= pd.to_datetime(end_date))
]

# =========================
# KPI METRICS
# =========================

total_sales = filtered_df["Sales"].sum()
total_profit = filtered_df["Profit"].sum()
total_orders = filtered_df["Order ID"].nunique()
avg_discount = filtered_df["Discount"].mean()

col1, col2, col3, col4 = st.columns(4)

col1.metric("💰 Total Sales", f"${total_sales:,.0f}")
col2.metric("📈 Total Profit", f"${total_profit:,.0f}")
col3.metric("🛒 Total Orders", total_orders)
col4.metric("🏷 Avg Discount", f"{avg_discount:.2f}")

st.divider()

# =========================
# SALES TREND
# =========================

st.subheader("📈 Sales Trend")

sales_trend = (
    filtered_df.groupby("Order Date")["Sales"]
    .sum()
    .reset_index()
)

fig_trend = px.line(
    sales_trend,
    x="Order Date",
    y="Sales",
    title="Sales Over Time"
)

st.plotly_chart(fig_trend, use_container_width=True)

# =========================
# MONTHLY GROWTH
# =========================

st.subheader("📊 Monthly Growth Rate")

filtered_df["Month"] = filtered_df["Order Date"].dt.to_period("M")

monthly_sales = filtered_df.groupby("Month")["Sales"].sum()

growth_rate = monthly_sales.pct_change() * 100

fig_growth = px.line(
    x=growth_rate.index.astype(str),
    y=growth_rate.values,
    labels={"x": "Month", "y": "Growth %"},
    title="Monthly Growth Rate"
)

st.plotly_chart(fig_growth, use_container_width=True)

# =========================
# CATEGORY SALES
# =========================

st.subheader("📦 Category Performance")

category_sales = filtered_df.groupby("Category")["Sales"].sum().reset_index()

fig_category = px.bar(
    category_sales,
    x="Category",
    y="Sales",
    color="Category"
)

st.plotly_chart(fig_category, use_container_width=True)

# =========================
# CUSTOMER SEGMENT
# =========================

st.subheader("👥 Customer Segment Analysis")

segment_sales = filtered_df.groupby("Segment")["Sales"].sum().reset_index()

fig_segment = px.pie(
    segment_sales,
    names="Segment",
    values="Sales"
)

st.plotly_chart(fig_segment, use_container_width=True)

# =========================
# PROFIT VS DISCOUNT
# =========================

st.subheader("💰 Profit vs Discount")

fig_scatter = px.scatter(
    filtered_df,
    x="Discount",
    y="Profit",
    color="Category"
)

st.plotly_chart(fig_scatter, use_container_width=True)

# =========================
# TOP PRODUCTS
# =========================

st.subheader("🏆 Top Products")

top_products = (
    filtered_df.groupby("Product Name")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

st.dataframe(top_products)

# =========================
# REGION SALES
# =========================

st.subheader("🌍 Regional Sales")

region_sales = filtered_df.groupby("Region")["Sales"].sum().reset_index()

fig_region = px.bar(
    region_sales,
    x="Region",
    y="Sales",
    color="Region"
)

st.plotly_chart(fig_region, use_container_width=True)

# =========================
# TOP CITIES
# =========================

st.subheader("🏙 Top Cities")

city_sales = (
    filtered_df.groupby("City")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    .reset_index()
)

fig_city = px.bar(
    city_sales,
    x="City",
    y="Sales",
    color="City"
)

st.plotly_chart(fig_city, use_container_width=True)

# =========================
# WORLD MAP
# =========================

st.subheader("🌎 Global Sales Map")

country_sales = filtered_df.groupby("Country")["Sales"].sum().reset_index()

fig_map = px.choropleth(
    country_sales,
    locations="Country",
    locationmode="country names",
    color="Sales",
    color_continuous_scale="Blues"
)

st.plotly_chart(fig_map, use_container_width=True)