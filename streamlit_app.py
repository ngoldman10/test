import pandas as pd
import os
import streamlit as st
import openai

#prompt beginning and ending to pass to API
prompt_start = ("Speak with the tone and vernacular of Stephen A. Smith from ESPN.\n\nPremise: Someone gets Stephen A. Smith started on ")
prompt_end = (", and Stephen A. Smith responds.\n\nStephen A. Smith:")

#Variable to store text input
prompt1 = st.text_input('Prompt', "Enter a topic then press enter. **Ex: the best highways in America**", key="textkey")
combo = (prompt_start + prompt1 + prompt_end)
st.markdown("Enter a topic then press enter. **Ex: the best highways in America**")
st.write('')
st.write('')

#api key
openai.api_key = st.secrets.key

#main flow
#if st.session_state.textkey == "Enter a topic then press enter. Ex:the best highways in America":
  #st.write("I've got something to say when you press enter.")
#else:
  #r = openai.Completion.create(
    #model="text-davinci-003",
    #prompt=combo,
    #max_tokens=256,
    #temperature=.9)
  #rtext = r['choices'][0]['text']
  #rtext = rtext.replace("\n","")
  #st.write(rtext)
  #st.image("https://ih1.redbubble.net/image.2640223911.0420/st,small,507x507-pad,600x600,f8f8f8.jpg")

