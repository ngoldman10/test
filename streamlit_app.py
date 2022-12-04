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

league_id = '865065387836960768'
league = League(league_id)

title = st.text_input('Movie title', 'user input')
st.write('Try this:', title)

league.get_rosters()
