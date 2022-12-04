from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import requests
import openai

"""
This is an app
"""
key = ${{ secrets.API_KEY }}
openai.api_key = key
mlist = openai.Model.list()
st.json(mlist,expanded=True)
