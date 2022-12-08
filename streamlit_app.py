# streamlit_app.py

import streamlit as st
from  mysql import connector

# Initialize connection.
# Uses st.experimental_singleton to only run once.
def init_connection():
    return connector().connect(**st.secrets["mysql"])

conn = init_connection()

# Perform query.
# Uses st.experimental_memo to only rerun when the query changes or after 10 min.
def run_query(query):
    with conn.cursor() as cur:
        cur.execute(query)
        return cur.fetchall()

rows = run_query("SELECT * FROM pets.mytable;")

# Print results.
for row in rows:
    st.write(f"{row[0]} has a :{row[1]}:")
