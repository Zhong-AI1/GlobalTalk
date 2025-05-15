import streamlit as st
from openai import OpenAI
import os

# 從環境變數讀取 API KEY
api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)

st.title("簡易測試")

if st.button("跟AI打招呼"):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": "你好"}]
    )
    st.write(response.choices[0].message.content)
