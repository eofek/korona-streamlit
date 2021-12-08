import streamlit as st
import pandas as pd
from pymongo import MongoClient
import numpy as np
import re
import matplotlib.pyplot as plt
import seaborn as sns
import datetime
import matplotlib.ticker as ticker
import math

from multipage import MultiPage
from pages import warsaw, poland

app = MultiPage()

app.add_page("Poland", poland.app)
app.add_page("Warsaw", warsaw.app)


app.run()