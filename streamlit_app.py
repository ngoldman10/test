import pandas as pd
import os
import streamlit as st
import openai

"""
This is an app
"""

prompt1 = st.text_input('Prompt', 'Tell me a joke')

openai.api_key = st.secrets.key
r = openai.Completion.create(
  model="text-davinci-003",
  prompt=prompt1,
  max_tokens=50,
  temperature=1
)

st.json(r,expanded=True)
