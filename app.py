import streamlit as st
import pandas as pd
import pymongo

st.title("wszyscy umrzemy")

# df = pd.read_csv('przypadki.csv')
#
# st.write(df)

# Initialize connection.
client = pymongo.MongoClient(**st.secrets["mongo"])

@st.cache(ttl=600)
def get_data():
    db = client.covidCasesPL
    items = client.PL.find()
    items = list(items)  # make hashable for st.cache
    return items

items = get_data()

st.write(items)