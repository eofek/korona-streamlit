import streamlit as st
import pandas as pd
from pymongo import MongoClient
import numpy as np
import re
import matplotlib.pyplot as plt
import seaborn as sns
import datetime
import matplotlib.ticker as ticker

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

cases = get_data()
cases.sort_values(by='date',  ascending=True, inplace=True)
cases.reset_index(drop=True, inplace=True)

cases['cases'] = cases.cases.astype(int)

delta = []
for index, row in cases.iterrows():
    if index < 7:
        delta.append(0)
    else:
        delta.append(cases.iloc[index]['cases']-cases.iloc[index-7]['cases'])
cases['delta'] = pd.Series(delta)


palette= sns.color_palette('YlOrRd', cases.cases.count())
fig, axe = plt.subplots(figsize=(16,9))
axe.tick_params(axis='x', rotation=55, labelsize=18)
axe.tick_params(axis='y', rotation=55, labelsize=18)
axe.get_yaxis().set_major_formatter(ticker.FuncFormatter(lambda x, p: format(int(x), '_')))
sns.barplot(x=pd.to_datetime(cases.date).dt.strftime("%d-%b"), y=cases.cases,palette=palette);
sns.lineplot(x=pd.to_datetime(cases.date).dt.strftime("%d-%b"), y=cases.cases.rolling(7).mean(), color='r', linewidth=4)
axe.xaxis.set_major_locator(ticker.MultipleLocator(10))

st.pyplot(fig)



cases.sort_values(by='date',  ascending=False, inplace=True)
cases['date'] = cases['date'].dt.strftime("%d-%b")

st.table(cases)