import pandas as pd
import streamlit as st
import openai

"""
This is an app
"""

openai.api_key = "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"

openai.Completion.create(
  model="text-davinci-003",
  prompt="Say this is a test",
  max_tokens=7,
  temperature=0
)
