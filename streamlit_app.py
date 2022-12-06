import pandas as pd
import os
import streamlit as st
import openai


prompt_start = ("Speak with the tone and vernacular of Stephen A. Smith from ESPN.\n\nPremise: Someone gets Stephen A. Smith started on ")
prompt_end = (", and Stephen A. Smith responds.\n\nStephen A. Smith:")
#initial_topic = ("the best highways in America")


prompt1 = st.text_input('Prompt', "Enter a topic then press enter. Ex:the best highways in America", key="textkey")

st.write(st.session_state.textkey)

if st.session_state.textkey == "Enter a topic then press enter. Ex:the best highways in America":
    st.write("Have not begun")
else:
    st.write("We have indeed begun!")

combo = (prompt_start + prompt1 + prompt_end)

#openai.api_key = st.secrets.key

#r = openai.Completion.create(
#  model="text-davinci-003",
#  prompt=combo,
#  max_tokens=256,
#  temperature=.9)

#rtext = r['choices'][0]['text']
#rtext = rtext.replace("\n","")

st.write('')
st.write('')

display = st.radio(
    "Start the show",
    ('Still airing Get Up!', 'First take is now Live'))

if display == 'Still airing Get Up!':
    st.write("Don't touch that dial!")
else:
    st.write("Good to go!")
    #st.write(rtext)
    #st.image("https://ih1.redbubble.net/image.2640223911.0420/st,small,507x507-pad,600x600,f8f8f8.jpg")

