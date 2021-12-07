import streamlit as st
import pandas as pd
from pymongo import MongoClient

st.title("wszyscy umrzemy")

# df = pd.read_csv('przypadki.csv')
#
# st.write(df)

# Initialize connection.



def get_data():
    client = MongoClient("mongodb+srv://streamlit:$Upv.AF63u-WARG@covidcases.uh3sr.mongodb.net/covidCasesPL?retryWrites=true&w=majority")
    collection = client['covidCasesPL']['PL']
    df = pd.DataFrame(list(collection.find({},{"_id":0})))

    return df

items = get_data()

st.write(items)