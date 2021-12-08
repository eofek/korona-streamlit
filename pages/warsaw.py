import streamlit as st
import numpy as np
import pandas as pd
#from pages import utils

from pymongo import MongoClient
import re
import matplotlib.pyplot as plt
import seaborn as sns
import datetime
import matplotlib.ticker as ticker

def get_data():
    client = MongoClient("mongodb+srv://streamlit:$Upv.AF63u-WARG@covidcases.uh3sr.mongodb.net/covidCasesPL?retryWrites=true&w=majority")
    collection = client['covidCasesPL']['Warsaw']
    df = pd.DataFrame(list(collection.find({},{"_id":0})))

    return df

def app():
    st.title("wszyscy umrzemy")
    st.markdown("Przypadki w DC")
    
    cases = get_data()
    cases['date'] = pd.to_datetime(cases['date']).dt.tz_localize(None)
    cases.fillna(0, inplace=True)
    cases['cases'] = cases['cases'].astype(int)
    
    delta = []
    for index, row in cases.iterrows():
        if index < 7:
            delta.append(0)
        else:
            delta.append(cases.iloc[index]['cases']-cases.iloc[index-7]['cases'])
    cases['delta'] = pd.Series(delta)
    
    percdelta = []
    for index, row in cases.iterrows():
        if index < 7:
            percdelta.append(0)
        else:
            print(index, cases.iloc[index]['delta'], np.round((cases.iloc[index]['delta']/cases.iloc[index-7]['cases'])*100, 2) )
            percdelta.append((cases.iloc[index]['delta']/cases.iloc[index-7]['cases'])*100)

    cases['% change w/w'] = np.round(pd.Series(percdelta), 2)
    
    
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
