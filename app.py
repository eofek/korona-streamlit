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
    collection = db.PL
    df = pd.DataFrame(list(collection.find()))

    return df

items = get_data()

st.write(items)