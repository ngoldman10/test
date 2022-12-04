from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
import requests
from sleeper_wrapper import League

"""
This is an app
"""



title = st.text_input('Movie title', 'user input')
st.write('Try this:', title)

league_id = '865065387836960768'
league = League(league_id)
a = league.get_rosters()
st.json(a, expanded=True)
