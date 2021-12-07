import streamlit as st
import pandas as pd
import pymongo

st.title("wszyscy umrzemy")

# df = pd.read_csv('przypadki.csv')
#
# st.write(df)

# Initialize connection.



def get_data():
    lnk = "mongodb+srv://streamlit:$Upv.AF63u-WARG@covidcases-lb.uh3sr.mongodb.net/covidCasesPL?retryWrites=true&w=majority"
    client = pymongo.MongoClient(lnk)
    db = client.covidCasesPL
    collection = db.PL
    df = pd.DataFrame(list(collection.find()))

    return df

items = get_data()

st.write(items)