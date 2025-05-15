import streamlit as st
import openai
from dotenv import load_dotenv
import os

load_dotenv()  # 讀取 .env 裡的環境變數

openai.api_key = os.getenv("OPENAI_API_KEY")

st.title("我的生成式AI聊天機器人")

prompt = st.text_input("請輸入問題")

if prompt:
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    st.write(response.choices[0].text.strip())
