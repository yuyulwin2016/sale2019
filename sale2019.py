import pandas as pd
import streamlit as st
import plotly.express as px
st.set_page_config(page_title = "Sale Dashboard 2019", page_icon = ":bar_chart:", layout = "wide")
df = pd.read_csv('all_df.csv')
st.sidebar.header('Please Filter Here')
product_name = st.sidebar.multiselect(
    "Select Product: ",
    options = df['Product'].unique(),
    default = df['Product'].unique()[:5]
)
city_name = st.sidebar.multiselect(
    "Select City: ",
    options = df['City'].unique(),
    default = df['City'].unique()[:5]
)
month_name = st.sidebar.multiselect(
    "Select Month: ",
    options = df['Month'].unique(),
    default = df['Month'].unique()[:5]
)
st.title(":bar_chart: Sale Dashboard 2019")
total = df['Total'].sum()
no_of_product = df['Product'].nunique()
a, b = st.columns(2)
c,d,e = st.columns(3)
f,g = st.columns(2)

with a:
    st.subheader('Total Sale')
    st.subheader(f"US $ {total}")
with b:
    st.subheader('No. of Product')
    st.subheader(no_of_product)
df_select = df.query("Product == @product_name and Month == @month_name and City == @city_name")

sale_by_product = df_select.groupby('Product')['Total'].sum().sort_values()
fig_by_product = px.bar(
    sale_by_product,
    x = sale_by_product.values,
    y = sale_by_product.index,
    title = "Sale by Product"
)
c.plotly_chart(fig_by_product, use_container_width = True)

fig_by_city = px.pie(
    df_select,
    values = 'Total',
    names = 'City',
    title = 'Sale by City'
)
d.plotly_chart(fig_by_city, use_container_width = True)

sale_by_month = df_select.groupby('Month')['Total'].sum().sort_values()
fig_by_month = px.bar(
    sale_by_month,
    x = sale_by_month.values,
    y = sale_by_month.index,
    title = "Sale by Month"
)
e.plotly_chart(fig_by_month, use_container_width = True)

fig_by_month = px.line(
    sale_by_month,
    x = sale_by_month.values,
    y = sale_by_month.index,
    title = "Sale by Month"
)
f.plotly_chart(fig_by_month, use_container_width = True)

fig_by_quantity = px.scatter(
    df_select,
    x = 'Total',
    y = 'QuantityOrdered',
    title = "Sale Amount Total"
)
g.plotly_chart(fig_by_quantity, use_container_width = True)