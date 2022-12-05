import pandas as pd
import os
import streamlit as st
import openai

"""
This is an app
"""

openai.api_key = st.secrets.key
r = openai.Completion.create(
  model="text-davinci-003",
  prompt="Say this is a test",
  max_tokens=7,
  temperature=0
)

st.json(r,expanded=True)
