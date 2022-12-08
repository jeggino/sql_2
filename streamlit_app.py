# streamlit_app.py

import streamlit as st
import mysql.connector

config = {
  'user': 'root',
  'password': 'Platinum79',
  'host': '127.0.0.1',
  'database': 'pets',
  'raise_on_warnings': True
}

conn = mysql.connector.connect(**config)

# Perform query.
# Uses st.experimental_memo to only rerun when the query changes or after 10 min.
def run_query(query):
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()

rows = run_query("SELECT * FROM mytable;")

# Print results.
for row in rows:
    st.write(f"{row[0]} has a :{row[1]}:")
