import streamlit as st
import sqlite3
import pandas as pd
import datetime
import plotly.express as px

def get_connection():
    conn = sqlite3.connect("sales.db")
    return conn

def load_data():
    conn = get_connection()
    df = pd.read_sql("SELECT * FROM sales", conn)
    conn.close()
    return df

def add_sale(product, quantity, price, date):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO sales (product, quantity, price, date) VALUES (?, ?, ?, ?)",
        (product, quantity, price, date)
    )
    conn.commit()
    conn.close()
    st.success("Dodano nowy rekord sprzedaży!")
    st.balloons()

st.title("Aplikacja sprzedażowa - Sales Dashboard")

st.header("Dodaj nową sprzedaż")
with st.form("add_form"):
    product = st.text_input("Produkt")
    quantity = st.number_input("Ilość", min_value=1, step=1)
    price = st.number_input("Cena jednostkowa", min_value=0.0, step=0.01)
    date = st.date_input("Data sprzedaży", datetime.date.today())
    submitted = st.form_submit_button("Dodaj")
    if submitted:
        add_sale(product, quantity, price, date.strftime("%Y-%m-%d"))

st.header("Dane sprzedaży")
df = load_data()

products = df['product'].unique()
selected_product = st.selectbox("Wybierz produkt do filtrowania (wszystkie dla pełnej listy)", ["Wszystkie"] + list(products))
if selected_product != "Wszystkie":
    df = df[df['product'] == selected_product]

st.dataframe(df)

st.header("Wykresy sprzedaży")

df['total'] = df['quantity'] * df['price']
daily_sales = df.groupby('date')['total'].sum().reset_index()
fig1 = px.bar(daily_sales, x='date', y='total', title="Sprzedaż dzienna (wartość)")
st.plotly_chart(fig1)

product_sales = df.groupby('product')['quantity'].sum().reset_index()
fig2 = px.pie(product_sales, names='product', values='quantity', title="Suma sprzedanych produktów")
st.plotly_chart(fig2)

if st.checkbox("Pokaż surowe dane"):
    st.subheader("Surowe dane")
    st.write(df)
