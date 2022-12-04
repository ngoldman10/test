from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

"""
This is an app
"""


title = st.text_input('Movie title', 'user input')
st.write('Try this:', title)
