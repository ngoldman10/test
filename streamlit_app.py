import pandas as pd
import os
import streamlit as st
import openai


prompt_start = ("Speak with the tone and vernacular of Stephen A. Smith from ESPN.\n\nPremise: Someone gets Stephen A. Smith started on ")
prompt_end = (", and Stephen A. Smith responds.\n\nStephen A. Smith:")
initial_topic = ("the best highways in America")

prompt1 = st.text_input('Prompt', initial_topic)

combo = (prompt_start + prompt1 + prompt_end)

openai.api_key = st.secrets.key

r = openai.Completion.create(
  model="text-davinci-003",
  prompt=combo,
  max_tokens=256,
  temperature=.9
)

rtext = r['choices'][0]['text']
rtext = rtext.replace("\n","")

st.write('')
st.write('')
st.write(rtext)
