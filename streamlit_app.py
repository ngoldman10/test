from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import requests
import os
import openai

"""
This is an app
"""

openai.api_key = os.getenv(API_KEY)
mlist = openai.Model.list()
st.json(mlist,expanded=True)
