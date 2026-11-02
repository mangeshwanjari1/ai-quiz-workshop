
import streamlit as st
import sqlite3
import pandas as pd

st.title("SQLite Database Viewer")

conn = sqlite3.connect("quiz_attempts.db")

tables = pd.read_sql_query(
    "SELECT name FROM sqlite_master WHERE type='table'",
    conn
)

table = st.selectbox("Select Table", tables["name"])

data = pd.read_sql_query(
    f'SELECT * FROM "{table}"', conn
)

st.dataframe(data, use_container_width=True)

conn.close()
